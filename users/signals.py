from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
#from .models import Profile

# creating an entry in the 'Profile' database table when an entry is created in the 'User' database table
# the 'Profile' table is not currently used in this application, but might get utilized later
#@receiver(post_save, sender=User)
#def create_profile(sender, instance, created, **kwargs):
#    if created:
#        Profile.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_profile(sender, instance, **kwargs):
#    instance.profile.save()
