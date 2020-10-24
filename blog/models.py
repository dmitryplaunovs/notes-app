from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


# defining a database table for posts
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) # recording the timestamp when a new entry is created
    author = models.ForeignKey(User, on_delete=models.CASCADE) # ForeignKey defines a "many-to-one relationship"
    image = models.ImageField(default='',upload_to='images',blank=True,null=True)
    audio = models.FileField(default='',upload_to='audio',blank=True,null=True)

    def __str__(self):
        return self.title

    # defining a URL for a new entry
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

# model names should be singular, for example, Post, because they represent a single object
# fields should be written in lowercase and with underscores
# The __str__ method defines a human-readable representation of the model in the Django admin site
# CASCADE defines that when a user is deleted, all his/her entries are deleted as well
