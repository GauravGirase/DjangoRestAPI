from rest_framework import serializers
from .models import School, Student


# Serializers define the API representation.
class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = ['name', 'city', 'pin_code', 'email', 'password']

    def create(self, validated_data):

        validated_data['created_by'] = self.context['request'].user
        return School.objects.create(**validated_data)

class StudentSerializer(serializers.ModelSerializer):
    school = serializers.CharField(source='school.name')

    class Meta:
        model = Student
        fields = ['name', 'username', 'password', 'grade', 'school']

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return Student.objects.create(**validated_data)
