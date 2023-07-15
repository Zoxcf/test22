from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include ('app_advertisements.urls')),
    path('',include ('app_lesson_4.urls')),
    path('advertisment/',include("app_advertisment.urls")),
]
"""
mysite.com/p/
"""











