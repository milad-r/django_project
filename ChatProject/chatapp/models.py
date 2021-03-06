from django.db import models

class Message(models.Model):
    sender = models.ForeignKey('User', on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey('User', on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    seen    = models.BooleanField(default=False)
    
    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp',)



class User(models.Model):
    username= models.CharField(max_length=10 , unique=True , primary_key=True )
    phone_number  = models.CharField(max_length=11 , default="0" , unique=True)
    profile_image = models.ImageField(upload_to='upload/images/profileimages/', null=True , blank=True)
    reg_google    = models.CharField(max_length=400,null=True)
    def __str__(self):
        return self.username

            
