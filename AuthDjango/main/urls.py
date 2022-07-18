from django.urls import path
from main import views

urlpatterns =[
    path('secure/',views.some,name='some'),
    path('',views.index)
]