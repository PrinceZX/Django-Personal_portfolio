
from django.urls import path
from . import todoviews

app_name = 'Todo'

urlpatterns = [
    path('', todoviews.todohome, name='todohome'),

]