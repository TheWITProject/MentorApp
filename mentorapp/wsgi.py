"""
WSGI config for mentorapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
application = get_wsgi_application()

# ML registry
import inspect
from ml.registry import MLRegistry
from ml.mentor_match_classifier.mentor_match import MentorMatchClassifier

try:
    registry = MLRegistry() # create ML registry
    # Random Forest classifier
    mm = MentorMatchClassifier()
    # add to ML registry
    registry.add_algorithm(endpoint_name="mentor_match_classifier",
                            algorithm_object=mm,
                            algorithm_name="mentor matching",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="The WIT Project",
                            algorithm_description="Matching mentors to students",
                            algorithm_code=inspect.getsource(MentorMatchClassifier))
except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))