from django.urls import path
from goals.views import GoalList, GoalDetailView, GoalCreate, GoalUpdate, GoalDelete
from goals.views import SessionList, ResourceList, MilestoneList
# Session
# Resource
# Milestone

urlpatterns = [
    path('goals/', GoalList.as_view(), name='goal-list'),
    path('goals/new/', GoalCreate.as_view(), name='goal-create'),
    path('goals/<int:pk>/', GoalDetailView.as_view(), name='goal-detail'),
    path('goals/<int:pk>/edit/', GoalUpdate.as_view(), name='goal-update'),
    path('goals/<int:pk>/delete/',GoalDelete.as_view(), name='goal-delete'),
    path('sessions/', SessionList.as_view()),
    path('resources/', ResourceList.as_view()),
    path('milestone/', MilestoneList.as_view())
]