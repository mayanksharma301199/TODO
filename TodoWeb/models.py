from django.db import models

class Task(models.Model):
    Content = models.CharField(max_length = 255)
    Status = models.CharField(max_length = 10, default = "false")
    Userid = models.IntegerField(default=0)

class User(models.Model):
    Name = models.CharField(max_length = 50, default = "None")
    UserEmail = models.EmailField(max_length = 254)
    Password = models.CharField(max_length = 255, default = "None")

    USERNAME_FIELD = 'UserEmail'

class BlacklistToken(models.Model):
    TokenVlaue = models.CharField(max_length = 255)
    TokenExpiryDate = models.IntegerField(default=0)
    Status = models.CharField(max_length = 10, default = "false")
