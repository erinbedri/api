from django.db.models import Q
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Driver
from api.serializers import DriverSerializer


@api_view(['GET', 'POST'])
def driver_list(request):
    if request.method == 'GET':
        drivers_list = Driver.objects.all()
        query_param = request.query_params.get('query', None)

        if query_param is not None:
            drivers_list = drivers_list.filter(
                Q(first_name__icontains=query_param) |
                Q(last_name__icontains=query_param))

        serializer = DriverSerializer(drivers_list, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        driver_serializer = DriverSerializer(data=request.data)

        if driver_serializer.is_valid():
            driver_serializer.save()
            return JsonResponse(driver_serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(driver_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def driver_detail(request, pk):
    try:
        driver = Driver.objects.get(pk=pk)
    except Driver.DoesNotExist:
        return JsonResponse({'message': 'The driver does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        driver_serializer = DriverSerializer(driver)
        return Response(driver_serializer.data)

    if request.method == 'PUT':
        driver_serializer = DriverSerializer(driver, data=request.data)

        if driver_serializer.is_valid():
            driver_serializer.save()
            return JsonResponse(driver_serializer.data)

        return JsonResponse(driver_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        driver.delete()
        return JsonResponse({'message': 'Driver was successfully deleted'}, status=status.HTTP_204_NO_CONTENT)
