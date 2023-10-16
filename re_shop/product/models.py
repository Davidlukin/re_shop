from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    description = models.CharField(max_length=700)
    image = models.ImageField(blank=True,upload_to='images')

    def __str__(self):
        return self.name