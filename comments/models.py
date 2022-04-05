from pyexpat import model
from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from accounts.models import Account
from projects.models import Project
from django.contrib.auth.models import AbstractUser, User
import projects

# Create your models here.
class Single(models.Model):
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.CharField(max_length=300)

    def __str__(self):
        return self.Project



class Rating(models.Model):
    Project = models.ForeignKey(projects, on_delete=models.CASCADE),
    user = models.ForeignKey(Account, on_delete=models.CASCADE),
    rating = models.FloatField()


    def __str__(self):
        return self.rating


