from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from goals.models import Goal, Session, Milestone, Resource


# Create your views here.

# SignUp
def SignupView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('goal-list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Goals Views
class GoalList(ListView):
    model = Goal

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

class GoalDetailView(DetailView):
    model = Goal

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

class GoalCreate(CreateView):
    model = Goal
    fields = ['name', 'committed_effort','planned_completion_date','motivation']
    success_url = reverse_lazy('goal-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class GoalUpdate(UpdateView):
    model = Goal
    fields = ['name', 'committed_effort','planned_completion_date','motivation']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('goal-list')

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

class GoalDelete(DeleteView):
    model = Goal
    success_url = reverse_lazy('goal-list')

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

# Resource Views
class ResourceList(ListView):
    model = Resource

    def get_queryset(self):
        return Resource.objects.filter(user=self.request.user)

class ResourceDetailView(DetailView):
    model = Resource

    def get_queryset(self):
        return Resource.objects.filter(user=self.request.user)

class ResourceUpdate(UpdateView):
    model = Resource
    fields = ['name','location','description','priority','level']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('resource-list')

    def get_queryset(self):
        return Resource.objects.filter(user=self.request.user)
    
class ResourceCreate(CreateView):
    model = Resource
    fields = ['name','location','description','priority','level']
    success_url = reverse_lazy('resource-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ResourceDelete(DeleteView):
    model = Resource

    def get_queryset(self):
        return Resource.objects.filter(user=self.request.user)

# Session Views
class SessionList(ListView):
    model = Session

    def get_queryset(self):
        return Session.objects.filter(user=self.request.user)

class SessionDetailView(DetailView):
    model = Session

    def get_queryset(self):
        return Session.objects.filter(user=self.request.user)

class SessionCreate(CreateView):
    model = Session
    fields = ['date', 'duration','description','resource','goal']
    success_url = reverse_lazy('session-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class SessionUpdate(UpdateView):
    model = Session
    fields = ['date', 'duration','description','resource','goal']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('session-list')

    def get_queryset(self):
        return Session.objects.filter(user=self.request.user)

class SessionDelete(DeleteView):
    model = Session
    success_url = reverse_lazy('session-list')

    def get_queryset(self):
        return Session.objects.filter(user=self.request.user)

# Milestone Views
class MilestoneList(ListView):
    model = Milestone

    def get_queryset(self):
        return Milestone.objects.filter(user=self.request.user)

class MilestoneDetailView(DetailView):
    model = Milestone

    def get_queryset(self):
        return Milestone.objects.filter(user=self.request.user)

class MilestoneCreate(CreateView):
    model = Milestone
    fields = ['name','goal','planned_completion_date','actual_completion_date','reward','proof']
    success_url = reverse_lazy('milestone-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MilestoneUpdate(UpdateView):
    model = Milestone
    template_name_suffix = '_update_form'
    fields = ['name','goal','planned_completion_date','actual_completion_date','reward','proof']
    success_url = reverse_lazy('milestone-list')

    def get_queryset(self):
        return Milestone.objects.filter(user=self.request.user)

class MilestoneDelete(DeleteView):
    model = Milestone
    success_url = reverse_lazy('milestone-list')

    def get_queryset(self):
        return Milestone.objects.filter(user=self.request.user)