from django.db import models

# Create your models here.

class Posts(models.Model):
    user_name = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.user_name