from django.db import models

class Subscriber(models.Model):
    name= models.CharField(max_length=20)
    email= models.EmailField(max_length=30)
    def __str__(self):
            return self.name

class Content(models.Model):
    content_type= models.CharField(max_length=20)
    branch= models.CharField(max_length=20)
    semester= models.IntegerField()
    subject= models.CharField(max_length=40)
    file= models.FileField()
    def __str__(self):
        return self.subject
    
class User(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    def __str__(self):
        return self.username
