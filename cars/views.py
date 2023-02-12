from rest_framework.decorators import api_view # for every function we create we are going to put this decorator right above that function.
from rest_framework.response import Response


@api_view(['GET'])
def cars_list(request):

    return Response('ok')

