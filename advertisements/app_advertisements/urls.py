from django.urls import path
from .views import index, test_33


urlpatterns = [
    path('', index),
    path('test33/',test_33)
]

"""
https://mysite.com/test33/
"""
