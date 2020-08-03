from django.db import models
#imports the states codes to avoid human error typos
# from localflavor.us.models import USStateField

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class College(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    logo = models.TextField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    
    class Meta:
      order_with_respect_to = 'name'

    def __str__(self):
      return f"{self.name} located in {self.city}, {self.state}"




class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Product(models.Model):
    CATEGORY = (
             ('Active', 'Active'),
             ('InActive', 'InActive'),
             )
    majors = models.CharField(max_length=200, null=True)
    states = models.CharField(max_length=200, null=True)
    technology = models.CharField(max_length=200, null=True)
    financialaid = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

class Order(models.Model):
    STATUS = (
            ('Pending', 'Pending'),
            ('Out for delivery', 'Out for delivery'),
            ('Delivered', 'Delivered'),
            )

    user = models.ForeignKey(User, null=True, on_delete= models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices= STATUS)
    # tags = models.ManyToManyField(Tag)

class Major(models.Model):
    username = models.CharField(max_length=255, null=True)
    firstname = models.CharField(max_length=255, null=True)
    lastname = models.CharField(max_length=255, null=True)
    email = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
#imports the states codes to avoid human error typos
    state = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
      order_with_respect_to = 'lastname'

    def __str__(self):
      return f"{self.firstname} {self.lastname}, {self.email}"