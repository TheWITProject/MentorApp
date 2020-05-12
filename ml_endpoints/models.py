from django.db import models

# 
class Endpoint(models.Model): # It is where the API will be served and eventually will be the API url.
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

class MLAlgorithm(models.Model): # Algorithm object, it contains the actual model and we need it to call the algorithm
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=50000)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)


class MLAlgorithmStatus(models.Model): # it's debugging and checking the status algo. it can start at any of these stages: testing, staging, production, ab_testing  
    status = models.CharField(max_length=128)
    active = models.BooleanField()
    created_by = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE, related_name = "status")

class MLRequest(models.Model): #This is where the data gets inputed request by the client and where the information is hold for giving out the match.
    input_data = models.CharField(max_length=10000)
    full_response = models.CharField(max_length=10000)
    response = models.CharField(max_length=10000)
    feedback = models.CharField(max_length=10000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE) # This is used to compute the response
