from django.urls import path
from blog.views import docu1, docu2, docu3, docu4, docu5

urlpatterns = [
    path('docu1/', docu1, name="docu1"),
    path('docu2/', docu2, name="docu2"),
    path('docu3/', docu3, name="docu3"),
    path('docu4/', docu4, name="docu4"),
    path('docu5/', docu5, name="docu5"),
]
