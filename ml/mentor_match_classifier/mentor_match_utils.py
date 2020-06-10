import pandas as pd 
import numpy as np 
import random 
import string 
from ast import literal_eval

from matching import Player  
from matching.games import HospitalResident

from ml.mentor_match_classifier.utils import count_equal_responses

class MentorMatchingMethods:

    def fix_df_arrays(self, surveys):
        return surveys.replace(regex=';', value =',') 

    def create_user_id(self, surveys): 
        letters = string.ascii_lowercase
        unique_id = [] 
        for i in range(0, surveys.shape[0]): 
            unique_id.append(( ''.join(random.choice(letters) for i in range(10)) ))

        # creating column of unique ids  
        surveys['ID'] = unique_id
        return surveys

    def create_score_matrix(self, surveys):
        student_subset_df = surveys[surveys['Are you a Mentor or Student?'] == 'student']
        mentor_subset_df = surveys[surveys['Are you a Mentor or Student?']== 'mentor']

        score_matrix = pd.DataFrame(np.zeros(shape = (student_subset_df.shape[0],mentor_subset_df.shape[0])))
        score_matrix.columns = student_subset_df['ID']
        return score_matrix 

    def assign_id(self, surveys, score_matrix): 
        mentor_subset_df = surveys[surveys['Are you a Mentor or Student?']== 'mentor']
        mentor_subset_df.reset_index(drop=True, inplace=True)  #only thing is how to gain access to the df here 
        score_matrix['mentor_id'] = mentor_subset_df['ID']
        score_matrix.set_index('mentor_id', inplace = True)
        return score_matrix 

    def final_score(self, region, no_group, with_group):
        # if(region == 0):     #if the mentor/mentee have dif regions
        #     return 0
        # else:
            # return (no_group + with_group)
        return (no_group + with_group)

    def calculate_match_scores(self, surveys, score_matrix):
        # iterating over students in score matrix
        for i in score_matrix:
            # getting student[i] survey responses from survey dataframe
            student = surveys[surveys['ID'] == i]
            for j in score_matrix.iterrows():
                # getting mentor[j] survey responses from survey dataframe
                mentor = surveys[surveys['ID'] == j[0]]
                # time to compare student to every mentor and get a score
                score = 0
                for col in surveys.columns:
                    count = count_equal_responses(student[col].squeeze(), mentor[col].squeeze())
                    score += count
                score_matrix[i][j[0]] = score
        return score_matrix

    def top_matches_mentor(self, score_matrix): 
        mentor_pref_dict_5 = {}
        mentor_pref_dict = {}
        for x,y in score_matrix.iterrows():
            mentor_pref_dict_5[x] = np.array(y.nlargest().index.values)
            mentor_pref_dict[x] = np.array(y.nlargest(len(y)).index.values)
        return mentor_pref_dict, mentor_pref_dict_5

    def top_matches_student(self, score_matrix): 
        student_pref_dict_5 = {} #store in dict
        student_pref_dict = {} #store in dict
        for x in score_matrix:
            student_pref_dict_5[x] = np.array(score_matrix[x].nlargest().index.values)
            student_pref_dict[x] = np.array(score_matrix[x].nlargest(len(score_matrix[x])).index.values)
        return student_pref_dict, student_pref_dict_5

    def get_mentor_match(self, mentor_pref_dict, student_pref_dict): 
        capacities = {mentor: 1 for mentor in mentor_pref_dict}

        # documentation: https://github.com/daffidwilde/matching
        game = HospitalResident.create_from_dictionaries(student_pref_dict, mentor_pref_dict, capacities)
        matches = game.solve()
        
        return matches

    def matches_to_json(self, surveys, matches):
        # getting array of mentor ifs from game results
        mentor_ids = list(matches.keys())
        mentor_ids = [str(item) for item in mentor_ids]

        # getting array of student ids from game results
        student_ids = list(matches.values())
        student_ids = [str(item[0]) for item in student_ids]

        # creating user id list
        user_ids = mentor_ids + student_ids

        # creating match list
        matches_ids = student_ids + mentor_ids

        # creating dataframe with mentor and student matches
        matches_df = pd.DataFrame(user_ids,columns = ['User IDs'])
        matches_df['Match IDs'] = matches_ids
        print(matches_df)

        # replacing randomly generated IDs with database user ids
        user_id = []
        match_id = []
        for mentor in matches_df['User IDs']:
            user_id.append(int(surveys.loc[surveys['ID'] == mentor]['user_id'].values))

        for student in matches_df['Match IDs']:
            match_id.append(int(surveys.loc[surveys['ID'] == student]['user_id'].values))

        matches_df['User IDs'] = user_id
        matches_df['Match IDs'] = match_id
        print(matches_df)
        return matches_df.to_json()