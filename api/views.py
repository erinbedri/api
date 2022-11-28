from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Driver
from api.serializers import DriverSerializer


@api_view(['GET'])
def drivers(request):
    drivers_list = Driver.objects.all()
    serializer = DriverSerializer(drivers_list, many=True)

    return Response(serializer.data)
