from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):

     # Validators
    def start_with_m(value):
        if value[0].lower() != 'm':
            raise serializers.ValidationError('Name should start with m')

    #name = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=200, validators=[start_with_m])
    
    class Meta:
        model = Employee
        fields = ['name', 'age', 'city']
        #read_only_fields = ['name', 'age']
        #extra_kwargs = {'name':{'read_only':True}}
  
    # Field level validation
    def validate_age(self, value):
        if value > 50:
            raise serializers.ValidationError('Age should be less than 50')
        return value

    # Object level validation
    def validate(self, data):
        name = data.get('name')
        city = data.get('city')

        if name.lower() == 'viru' and city.lower() != 'bhopal':
            raise serializers.ValidationError('City must be Bhopal')
        return data

   