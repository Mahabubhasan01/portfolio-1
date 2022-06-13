from django.urls import path
from . import views

urlpatterns = [
    path('service/',views.service,name='service'),
    path('skills/',views.skills,name='skills'),
    path('mskills/',views.mskills,name='mskills')
]
