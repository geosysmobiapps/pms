from django.shortcuts import render
from django.views import View
from django.shortcuts import render


''' ___ Dashboard View ___ '''


class DashBoardView(View):
    template_name = "master/dashboard.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

''' ___ Project Management ___ '''


class ProjectListView(View):
    template_name = "master/project_list.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ProjectCreateView(View):
    template_name = "master/create_project.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ProjectDetailView(View):
    template_name = "master/project_details.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


''' ___ Department / Staff ___ '''

class TeamCreateView(View):
    template_name = "master/create_team.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class MemberCreateView(View):
    template_name = "master/create_member.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


''' ___ Lead Management ___ '''

class LeadListView(View):
    template_name = "master/lead_list.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class LeadCreateView(View):
    template_name = "master/create_lead.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

class LeadDetailView(View):
    template_name = "master/lead_details.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


''' ___ Manage Schedules ___ '''

class ScheduleListView(View):
    template_name = "master/schedule_list.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ScheduleCreateView(View):
    template_name = "master/create_schedule.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


''' Quotations '''

class QuotationListView(View):
    template_name = "master/quotation_list.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class QuotationCreateView(View):
    template_name = "master/create_quotation.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class QuotationDetailView(View):
    template_name = "master/quotation_details.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


''' ___ Customers ___ '''

class CustomerListView(View):
    template_name = "master/customer_list.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class CustomerCreateView(View):
    template_name = "master/create_customer.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


''' ___ Reports ___ '''

class ProjectReportView(View):
    template_name = "master/project_report.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

''' ___ Settings ___'''


class ProfileSettingsView(View):
    template_name = "master/profile_settings.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

class SupportView(View):
    template_name = "master/support.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)