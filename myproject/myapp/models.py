from django.db import models
from django import forms

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=30)
    
    class Meta:
        db_table="User"
    def __str__(self):
        return self.username

class Reporter(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta():
       db_table="reporter"
        
class Profile(models.Model):
    name=models.CharField(max_length=50)
    picture=models.ImageField(upload_to='pictures')
    
    def __repr__(self):
        return self.name
    
    class Meta():
        db_table='Profile'
        
class Questions(models.Model):
    question=models.CharField(max_length=1000)
    
    def __str__(self):
        return self.question
        
    class Meta():
        db_table='Questions'
        
class Article(models.Model):
    name=models.CharField(max_length=250)
    reporter=models.ForeignKey(Reporter,on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s"%(self.name)
    
    class Meta():
        db_table="article"
     
 