import json
import os

from django.test import TestCase

from ml.mentor_match_classifier.mentor_match import MentorMatchClassifier
import inspect
from ml.registry import MLRegistry

class MLTests(TestCase):
    def test_rf_algorithm(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/surveys.json') as json_file:
            input_data = json.load(json_file)
        mentor_match_alg = MentorMatchClassifier()
        response = mentor_match_alg.compute_prediciton(input_data)
        self.assertEqual('OK', response['status'])
        self.assertTrue('matches' in response)