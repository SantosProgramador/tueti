from rest_framework import serializers

from tueti.models import Tuet, TuetiUser


class TuetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuet
        fields = ('text', 'author', 'created')


class TuetiUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TuetiUser
        fields = ('user.name', 'user.email')