from django.urls import path
from . import views

# Define the app name para poder acceder a las urls de este archivo desde cualquier template con 
# la sintaxis 'app_name:url_name'
app_name = "register"

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.perfil_view, name='perfil'),
]