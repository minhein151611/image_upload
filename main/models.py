from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="photoes/")

    def __str__(self):
        return self.name