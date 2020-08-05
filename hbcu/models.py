from django.db import models
#imports the states codes to avoid human error typos
# from localflavor.us.models import USStateField

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

User = get_user_model()

# Create your models here.
class College(models.Model):
    name = models.TextField(max_length=3000, default='')
    url = models.URLField(null=True, blank=True, default='')
    major = models.TextField( max_length=3000, default='')
    degree = models.TextField(max_length=3000, default='')
    city = models.TextField(max_length=3000, default='')
    state = models.TextField(max_length=3000, default='')
    technology = models.TextField(max_length=500, default='')
    financial_aid = models.TextField(max_length=3000, default='')
    logo = models.TextField(null=True, blank=True)
    campus_image = models.TextField(null=True, blank=True)
    virtual_tour = models.TextField(max_length=3000, default='')
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


class Product(models.Model):
    CATEGORY = (
             ('Active', 'Active'),
             ('InActive', 'InActive'),
             )
    majors = models.TextField(max_length=200, null=True)
    states = models.TextField(max_length=200, null=True)
    technology = models.TextField(max_length=200, null=True)
    financialaid = models.TextField(max_length=200, null=True)
    category = models.TextField(max_length=200, null=True, choices=CATEGORY)
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
    status = models.TextField(max_length=200, null=True, choices= STATUS)
    # tags = models.ManyToManyField(Tag)

class Major(models.Model):
    username = models.TextField(max_length=255, null=True)
    firstname = models.TextField(max_length=255, null=True)
    lastname = models.TextField(max_length=255, null=True)
    email = models.TextField(null=True, blank=True)
    city = models.TextField(max_length=255, null=True, blank=True)
#imports the states codes to avoid human error typos
    state = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
      order_with_respect_to = 'lastname'

    def __str__(self):
      return f"{self.firstname} {self.lastname}, {self.email}"