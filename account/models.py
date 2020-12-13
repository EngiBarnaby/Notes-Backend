from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db.models.signals import post_save

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    user_picture = models.ImageField(default="profile2.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username



def custom_user_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='Simple Users')
        instance.groups.add(group)
        CustomUser.objects.create(
            user=instance,
            username=instance.username,
            email=instance.email
        )
        print('Profile created!')


post_save.connect(custom_user_profile, sender=User)
