from django.db import models

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