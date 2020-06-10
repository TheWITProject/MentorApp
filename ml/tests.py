import json
import os

from django.test import TestCase

from ml.mentor_match_classifier.mentor_match import MentorMatchClassifier
import inspect
from ml.registry import MLRegistry

class MLTests(TestCase):
    def test_mentormatch_algorithm(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/../research/surveys.json') as json_file:
            input_data = json.load(json_file)
        mentor_match_alg = MentorMatchClassifier()
        response = mentor_match_alg.compute_prediciton(input_data)
        self.assertEqual('OK', response['status'])
        self.assertTrue('matches' in response)

    def test_registry(self):
        registry = MLRegistry()
        self.assertEqual(len(registry.endpoints), 0)
        endpoint_name = "mentor_match_classifier"
        algorithm_object = MentorMatchClassifier()
        algorithm_name = "mentor match algos"
        algorithm_status = "production"
        algorithm_version = "0.0.1"
        algorithm_description = "matching mentors to students"
        algorithm_owner = "The WIT Project"
        algorithm_code = inspect.getsource(MentorMatchClassifier)
        # add to registry
        registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
                    algorithm_status, algorithm_version, algorithm_owner,
                    algorithm_description, algorithm_code)
        # there should be one endpoint available
        self.assertEqual(len(registry.endpoints), 1)