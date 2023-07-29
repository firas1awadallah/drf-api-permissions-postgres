from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Snack(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    desc = models.TextField()
    rank = models.IntegerField(default=0)
    price = models.TextField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title 