from rest_framework import serializers

from api.models import Driver, Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'country']


class DriverSerializer(serializers.ModelSerializer):
    team = TeamSerializer()

    class Meta:
        model = Driver
        fields = ['id', 'first_name', 'last_name', 'team']
