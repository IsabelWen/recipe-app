from django.shortcuts import render
from .models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def profile(request):
    user = User.objects.first()  # Retrieve the first user
    context = {'user': user}
    return render(request, 'users/users_profile.html', context)