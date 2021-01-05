from django.shortcuts import render
from django.views.generic import ListView
from goals.models import Goal, Session, Milestone, Resource

# Create your views here.

# Goals Views
class GoalList(ListView):
    model = Goal

# Session Views
class SessionList(ListView):
    model = Session

# Milestone Views
class MilestoneList(ListView):
    model = Milestone

# Resource Views
class ResourceList(ListView):
    model = Resource