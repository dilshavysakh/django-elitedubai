from django.db import models

# Create your models here.
class Fleet(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField()
    passengers=models.IntegerField(default=0)
    luggage=models.IntegerField(default=0)
    img=models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    fullname=models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone=models.IntegerField(default=0)
    msg=models.TextField()
    
    
    def __str__(self):
        return self.fullname