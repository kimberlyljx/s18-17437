# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    bio = models.CharField(max_length=200)
    picture = models.FileField(upload_to="images", default=settings.DEFAULT_PIC)
    content_type = models.CharField(max_length=50)
    user = models.OneToOneField(User, 
        related_name="profile",
        on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', symmetrical=False)

    def __unicode__(self):
        return 'id=' + str(self.id) + ',bio="' + self.bio + '"'

class Post(models.Model):
    text = models.CharField(max_length=200)
    creation_time = models.DateTimeField()
    user_profile = models.ForeignKey(Profile, 
        related_name="posts",
        on_delete=models.CASCADE)
    def __str__(self):
        return 'id=' + str(self.id) + ',text="' + self.text + '"'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
