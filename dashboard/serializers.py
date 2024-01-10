from rest_framework import serializers
from .models import DashBoard
from django.contrib.auth.models import Group, User


class DashBoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = DashBoard
        fields = ('id','balanca', 'create', 'update', 'active')





class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']        