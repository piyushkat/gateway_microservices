from rest_framework import views
from rest_framework.response import Response
import requests
from rest_framework.generics import GenericAPIView

from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def api_handler(request, service_name, endpoint):
    # Route the request to the appropriate microservice
    if service_name == 'service1':
        base_url = 'http://127.0.0.1:8001/api/auth/'
    elif service_name == 'service2':
        base_url = 'http://127.0.0.1:8002/api/product/'
    else:   
        return JsonResponse({'error': 'Invalid service name'})
    
    if request.method == 'GET':
        # Make a GET request to the microservice
        response = requests.get(base_url + endpoint)
        return JsonResponse(response.json(), status=response.status_code)
    elif request.method == 'POST':
        # Make a POST request to the microservice
        data = request.body
        headers = {'Content-Type': 'application/json'}
        response = requests.post(base_url + endpoint, data=data, headers=headers)
        return JsonResponse(response.json(), status=response.status_code)


