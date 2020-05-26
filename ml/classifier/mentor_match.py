import joblib # Joblib is such an pacakge that can simply turn our Python code into parallel computing mode and of course increase the computing speed.
import pandas as pd


class MentorMatchClassifier: # constructor to load preprocesign objects from jupiter notebook
    def __init__(self):
        path_to_responses_file = "../../research/" # load our data from jupyter noteboook
        self.encoders = joblib.load(path_to_responses_file + "encoders.joblib") # reconstruct a python object from a file with the use of joblib
        self.model = joblib.load(path_to_responses_file + "random_forest.joblib") 
# 

# creating preprocessig method which takes JSON data as input 
def preprocessing(self, input_data):
    #add all preprocessing steps 
    input_data = pd.DataFrame(input_data, index = 0)
    mapping  = map_Mwhy(path_to_responses_file)
    map_pro = map_professions()
    
    #apply pre-processing (cleanup and scoring)
    for column in [
        'Timestamp',
        'mOs',
        'Mindustry',
        'Bregion',
        'mWhy',
        'Mwhy',
        'gender', 
        'yearsExp',
        'CompSize',
        'Profession',
        'track',
        'ethnicity',
        'Growth',
        'Groups'
    ]:
        #cleaning data
        categorical_convert = self.encoders[column] #
        input_data[column] = categorical_convert.transform(input_data[column])

    return input_data

#create a predict the method that intakes processed, score data and returns 1-1 match
# Predict method : this method calls ML for computing predictions on prepared data,
def predict(self, input_data):
    return self.model.predict_proba(input_data) # Predict_proba will give the only probability of 1 


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

