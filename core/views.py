from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response


@api_view(['GET'])
def home(request):
    raise NotFound('test')
    return Response({'message': 'Hello, World!'})
