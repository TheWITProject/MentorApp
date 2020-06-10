import os
import joblib
import pandas as pd
import json
from ml.mentor_match_classifier.mentor_match_utils import MentorMatchingMethods


class MentorMatchClassifier: # constructor to load preprocesign objects from jupiter notebook
    def __init__(self):
        self.mm = MentorMatchingMethods()

    # creating preprocessig method which takes JSON data as input 
    def preprocessing(self, input_data):
        input_data = pd.DataFrame(input_data)
        input_data = self.mm.fix_df_arrays(input_data)
        input_data = self.mm.create_user_id(input_data)
        print('input data:')
        print(input_data)
        return input_data

    # create a predict the method that intakes processed, score data and returns 1-1 match
    # Predict method : this method calls ML for computing predictions on prepared data,
    def predict(self, input_data):
        score_matrix = self.mm.create_score_matrix(input_data)
        score_matrix = self.mm.assign_id(input_data, score_matrix)
        score_matrix = self.mm.calculate_match_scores(input_data, score_matrix)
        print('score matrix:')
        print(score_matrix)
        mentor_pref_dict, mentor_pref_dict_5 = self.mm.top_matches_mentor(score_matrix)
        student_pref_dict, student_pref_dict_5 = self.mm.top_matches_student(score_matrix)
        matches = self.mm.get_mentor_match(mentor_pref_dict, student_pref_dict)    
        print('matches:')
        print(matches)
        return matches

    def postprocessing(self, prediction, input_data):
        match_json_result = self.mm.matches_to_json(input_data, prediction)
        print('matches in json:')
        print(match_json_result)
        return {"matches": match_json_result, "status": "OK"}

    def compute_prediciton(self, input_data):
        try:
            input_data = self.preprocessing(input_data)
            prediction = self.predict(input_data)
            print('prediction:')
            print(prediction)
            prediction = self.postprocessing(prediction, input_data)
            print(prediction)
        except Exception as e:
            return {"status": "Error" ," message": str(e)}
        
        return prediction