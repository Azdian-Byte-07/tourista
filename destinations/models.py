from django.db import models


class Destination(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    pretty_picture = models.ImageField()
    activities = models.TextField()
    optimal_visiting_season = models.CharField(max_length=10)

'''

from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    logo = models.ImageField(upload_to='restaurant_logos', null=True, blank=True)


    def __str__(self):
        return self.name


class User(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=50)


    def __str__(self):
        return self.first_name

'''