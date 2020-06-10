from ast import literal_eval
import numpy as np 

def count_equal_responses(self, student, mentor):
        count = 0
        if isinstance(student, (int, np.integer)):
            count += 0
        elif '[' in student:
            student = literal_eval(student)
            mentor = literal_eval(mentor)
            for x in student: 
                for y in mentor:
                    if x == y: 
                        count += 1
        elif ( '[' not in student and type(student) is str):
            if student == mentor:
                count += 1
        return count