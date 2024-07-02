from django.db import models

# Create your models here.
class Order:
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    items = models.TextField()
    
    def __str__(self):
        return f"{self.last_name} {self.first_name} | {self.phone}"