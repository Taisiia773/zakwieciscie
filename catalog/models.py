from django.db import models

# Create your models here.
class Flower(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    img = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} | {self.color} | {self.price} zl"
    
    class Meta:
        verbose_name = "Flower"
        verbose_name_plural = "Flowers"