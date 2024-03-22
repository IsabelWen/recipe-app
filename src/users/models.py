from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=120)
    pic = models.ImageField(upload_to='users', default='no_picture.jpg')
    bio = models.TextField(default="No bio ...")

    def __str__(self):
        return f"{self.name}"
    
    # creates a user object with the same username if it doesn't exist
    def save(self, *args, **kwargs):
        if not self.user:
            user = User.objects.get_or_create(
                username=self.username,
            )
            self.user = user
        super().save(*args, **kwargs)