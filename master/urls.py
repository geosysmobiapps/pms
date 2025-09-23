from django.urls import path
from .views import *


app_name = 'master'


urlpatterns = [
    # Dashboard
    path('', DashBoardView.as_view(), name= "dashboard"),
    # Projects
    path('project-list/', ProjectListView.as_view(), name= "project-list"),
    path('new-project/', ProjectCreateView.as_view(), name= "create-project"),
    path('project-details/', ProjectDetailView.as_view(), name= "project-details"),
    # Teams
    path('new-team/', TeamCreateView.as_view(), name= "create-team"),
    path('new-member/', MemberCreateView.as_view(), name= "create-member"),
    # Leads
    path('lead-list/', LeadListView.as_view(), name= "lead-list"),
    path('new-lead/', LeadCreateView.as_view(), name= "create-lead"),
    path('lead-details/', LeadDetailView.as_view(), name= "lead-details"),
    # Schedules
    path('new-schedule/', ScheduleCreateView.as_view(), name= "create-schedule"),
    path('schedule-list/', ScheduleListView.as_view(), name= "schedule-list"),
    # Quotations
    path('new-quotation/', QuotationCreateView.as_view(), name= "create-quotation"),
    path('quotation-list/', QuotationListView.as_view(), name= "quotation-list"),
    path('quotation-details/', QuotationDetailView.as_view(), name= "quotation-details"),
    # Customer
    path('customer-list/', CustomerListView.as_view(), name= "customer-list"),
    path('new-customer/', CustomerCreateView.as_view(), name= "create-customer"),
    # Reports
    path('project-report/', ProjectReportView.as_view(), name= "project-report"),
    # Settings
    path('profile-settings/', ProfileSettingsView.as_view(), name= "profile-settings"),
    path('support/', SupportView.as_view(), name= "support"),
]
