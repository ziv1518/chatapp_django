from tkinter import CASCADE
from django.db import models
from account.models import User
from django.utils import timezone

# Create your models here.

class friend(models.Model):
    user1 = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='user1')
    user2 = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='user2')
    messages = models.ManyToManyField('message',blank=True)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return str((self.user1.username, self.user2.username))

    def get_latest_message(self):
        return self.messages.latest('created')
'''
class chatroom(models.Model):
    users = models.ManyToManyField(User,related_name='users')
    created = models.DateTimeField(auto_now_add=True)
    
'''
class message(models.Model):
    author = models.ForeignKey(User,related_name='author',on_delete=models.PROTECT)
    content = models.CharField(max_length=500,verbose_name='content')
    created = models.DateTimeField(auto_now_add=True)
