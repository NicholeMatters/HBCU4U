from django.db import models
#imports the states codes to avoid human error typos
# from localflavor.us.models import USStateField

# Create your models here.
class College(models.Model):
    name = models.CharField(max_length=3000, default='')
    url = models.URLField(null=True, blank=True, default='')
    major = models.CharField( max_length=3000, default='')
    degree = models.CharField(max_length=3000, default='')
    city = models.CharField(max_length=3000, default='')
    state = models.CharField(max_length=3000, default='')
    technology = models.CharField(max_length=500, default='')
    financial_aid = models.CharField(max_length=3000, default='')
    logo = models.TextField(null=True, blank=True)
    campus_image = models.TextField(null=True, blank=True)
    virtual_tour = models.CharField(max_length=3000, default='')
    
    
    class Meta:
      order_with_respect_to = 'name'

    def __str__(self):
      return f"{self.name} located in {self.city}, {self.state}"

#Creates a user and creates a profile in admin
class User(models.Model):
    username = models.CharField(max_length=3000, null=True)
    firstname = models.CharField(max_length=3000, null=True)
    lastname = models.CharField(max_length=3000, null=True)
    email = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=3000, null=True, blank=True)
#imports the states codes to avoid human error typos
    state = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
      order_with_respect_to = 'lastname'

    def __str__(self):
      return f"{self.firstname} {self.lastname}, {self.email}"


class UserProfile(models.Model):  
    user = models.OneToOneField(User, unique=True, on_delete= models.CASCADE)
#Remember to Add a widget for multiple gender options
    gender = models.CharField(max_length=140)  
    profile_picture = models.ImageField(upload_to='thumbpath', blank=True)

    def __unicode__(self):
        return u'Profile of user: %s' % self.user.username

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
    username = models.CharField(max_length=3000, null=True)
    firstname = models.CharField(max_length=3000, null=True)
    lastname = models.CharField(max_length=3000, null=True)
    email = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=3000, null=True, blank=True)
#imports the states codes to avoid human error typos
    state = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
      order_with_respect_to = 'lastname'

    def __str__(self):
      return f"{self.firstname} {self.lastname}, {self.email}"