from rest_framework import serializers

start = ' rwa1 cwb1 bwc1 qwd1 kwe1 bwf1 cwg1 rwh1 pwa2 pwb2 pwc2 pwd2 pwe2 pwf2 pwg2 pwh2 pba7 pbb7 pbc7 pbd7 pbe7 pbf7 pbg7 pbh7 rba8 cbb8 qbd8 kbe8 bbf8 cbg8 rbh8'

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