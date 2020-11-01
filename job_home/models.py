from django.db import models
from django.utils.text import slugify
import random
from accounts.models import Country_cont
from django.http import request
from django.contrib.auth.models import User





class Added_JOBS(models.Model):
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    JobNature  = (
    ('Part-time','Part-time'),
    ('Full-time','Full-time'))
    City = models.ForeignKey('accounts.Country_cont',on_delete=models.CASCADE,blank=True ,null=True)
    category = models.ForeignKey("Cartegory", on_delete=models.CASCADE,default=1) 
    Job_Nature = models.CharField(max_length=120,choices=JobNature,default=1)
    title = models.CharField(max_length=120)
    discription= models.TextField(max_length=3500)
    Published_on= models.DateTimeField(auto_now=True)
    Vacancy= models.IntegerField()
    imag = models.ImageField(upload_to='imags/',default='logo_defuel.png')
    Salary= models.IntegerField()
    slug = models.SlugField(blank=True ,null=True)

    def save(self,*args, **kwargs):
        i = random.randrange(0,12)
        self.slug = slugify(self.title)+'-'+str(i)
        super(Added_JOBS,self).save(*args, **kwargs)

        


    def __str__(self):
        return self.title


    class Meta:
        ordering =  [ '-Published_on' ]







class CEVEE(models.Model):
    job_Name = models.ForeignKey('Added_JOBS', on_delete=models.CASCADE)
    name = models.CharField(max_length=102)
    Email = models.EmailField(max_length=300)
    website = models.URLField()
    cv = models.FileField(upload_to='cvs/')
    Coverletter = models.TextField(max_length=3500)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    



class Cartegory(models.Model):
    name =  models.CharField(max_length=211)
    def __str__(self):
        return self.name
    





