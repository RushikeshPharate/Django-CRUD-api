from rest_framework import serializers
from .models import Student



class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    city=serializers.CharField(max_length=20)
    mob=serializers.IntegerField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.city=validated_data.get('city',instance.city)
        instance.mob=validated_data.get('mob',instance.mob)
        instance.save()
        return instance