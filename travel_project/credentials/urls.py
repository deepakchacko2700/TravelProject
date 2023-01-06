from . import views
from django.urls import path
app_name = 'credentials'
urlpatterns=[
    path("registration", views.register, name="registration"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
]