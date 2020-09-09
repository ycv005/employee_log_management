from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import GlobalUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    my_contacts = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='globaluser-detail'
    )

    class Meta:
        model = get_user_model()
        fields = ['id', 'url', 'name', 'email', 'phone_number', 'my_contacts']


class GlobalUserSerializer(serializers.HyperlinkedModelSerializer):
    names = serializers.StringRelatedField(many=True)

    class Meta:
        model = GlobalUser
        fields = ['id', 'url', 'phone_number', 'spam', 'names']
