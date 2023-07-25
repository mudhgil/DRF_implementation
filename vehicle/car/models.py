from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=50)
    launch = models.CharField(max_length=100)
    style = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Cars(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    fuel = models.CharField(max_length=50)
    seat = models.IntegerField()
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
