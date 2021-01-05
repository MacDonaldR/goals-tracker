from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from goals.models import Goal, Session, Milestone, Resource


# Create your views here.

# Goals Views
class GoalList(ListView):
    model = Goal

class GoalDetailView(DetailView):
    model = Goal

class GoalCreate(CreateView):
    model = Goal
    fields = ['name', 'committed_effort','planned_completion_date','motivation']
    success_url = reverse_lazy('goal-list')

class GoalUpdate(UpdateView):
    model = Goal
    fields = ['name', 'committed_effort','planned_completion_date','motivation']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('goal-list')

class GoalDelete(DeleteView):
    model = Goal
    success_url = reverse_lazy('goal-list')

# Resource Views
class ResourceList(ListView):
    model = Resource

class ResourceDetailView(DetailView):
    model = Resource

class ResourceUpdate(UpdateView):
    model = Resource
    fields = ['name','location','description','priority','level']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('resource-list')

class ResourceCreate(CreateView):
    model = Resource
    fields = ['name','location','description','priority','level']
    success_url = reverse_lazy('resource-list')

class ResourceDelete(DeleteView):
    model = Resource

# Session Views
class SessionList(ListView):
    model = Session

class SessionDetailView(DetailView):
    model = Session

class SessionCreate(CreateView):
    model = Session
    fields = ['date', 'duration','description','resource','goal']
    success_url = reverse_lazy('session-list')

class SessionUpdate(UpdateView):
    model = Session
    fields = ['date', 'duration','description','resource','goal']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('session-list')

class SessionDelete(DeleteView):
    model = Session
    success_url = reverse_lazy('session-list')

# Milestone Views
class MilestoneList(ListView):
    model = Milestone

class MilestoneDetailView(DetailView):
    model = Milestone

class MilestoneCreate(CreateView):
    model = Milestone
    fields = ['name','goal','planned_completion_date','actual_completion_date','reward','proof']
    success_url = reverse_lazy('milestone-list')

class MilestoneUpdate(UpdateView):
    model = Milestone
    template_name_suffix = '_update_form'
    fields = ['name','goal','planned_completion_date','actual_completion_date','reward','proof']
    success_url = reverse_lazy('milestone-list')

class MilestoneDelete(DeleteView):
    model = Milestone
    success_url = reverse_lazy('milestone-list')