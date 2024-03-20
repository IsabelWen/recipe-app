from django.shortcuts import render
from .models import User

# Create your views here.
def profile(request):
    user = User.objects.first()  # Retrieve the first user
    context = {'user': user}
    return render(request, 'users/users_profile.html', context)