from rest_framework import serializers
from .models import Doctor, Patient, Medicine

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Doctor
        fields = ('id', 'name', 'email', 'password')

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Patient
        fields = ('id', 'name', 'email', 'password', 'doctor_id', 'symptoms', 'illness')

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Medicine
        fields = ('id', 'name', 'tabletd', 'time','days') 

# class MedicineTakeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model  = MedicineTake
#         fields = ('id', 'total', 'taken')
