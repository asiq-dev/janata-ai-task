from django.db import models

# Create your models here.


class Stock(models.Model):
    date = models.DateField()
    trade_code = models.TextField()
    high = models.TextField()
    low = models.TextField()
    open = models.TextField()
    close = models.TextField()
    volume = models.TextField()
