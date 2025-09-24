from django.shortcuts import render, redirect
from django.views import View

# Create your views here.


class LoginView(View):
    template_name = "accounts/login.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        # Get the selected account type from the form
        account_type = request.POST.get('account_type')
        
        # Redirect based on account type
        if account_type == 'admin':
            return redirect("master:dashboard")
        elif account_type == 'staff':
            return redirect("staff:dashboard")
        else:
            # If no account type selected, redirect back to login with error
            return render(request, self.template_name, {
                'auth_error': 'Please select an account type'
            })