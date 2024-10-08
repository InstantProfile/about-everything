from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.main_menu, name='main'),
    path('timemanager/', include('TimeManager.urls')),
    path('accounts/', include('accounts.urls')),
]
