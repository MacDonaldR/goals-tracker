from django.urls import path, include
from goals.views import SignupView
from goals.views import GoalList, GoalDetailView, GoalCreate, GoalUpdate, GoalDelete
from goals.views import ResourceList, ResourceDetailView, ResourceCreate, ResourceUpdate, ResourceDelete
from goals.views import SessionList, SessionDetailView, SessionCreate, SessionUpdate, SessionDelete
from goals.views import MilestoneList, MilestoneDetailView, MilestoneCreate, MilestoneUpdate, MilestoneDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Login
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignupView, name='signup'),
    # Goal CRUD
    path('goals/', login_required(GoalList.as_view()), name='goal-list'),
    path('goals/new/', login_required(GoalCreate.as_view()), name='goal-create'),
    path('goals/<int:pk>/', login_required(GoalDetailView.as_view()), name='goal-detail'),
    path('goals/<int:pk>/edit/', login_required(GoalUpdate.as_view()), name='goal-update'),
    path('goals/<int:pk>/delete/',login_required(GoalDelete.as_view()), name='goal-delete'),
    # Session CRUD
    path('sessions/', login_required(SessionList.as_view()), name='session-list'),
    path('sessions/new/', login_required(SessionCreate.as_view()), name='session-create'),
    path('sessions/<int:pk>/', login_required(SessionDetailView.as_view()), name='session-detail'),
    path('sessions/<int:pk>/edit/', login_required(SessionUpdate.as_view()), name='session-update'),
    path('sessions/<int:pk>/delete/', login_required(SessionDelete.as_view()), name='session-delete'),
    # Resource CRUD
    path('resources/', login_required(ResourceList.as_view()), name='resource-list'),
    path('resources/new/', login_required(ResourceCreate.as_view()), name='resource-create'),
    path('resources/<int:pk>/', login_required(ResourceDetailView.as_view()), name='resource-detail'),
    path('resources/<int:pk>/edit/', login_required(ResourceUpdate.as_view()), name='resource-update'),
    path('resources/<int:pk>/delete/', login_required(ResourceDelete.as_view()), name='resource-delete'),
    # Milestone CRUD
    path('milestones/', login_required(MilestoneList.as_view()), name='milestone-list'),
    path('milestones/new/', login_required(MilestoneCreate.as_view()), name='milestone-create'),
    path('milestones/<int:pk>/', login_required(MilestoneDetailView.as_view()), name='milestone-detail'),
    path('milestones/<int:pk>/edit/', login_required(MilestoneUpdate.as_view()), name='milestone-update'),
    path('milestones/<int:pk>/delete/', login_required(MilestoneDelete.as_view()), name='milestone-delete')
]