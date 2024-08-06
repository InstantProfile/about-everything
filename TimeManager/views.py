from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import WorkEntryForm
from .models import WorkEntry


def add_work_entry(request):
    if request.method == 'POST':
        form = WorkEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = WorkEntryForm()
    return render(request, 'TimeManager/add_work_entry.html', {'form': form})


class WorkEntryListView(ListView):
    model = WorkEntry
    template_name = 'TimeManager/work_entry_list.html'
    context_object_name = 'work_entries'


def index(request):
    menu = [
        {'name': 'Домой', 'url': 'main'},
        {'name': 'Добавить', 'url': 'add_work_entry'},
        {'name': 'Просмотреть', 'url': 'work_entry_list'}
    ]
    return render(request, 'TimeManager/main_time_manager.html', {'menu': menu})
