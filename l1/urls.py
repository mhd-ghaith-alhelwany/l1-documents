from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("docs.urls"), name="docs"),
    path('admin/', admin.site.urls),
]
