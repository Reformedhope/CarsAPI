from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view # for every function we create we are going to put this decorator right above that function.
from rest_framework.response import Response
from rest_framework import status
from.Serializers import CarSerializer
from.models import Car

@api_view(['GET', 'POST'])
def cars_list(request):

    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        # serializer.is_valid() == True # This is one way to do it
        serializer.is_valid(raise_exception=True) #This is another way to complete the above
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # else:
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT'])
def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'GET':
        serializer = CarSerializer(car)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CarSerializer(car, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

   
