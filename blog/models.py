from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=175)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='blog/images/')
    date = models.DateField()


    def __str__(self):
        return self.title