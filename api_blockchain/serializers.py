from rest_framework import serializers
from .models import Operation, Blockchain


class OperationSerializer(serializers.Serializer):
    def create(self, validated_data):
        return Comment(**validated_data)

    src_account = serializers.CharField()
    des_account = serializers.CharField()
    amount = serializers.IntegerField()

    def update(self, instance, validated_data):
        pass


