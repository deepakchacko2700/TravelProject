from . import views
from django.urls import path, include
app_name = 'travelapp'

urlpatterns = [
    path('', views.demo, name="demo"),
    path('about', views.about, name="about")
    # path('add/', views.add, name='add'),
    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact')
]
