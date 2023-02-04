from django.urls import path
from accounts.views import login_user, Logout_user, Registrar_usuario

urlpatterns = [
   path('login-user/', login_user, name="login_user"),
   path('logout-user/', Logout_user.as_view(), name="logout_user"),
   path('register-user/', Registrar_usuario, name="register_user"),
     
]