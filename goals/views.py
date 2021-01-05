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

# Session Views
class SessionList(ListView):
    model = Session

class SessionDetailView(DetailView):
    model = Session

# Milestone Views
class MilestoneList(ListView):
    model = Milestone

class MilestoneDetailView(DetailView):
    model = Milestone

# Resource Views
class ResourceList(ListView):
    model = Resource

class ResourceDetailView(DetailView):
    model = Resource