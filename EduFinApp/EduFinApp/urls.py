from django.contrib import admin
from django.urls import path
from core.views import testing_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('testing', testing_view, name='testing'),
]