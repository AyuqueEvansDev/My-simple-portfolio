
from django.db import models
import datetime

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='images.posts')
    date = models.DateField(datetime.date.today)

