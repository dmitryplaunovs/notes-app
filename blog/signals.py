from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from .models import Post


# a signal to delete an image and audio, if a post is deleted
@receiver(post_delete, sender=Post) # the signal is triggered after a delete() function in the Post model
def submission_delete(sender, instance, **kwargs): # taking the model and the specific post (instance) as parameters
    instance.image.delete(save=False)
    instance.audio.delete(save=False)


# a signal to delete an image, if a post is updated with another image or the image is removed
@receiver(pre_save, sender=Post) # the signal is triggered before a save() function in the Post model
def updating_image_delete(sender, instance, **kwargs): # taking the model and the specific post (instance) as parameters
    if instance.pk:
        # running this code first
        try:
            old_image = Post.objects.get(pk=instance.pk).image
        # if the post doesn't exist, then return False
        except Post.DoesNotExist:
            return False
        # if there wasn't that exception
        else:
            new_image = instance.image
            if new_image:
                if old_image and old_image.url != new_image.url:
                    old_image.delete(save=False)
            else:
                old_image.delete(save=False)
    if not instance.pk:
        return False


# a signal to delete an audio file, if the post is updated with another audio file or the audio file is removed
@receiver(pre_save, sender=Post)
def updating_audio_delete(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_audio = Post.objects.get(pk=instance.pk).audio
        except Post.DoesNotExist:
            return False
        else:
            new_audio = instance.image
            if new_audio:
                if old_audio and old_audio.url != new_audio.url:
                    old_audio.delete(save=False)
            else:
                old_audio.delete(save=False)
    if not instance.pk:
        return False
