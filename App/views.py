from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Doctor, Patient, Medicine
from .serializers import DoctorSerializer, PatientSerializer, MedicineSerializer

from PIL import Image
import pytesseract

import os
import re

from ImageUpload.models import UploadedImage

# Create your views here.

@api_view(['GET', 'POST'])
def doc_list(request):
    if request.method == 'GET':
        all_docs            = Doctor.objects.all()
        all_serialized_docs = DoctorSerializer(all_docs, many=True)
        return Response(all_serialized_docs.data)
    elif request.method == 'POST':
        print(request.data)
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET', 'DELETE'])
def single_doc(request, pk):
    try:
        sampleItem = Doctor.objects.get(pk=pk)
    except Doctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DoctorSerializer(sampleItem)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        sampleItem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET', 'POST'])
def patient_list(request):
    if request.method == 'GET':
        all_docs            = Patient.objects.all()
        all_serialized_docs = PatientSerializer(all_docs, many=True)
        return Response(all_serialized_docs.data)
    elif request.method == 'POST':
        print(request.data)
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET', 'DELETE'])
def single_patient(request, pk):
    try:
        sampleItem = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PatientSerializer(sampleItem)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        sampleItem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET', 'POST'])
def medicine_list(request):
    if request.method == 'GET':
        all_docs            = Medicine.objects.all()
        all_serialized_docs = MedicineSerializer(all_docs, many=True)
        return Response(all_serialized_docs.data)
    elif request.method == 'POST':
        print(request.data)
        serializer = MedicineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def med_info(request, pk):
    if request.method == 'GET':
        try:
            img = UploadedImage.objects.get(pk=pk)
        except UploadedImage.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        image_name = str(img.image)
        text = pytesseract.image_to_string(os.path.join('../uploaded_media', image_name))
        list_of_words = re.split(' |, |\*|\n', text)
        filter_meds = Medicine.objects.none()
        print(list_of_words)
        for word in list_of_words:
            if len(word) > 1:
                filter_meds = filter_meds.union(Medicine.objects.filter(name__icontains=word))
        print(filter_meds)
        if filter_meds.exists():
            serial_filter_meds = MedicineSerializer(filter_meds, many=True)
            return Response(serial_filter_meds.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

def doc_site(request):
    return render(request, 'Doctor_website/index.html')

def assign_prescription(request):
    return render(request, 'Doctor_website/single-blog.html')