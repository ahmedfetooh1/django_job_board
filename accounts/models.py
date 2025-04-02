from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
# from .models import Profile

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name


# create new user -----> create new empty profile by signals
@receiver(post_save, sender=User) 
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    city = models.ForeignKey(City,related_name='user_city',on_delete=models.CASCADE,null=True,blank=True)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='profile/')

    def __str__(self):
        return str(self.user)

