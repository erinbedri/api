from django.db.models import Q
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Driver, Team
from api.serializers import DriverSerializer, TeamSerializer


@api_view(['GET', 'POST'])
def driver_list(request):
    if request.method == 'GET':
        drivers_list = Driver.objects.all()
        query_param = request.query_params.get('query', None)

        if query_param is not None:
            drivers_list = drivers_list.filter(
                Q(first_name__icontains=query_param) |
                Q(last_name__icontains=query_param) |
                Q(team__name__icontains=query_param) |
                Q(team__country__icontains=query_param)
            )

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


@api_view(['GET', 'POST'])
def team_list(request):
    if request.method == 'GET':
        teams_list = Team.objects.all()
        query_param = request.query_params.get('query', None)

        if query_param is not None:
            teams_list = teams_list.filter(
                Q(name__icontains=query_param) |
                Q(country__icontains=query_param)
            )

        serializer = TeamSerializer(teams_list, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        team_serializer = TeamSerializer(data=request.data)

        if team_serializer.is_valid():
            team_serializer.save()
            return JsonResponse(team_serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(team_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def team_detail(request, pk):
    try:
        team = Team.objects.get(pk=pk)
    except Team.DoesNotExist:
        return JsonResponse({'message': 'The team does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        team_serializer = TeamSerializer(team)
        return Response(team_serializer.data)

    if request.method == 'PUT':
        team_serializer = TeamSerializer(team, data=request.data)

        if team_serializer.is_valid():
            team_serializer.save()
            return JsonResponse(team_serializer.data)

        return JsonResponse(team_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        team.delete()
        return JsonResponse({'message': 'Team was successfully deleted'}, status=status.HTTP_204_NO_CONTENT)