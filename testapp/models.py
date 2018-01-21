from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=True)

    def __str__(self):
        return self.name
