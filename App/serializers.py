from rest_framework import serializers
from .models import Doctor, Patient

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Doctor
        fields = ('id', 'name', 'email', 'password')

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Patient
        fields = ('id', 'name', 'email', 'password', 'doctor_id', 'symptoms', 'illness')