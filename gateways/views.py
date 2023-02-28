import requests
from rest_framework.decorators import csrf_exempt
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView


@csrf_exempt
def api_handler(request, service_name, endpoint):
    # Route the request to the appropriate microservice
    if service_name == 'service1':
        base_url = 'http://127.0.0.1:8001/api/auth/'
    elif service_name == 'service2':
        base_url = 'http://127.0.0.1:8002/api/product/'
    else:
        return Response({'error': 'Invalid service name'}, status=HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        # Make a GET request to the microservice
        response = requests.get(base_url + endpoint)
        return Response(response.json(), status=response.status_code)
    
    elif request.method == 'POST':
        # Make a POST request to the microservice
        data = request.data
        headers = {'Content-Type': 'application/json'}
        response = requests.post(base_url + endpoint, data=data, headers=headers)
        return Response(response.json(), status=response.status_code)
    
    elif request.method == 'PUT':
        # Make a PUT request to the microservice
        data = request.data
        headers = {'Content-Type': 'application/json'}
        response = requests.put(base_url + endpoint, data=data, headers=headers)
        return Response(response.json(), status=response.status_code)
    
    elif request.method == 'DELETE':
        # Make a DELETE request to the microservice
        response = requests.delete(base_url + endpoint)
        return Response(status=response.status_code)
    
    else:
        return Response({'error': 'Unsupported method'}, status=HTTP_400_BAD_REQUEST)



