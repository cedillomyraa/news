from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.name
# Create your models here.
