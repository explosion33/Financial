from django.db import models
import datetime

# Create your models here.

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    year_end = models.DateField(blank=True)

    def __str__(self):
        return self.name

class Subsidiary(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=15)
    ownership = models.FloatField(default=1.0)
    ref = models.CharField(max_length=10)
    #FINANCIAL MODEL
    gross_income = models.FloatField(default=0)
    eci = models.FloatField(default=0)
    sub_f = models.FloatField(default=0)
    rp_div = models.FloatField(default=0)
    for_tax = models.FloatField(default=0)
    qbai = models.FloatField(default=0)
    int_exp = models.FloatField(default=0) 