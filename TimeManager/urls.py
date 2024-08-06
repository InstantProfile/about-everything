from django.urls import path
from .views import add_work_entry, WorkEntryListView
from . import views
urlpatterns = [
    path('add/', add_work_entry, name='add_work_entry'),
    path('', views.index, name='main_timemanager'),
    path('list/', WorkEntryListView.as_view(), name='work_entry_list'),
]
