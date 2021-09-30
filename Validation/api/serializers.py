from rest_framework import serializers
from .models import Employee

# Validators
def start_with_m(value):
    if value[0].lower() != 'm':
        raise serializers.ValidationError('Name should start with m')

class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200, validators=[start_with_m])
    age = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return  Employee.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    # Field level validation
    def validate_age(self, value):
        if value > 50:
            raise serializers.ValidationError('Age should be less than 50')
        return value

    # Object level validation
    def validate(self, data):
        name = data.get('name')
        city = data.get('city')

        if name.lower() == 'manoj' and city.lower() != 'bhopal':
            raise serializers.ValidationError('City must be Bhopal')
        return data