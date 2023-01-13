from django.urls import path
from blog.views import docu1, docu2, docu3

urlpatterns = [
    path('docu1/', docu1, name="docu1"),
    path('docu2/', docu2, name="docu2"),
    path('docu3/', docu3, name="docu3"),
]
