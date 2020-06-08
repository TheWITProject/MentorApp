import joblib # Joblib is such an package that can simply turn our Python code into parallel computing mode and of course increase the computing speed.
import pandas as pd


class MentorMatchClassifier: # constructor to load preprocesign objects from jupiter notebook
    def __init__(self):
        # TO DO: fix path here to be relative
        path_to_responses_file = '/Users/ezronis/dev/MentorApp/research/'
        self.fix_df_arrays = joblib.load(path_to_responses_file + "fix_df_arrays.joblib")
        self.create_user_id = joblib.load(path_to_responses_file + "create_user_id.joblib")
        self.create_score_matrix = joblib.load(path_to_responses_file + "create_score_matrix.joblib")
        self.assign_id = joblib.load(path_to_responses_file + "assign_id.joblib")
        self.calculate_match_scores = joblib.load(path_to_responses_file + "calculate_match_scores.joblib")
        self.top_matches_mentor = joblib.load(path_to_responses_file + "top_matches_mentor.joblib")
        self.top_matches_student = joblib.load(path_to_responses_file + "top_matches_student.joblib")
        self.get_mentor_match = joblib.load(path_to_responses_file + "get_mentor_match.joblib")
        self.matches_to_json = joblib.load(path_to_responses_file + "matches_to_json.joblib")

    # creating preprocessig method which takes JSON data as input 
    def preprocessing(self, input_data):
        input_data = pd.DataFrame(input_data, index=[0])
        input_data = self.fix_df_arrays(input_data)
        input_data = self.create_user_id(input_data)
        return input_data

    # create a predict the method that intakes processed, score data and returns 1-1 match
    # Predict method : this method calls ML for computing predictions on prepared data,
    def predict(self, input_data):
        score_matrix = self.create_score_matrix(input_data)
        score_matrix = self.assign_id(input_data, score_matrix)
        score_matrix = self.calculate_match_scores(score_matrix, input_data)
        mentor_pref_dict, mentor_pref_dict_5 = self.top_matches_mentor(score_matrix)
        student_pref_dict, student_pref_dict_5 = self.top_matches_student(score_matrix)
        matches = self.get_mentor_match(mentor_pref_dict, student_pref_dict)

        return matches

    def postprocessing(self, prediction, input_data):
        match_json_result = self.matches_to_json(prediction, input_data)

        return {"matches": match_json_result, "status": "OK"}

    def compute_prediciton(self, input_data):
        try:
            input_data = self.preprocessing(input_data)
            prediction = self.predict(input_data)
            prediction = self.postprocessing(prediction, input_data)
        except Exception as e:
            return {"status": "Error" ," message": str(e)}
        
        return prediction

