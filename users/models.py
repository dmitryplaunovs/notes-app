from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# defining a database table for additional user information (e.g. profile images)
# the 'Profile' table is not currently used in this application, but might get utilized later
#class Profile(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    # if a user doesn't upload an image, then use the default one
#    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
#
#    # defining a human-readable name for each object in this class (each entry in the table)
#    def __str__(self):
#        return f'{self.user.username} Profile'
#
#    def save(self, *args, **kwargs):
#        super().save(*args, **kwargs)
#
#        img = Image.open(self.image.path)
#        # resizing the image to 300x300
#        if img.height > 300 or img.width > 300:
#            output_size = (300, 300)
#            img.thumbnail(output_size)
#            img.save(self.image.path)
