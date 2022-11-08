from django.urls import path
from .views import LoginView, LogoutView

urlpatterns = [
    path('', LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path('logout/', LogoutView.as_view(template_name="adm_auth/bootstrap/login.html"),
         name="logout", ),
]
