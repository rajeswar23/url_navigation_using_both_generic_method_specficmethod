from app1.views import *
from django.urls import path
app_name="friends"
urlpatterns=[
    path('sudheer/',sudheer,name='sudheer'),
    path('nivas/',nivas,name='nivas'),
]