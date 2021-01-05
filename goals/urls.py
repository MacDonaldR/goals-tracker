from django.urls import path
from goals.views import GoalList, GoalDetailView, GoalCreate, GoalUpdate, GoalDelete
from goals.views import ResourceList, ResourceDetailView, ResourceCreate, ResourceUpdate, ResourceDelete
from goals.views import SessionList, SessionDetailView, SessionCreate, SessionUpdate, SessionDelete
from goals.views import MilestoneList, MilestoneDetailView, MilestoneCreate, MilestoneUpdate, MilestoneDelete

urlpatterns = [
    # Goal CRUD
    path('goals/', GoalList.as_view(), name='goal-list'),
    path('goals/new/', GoalCreate.as_view(), name='goal-create'),
    path('goals/<int:pk>/', GoalDetailView.as_view(), name='goal-detail'),
    path('goals/<int:pk>/edit/', GoalUpdate.as_view(), name='goal-update'),
    path('goals/<int:pk>/delete/',GoalDelete.as_view(), name='goal-delete'),
    # Session CRUD
    path('sessions/', SessionList.as_view(), name='session-list'),
    path('sessions/new/', SessionCreate.as_view(), name='session-create'),
    path('sessions/<int:pk>/', SessionDetailView.as_view(), name='session-detail'),
    path('sessions/<int:pk>/edit/', SessionUpdate.as_view(), name='session-update'),
    path('sessions/<int:pk>/delete/', SessionDelete.as_view(), name='session-delete'),
    # Resource CRUD
    path('resources/', ResourceList.as_view(), name='resource-list'),
    path('resources/new/', ResourceCreate.as_view(), name='resource-create'),
    path('resources/<int:pk>/', ResourceDetailView.as_view(), name='resource-detail'),
    path('resources/<int:pk>/edit/', ResourceUpdate.as_view(), name='resource-update'),
    path('resources/<int:pk>/delete/', ResourceDelete.as_view(), name='resource-delete'),
    # Milestone CRUD
    path('milestones/', MilestoneList.as_view(), name='milestone-list'),
    path('milestones/new/', MilestoneCreate.as_view(), name='milestone-create'),
    path('milestones/<int:pk>/', MilestoneDetailView.as_view(), name='milestone-detail'),
    path('milestones/<int:pk>/edit/', MilestoneUpdate.as_view(), name='milestone-update'),
    path('milestones/<int:pk>/delete/', MilestoneDelete.as_view(), name='milestone-delete')
]