from rest_framework import serializers
from .models import Room,start


class RoomSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    code = serializers.CharField( default="",max_length=10)
    pieces = serializers.CharField( max_length=len(start),default=start)
    def create(self,validated_data):
        return Room.objects.create(**validated_data)
    def update(self,instance,validated_data):
        instance.code = validated_data.get('code',instance.code)
        #lembrar de arrumar o pieces
        instance.pieces = validated_data.get('pieces',instance.pieces)
        instance.save()
        return instance