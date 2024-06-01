from django.db import models

# Create your models here.


class service(models.Model):
    banner = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    discription = models.CharField(max_length=1000)

class serviceattribute(models.Model):
    att_of = models.ForeignKey(service,default=None,on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    discription = models.CharField(max_length=1000)

class technology(models.Model):
    tlogo = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)

class skill(models.Model):
    tech = models.ForeignKey(technology,on_delete=models.DO_NOTHING)
    certification = models.CharField(blank=True,default=None,max_length=300)
    cerlogo = models.ImageField(blank=True,default=None,upload_to='images/')
    cerimg = models.ImageField(blank=True,default=None,upload_to='images/')
    experience = models.CharField(blank=True,max_length=10)
    project = models.CharField(blank=True,default=None,max_length=1000)
    achievement = models.CharField(blank=True,default=None,max_length=100)

class project(models.Model):
    pimg = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    discription = models.CharField(max_length=10000)
    tech = models.CharField(max_length=300)

class order(models.Model):
     id = models.AutoField(primary_key=True)
     timeline = models.CharField(max_length=300)
     objectives = models.CharField(max_length=3000)
     questions = models.CharField(max_length=3000)
     audience = models.CharField(max_length=3000)

class doc(models.Model):
    doc_name = models.CharField(max_length=50)
    attachment = models.FileField(upload_to='docs/')

class social(models.Model):
    logo = models.ImageField(upload_to='images/')
    url = models.TextField(max_length=1000)

class education(models.Model):
    img = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=300)
    desc = models.CharField(max_length=1000)