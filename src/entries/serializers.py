from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Entry

class EntrySerializer(ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    class Meta:
        model = Entry

        fields = ['id', 'item', 'cost', 'timestamp', 'owner']

class UserSerializer(ModelSerializer):
    entry = serializers.PrimaryKeyRelatedField(many=True, queryset=Entry.objects.all())
    class Meta:
        model = User

        fields = ['id', 'email', 'is_active', 'is_staff', 'is_admin', 'timestamp', 'entry']

