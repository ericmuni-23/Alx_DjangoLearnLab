from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect

class Member(UserPassesTestMixin, TemplateView):
    template_name = 'member_template.html'

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.userprofile.role == 'Member'

    def handle_no_permission(self):
        return redirect('home')  # Redirect to home page if user doesn't have permission
