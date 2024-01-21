from django.test import TestCase

# Create your tests here.
# car_classifier/models.py
from django.db import models

class CarImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
