from django.db import models

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


User = get_user_model()

class Major(models.Model):
    name = models.CharField(max_length=3000, default='')

    def __str__(self):
      return self.name

class Degree(models.Model):
    name = models.CharField(max_length=3000, default='')

    def __str__(self):
      return self.name

class State(models.Model):
    name = models.CharField(max_length=3000, default=False)

    def __str__(self):
      return self.name

# Create your models here.
class College(models.Model):
    name = models.TextField(max_length=3000, default='')
    url = models.URLField(null=True, blank=True, default='')
    major = models.ManyToManyField(Major)
    degree = models.ManyToManyField(Degree)
    city = models.TextField(max_length=3000, default='')
    state = models.ManyToManyField(State)
    technology = models.TextField(max_length=500, default='')
    financial_aid = models.TextField(max_length=3000, default='')
    logo = models.TextField(null=True, blank=True)
    campus_image = models.TextField(null=True, blank=True)
    virtual_tour = models.BooleanField(default=False)
    history = models.TextField( max_length=3000, default='')
    
    class Meta:
      order_with_respect_to = 'name'

    def __str__(self):
      return f"{self.name} located in {self.city}, {self.state}"


class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.TextField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()



class HBCUgrads(models.Model):
    name = models.TextField(max_length=3000, default='')
    url = models.URLField(null=True, blank=True, default='')
    career = models.TextField( max_length=3000, default='')
    date_born = models.TextField(max_length=3000, default='')
    date_died = models.TextField(max_length=3000, default='')
    school = models.TextField(max_length=3000, default='')
    image = models.TextField(null=True, blank=True)
    history = models.TextField( max_length=3000, default='')
    
    class Meta:
      order_with_respect_to = 'name'

    def __str__(self):
      return f"{self.name} attended {self.school}"