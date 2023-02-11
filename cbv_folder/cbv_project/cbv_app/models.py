from django.db import models
from django.urls import reverse


# Create your models here.

class Movie(models.Model):
    movieName = models.CharField(max_length= 300)
    moviePriority = models.IntegerField()
    movieImg = models.ImageField(upload_to='task_img')
    movieDate = models.DateField()
    movieInfo = models.TextField()

    def __str__(self):
        return self.movieName