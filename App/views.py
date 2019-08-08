from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Doctor, Patient, Medicine
from .serializers import DoctorSerializer, PatientSerializer, MedicineSerializer

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
    return Response(status=status.HTTP_404_NOT_FOUND)

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
    return Response(status=status.HTTP_404_NOT_FOUND)

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
    return Response(status=status.HTTP_404_NOT_FOUND)

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
    return Response(status=status.HTTP_404_NOT_FOUND)

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
    return Response(status=status.HTTP_404_NOT_FOUND)