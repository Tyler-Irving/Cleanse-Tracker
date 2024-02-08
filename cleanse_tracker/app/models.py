from django.db import models
from django.contrib.auth.models import User

class Cleanse(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

class Restriction(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class CleanseEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cleanse = models.ForeignKey(Cleanse, on_delete=models.CASCADE)
    restriction = models.ForeignKey(Restriction, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)