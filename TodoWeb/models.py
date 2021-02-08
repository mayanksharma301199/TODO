from django.db import models

class Task(models.Model):
    Content = models.CharField(max_length = 255)
    Status = models. CharField(max_length = 10, default = "false")