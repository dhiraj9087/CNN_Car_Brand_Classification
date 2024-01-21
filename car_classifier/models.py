from django.db import models

# Create your models here.
# car_classifier/models.py
from django.db import models

class CarImage(models.Model):
    image = models.FileField(upload_to='uploads/')
