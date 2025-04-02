from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "jobs/%s.%s" %(instance.id,extension)

class Job(models.Model):
    JOB_TYPE =(
        ('Full Time','Full Time'),
        ('Part Time','Part Time'),
    )
    owner = models.ForeignKey(User,related_name='job_owner',on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    #location
    description = models.TextField(max_length=1000)
    job_type = models.CharField(max_length=20 , choices=JOB_TYPE)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experince = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(blank=True,null=True)


    def save(self,*args,**kwrgs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args,**kwrgs)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name
    
class Apply(models.Model):
    job = models.ForeignKey(Job,related_name='apply_job',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    created_at = models.DateTimeField(auto_now=True)
    cover_letter = models.TextField(max_length=500)

    def __str__(self):
        return self.name