from django.shortcuts import render

from django.db.models import Q

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ImageUpload.models import Base64
from .serializers import Base64Serializer, UploadedImageSerializer

from django.shortcuts import redirect

import base64

from functools import reduce

from ImageUpload.models import UploadedImage

# from .crossCheck import fun

# Create your views here.

@api_view(['POST'])
def scanner(request):
    print(request.data)
    serializer = Base64Serializer(data=request.data)
    if serializer.is_valid():
        #print(serializer.data)
        base64_value = str(serializer.data['image'])
        imgdata = base64.b64decode(base64_value)
        filename = 'test.jpeg'
        with open(filename, 'wb') as f:
            f.write(imgdata)
        return redirect('/medinfo')
        # return redirect('/upload/image', image=imgdata)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)