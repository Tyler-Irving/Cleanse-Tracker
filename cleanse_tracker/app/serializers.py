from django.contrib.auth.models import User
from .models import Cleanse, CleanseEntry, Restriction
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class CleanseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cleanse
        fields = ['name', 'description', 'start_date', 'end_date']

class CleanseEntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CleanseEntry
        fields = ['user', 'cleanse', 'restriction', 'is_completed']

class RestrictionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restriction
        fields = ['name', 'description']