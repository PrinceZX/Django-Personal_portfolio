from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class AutoProject(models.Model):
    title = models.CharField(max_length=175)
   # description = models.TextField()
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='project/images/')
    date = models.DateField()


    def __str__(self):
        return self.title
