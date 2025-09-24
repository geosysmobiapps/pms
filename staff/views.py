from django.shortcuts import render
from django.views import View



# Create your views here.
class DashboardView(View):
    template_name = "staff/staff_dashboard.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class ScheduleView(View):
    template_name = "staff/schedule.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class LogScheduleView(View):
    template_name = "staff/log_schedule.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        # Handle form submission here
        # Process the activity and expense data
        return render(request, self.template_name)
    
class ProjectsView(View):
    template_name = "staff/projects.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class AllProjectsView(View):
    template_name = "staff/all_projects.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class ProjectDetailView(View):
    template_name = "staff/project_detail.html"

    def get(self, request, project_id, *args, **kwargs):
        return render(request, self.template_name, {'project_id': project_id})

class ProfileView(View):
    template_name = "staff/profile.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)