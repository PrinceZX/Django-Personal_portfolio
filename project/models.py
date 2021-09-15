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


class Comment(models.Model):
    post = models.ForeignKey(AutoProject,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
