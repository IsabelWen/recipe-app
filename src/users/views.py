from django.shortcuts import render
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

# Create your views here.
class profile(LoginRequiredMixin, DetailView):
    model: CustomUser
    template_name = 'users/users_profile.html'
    context_object_name = 'current_user'
    def get_object(self, queryset=None):
        return CustomUser.objects.get(user=self.request.user)