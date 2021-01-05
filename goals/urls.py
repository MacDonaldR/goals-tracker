from django.urls import path
from goals.views import GoalList, SessionList, ResourceList, MilestoneList

urlpatterns = [
    path('goals/', GoalList.as_view()),
    path('sessions/', SessionList.as_view()),
    path('resources/', ResourceList.as_view()),
    path('milestone/', MilestoneList.as_view())
]