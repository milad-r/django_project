from django.db import models 
import uuid 
from django.shortcuts import reverse
class Post(models.Model):
    writer     = models.ForeignKey('Writer', on_delete = models.CASCADE)
    title      = models.CharField(max_length=150)
    body       = models.TextField()
    timestamp  = models.DateTimeField()
    assortment = models.ManyToManyField('Assortment', help_text ='please enter a assortment' )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:post_detail", kwargs={"pk": self.id})
    

class Writer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name  = models.CharField(max_length = 25)
    birthDay   = models.DateField()

    def __str__(self):
        return self.first_name + self.last_name

    
class Assortment(models.Model):
    name = models.CharField(max_length = 20 , help_text = 'select a assortment for the your post')

    def __str__(self):
        return self.name


class User_profile(models.Model):
    user_name = models.CharField(max_length = 20)
    user_first_name = models.CharField(max_length = 20)
    user_last_name = models.CharField(max_length = 20)
    