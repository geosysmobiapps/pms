from django.urls import path
from .views import *


app_name = 'staff'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('activities/', ActivitiesView.as_view(), name='activities'),
    path('log-activity/', LogActivityView.as_view(), name='log_activity'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('all-projects/', AllProjectsView.as_view(), name='all_projects'),
    path('project/<int:project_id>/', ProjectDetailView.as_view(), name='project_detail'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
