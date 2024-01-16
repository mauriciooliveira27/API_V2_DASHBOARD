from rest_framework import serializers
from .models import DashBoard
from django.contrib.auth.models import Group, User


class DashBoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = DashBoard
        fields = ('balanca', 'create')




