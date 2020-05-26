import joblib # Joblib is such an package that can simply turn our Python code into parallel computing mode and of course increase the computing speed.
import pandas as pd


class MentorMatchClassifier: # constructor to load preprocesign objects from jupiter notebook
    def __init__(self):
        path_to_responses_file = "../../matching_algo_notebook/" # load our data from jupyter noteboook
        self.FormatFile = joblib.load(path_to_responses_file + "FormatFile.joblib")
        self.map_Mwhy = joblib.load(path_to_responses_file + "map_Mwhy.joblib") # reconstruct a python object from a file with the use of joblib
        self.map_professions = joblib.load(path_to_responses_file + "map_professions.joblib") 
        self.join_df = joblib.load(path_to_responses_file + "join_df.joblib") 
        self.user_id = joblib.load(path_to_responses_file + "user_id.joblib") 
        self.score_df = joblib.load(path_to_responses_file + "score_df.joblib") 
        self.assign_id = joblib.load(path_to_responses_file + "assign_id.joblib") 
        self.final_score = joblib.load(path_to_responses_file + "final_score.joblib")
        self.group_equal = joblib.load(path_to_responses_file + "group_equal.joblib")
        self.insert_score = joblib.load(path_to_responses_file + "insert_score.joblib")
        self.top_matches_mentor = joblib.load(path_to_responses_file + "top_matches_mentor.joblib")
        self.top_matches_student = joblib.load(path_to_responses_file + "top_matches_student.joblib")
        self.hospital_resident = joblib.load(path_to_responses_file + "hospital_resident.joblib")
        
#

# creating preprocessig method which takes JSON data as input 
def preprocessing(self, input_data):
    # add all preprocessing steps : 
    response_file = self.FormatFile(input_data)
    var = self.map_Mwhy(response_file)
    var = self.map_professions(var)
    match_df = self.join_df(response_file, var)
    match_df = self.user_id(match_df) #c is match_df 
    match_sc = self.score_df(match_df)
    match_sc = self.assign_id(match_df, match_sc) #match_sc
    

    return match_sc, match_df

#create a predict the method that intakes processed, score data and returns 1-1 match
# Predict method : this method calls ML for computing predictions on prepared data,
def predict(self, input_data):
    match_sc, match_df = preprocessing(input_data)
    match_sc = self.insert_score(match_sc, match_df) # new mathc_sc
    mentor_pref_dict = self.top_matches_mentor(match_sc) #returns mentor_pref_df
    student_pref_dict = self.top_matches_student(match_sc) #return student_pref
    matches = self.hospital_resident(mentor_pref_dict,student_pref_dict)

    return matches # Predict_proba will give the only probability of 1 

#create a post processing method that takes in match results and returns it in a serialized format
# FIXED

def postprocessing(self, input_data):

    label = "GoodMatch" # predict whether or not we have a match 
    if input_data[1] > 0.5:
        label = ""

    return {"Best match": input_data[1], }


    # serialized format should return mentor-student match 

# this method combines preprocessing, predict, and postprocessing and returns JSON object with responses
def compute_prediciton(self, input_data):
    try:
        input_data = self.preprocessing(input_data)
        prediction = self.predict(input_data)[0]
        prediction = self.postprocessing(prediction)
    except Exception as e:
        return {"status": "Error" ," message": str(e)}
    
    return prediction

