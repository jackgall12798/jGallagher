from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model) :

      name=models.CharField(max_length=100)
      brand=models.CharField(max_length=100)
      cost=models.FloatField()
      category=models.CharField(max_length=100)
      date_released=models.DateField()
      description=models.TextField()
      photo=models.ImageField()

def __str__(self) :

  return self.name

class Profile(models.Model) :
      user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
      full_name=models.CharField(max_length=100)
      dob=models.DateField(max_length=8)
      address=models.TextField()
      city=models.CharField(max_length=100)
      country=models.CharField(max_length=100)
      photo=models.ImageField()

def __str__(self) :

  return self.full_name

class Review(models.Model) :
     
      author=models.ForeignKey(User, on_delete=models.CASCADE)
      rating=models.IntegerField()
      review=models.TextField()
      date_submitted=models.DateTimeField(default=timezone.now)

def __str__(self) :

  return self.author
