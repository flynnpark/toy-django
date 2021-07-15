from rest_framework import serializers


class HomeSerializer(serializers.Serializer):
    message = serializers.CharField(read_only=True)
