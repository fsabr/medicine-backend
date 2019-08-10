from django.conf.urls import url
from django.urls import path
from .views import doc_list, single_doc, patient_list, single_patient, medicine_list,\
    med_info, doc_site, assign_prescription

urlpatterns = [
    path('doctor/', doc_list),
    path('doctor/<int:pk>', single_doc),
    path('patient/', patient_list),
    path('patient/<int:pk>', single_patient),
    path('medicine/', medicine_list),
    path('medinfo/<int:pk>', med_info),
    path('home/', doc_site),
    path('prescription/', assign_prescription)
]