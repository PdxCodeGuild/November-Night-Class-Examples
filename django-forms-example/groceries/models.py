from django.db import models

class GroceryItem(models.Model):
    name = models.CharField(max_length=128)
    quantity = models.IntegerField(default=1)