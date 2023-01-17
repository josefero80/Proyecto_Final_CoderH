from django.urls import path
from . import views

urlpatterns = [

    path('docu1/', views.docu1, name="docu1"),
    path('docu2/', views.docu2, name="docu2"),
    path('docu3/', views.docu3, name="docu3"),
    path('docu4/', views.docu4, name="docu4"),
    path('docu5/', views.docu5, name="docu5"),
]
