from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver






class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    sity = models.ForeignKey('Country_cont',on_delete=models.CASCADE,blank=True ,null=True)
    phone = models.CharField(max_length=65)
    image = models.ImageField(upload_to='profiles/')
    def __str__(self):
        return str(self.user)
    





@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



class Country_cont(models.Model):
    sity = models.CharField(max_length=30,blank=True ,null=True)
    def __str__(self):
        return self.sity



    