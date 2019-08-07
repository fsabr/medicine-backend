from django.conf.urls import url
from django.urls import path
from .views import doc_list, single_doc, patient_list, single_patient

urlpatterns = [
    path('doctor/', doc_list),
    path('doctor/<int:pk>', single_doc),
    path('patient/', patient_list),
    path('patient/<int:pk>', single_patient)
]