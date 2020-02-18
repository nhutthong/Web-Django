from django.db import models

class SanPham(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    img_url = models.CharField(max_length=255)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    descript = models.CharField(max_length=255)
    discount = models.FloatField()

class Infomation(models.Model):
    name = models.CharField(max_length=255)
    cls = models.CharField(max_length=10)
    major = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    score = models.FloatField()