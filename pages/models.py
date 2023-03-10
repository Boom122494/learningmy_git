from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()
    comments = models.CharField(max_length=256)
    email = models.EmailField()

    def __str__(self):
        return self.text[:20]