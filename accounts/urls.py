from django.urls import path
from accounts.views import login_user, Logout_user, Registrar_usuario, ProfileUpdateView, UserDetailView

urlpatterns = [
   path('login-user/', login_user, name="login_user"),
   path('logout-user/', Logout_user.as_view(), name="logout_user"),
   path('register-user/', Registrar_usuario, name="register_user"),
   path('editar-user/', ProfileUpdateView.as_view(), name="edit_user"),
   path('profile/<int:pk>', UserDetailView.as_view(), name="profile_user"),
     
]