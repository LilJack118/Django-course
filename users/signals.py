from django.db.models.signals import post_save, post_delete #django signals
from django.contrib.auth.models import User
from .models import Profile

#function that create new profile after new user registration
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email = user.email,
            name=user.first_name,
        )

#delete user after deleting profile
def deleteUser(sender, instance, **kwargs): 
    user = instance.user
    user.delete()
 
post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)