from django.db import models
import datetime
# Create your models here.


class shahar(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    img = models.ImageField(default='')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'shaxar'
        verbose_name_plural = 'shaxarlar'

class Contact(models.Model):
    ism = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mavzu = models.CharField(max_length=50)
    matn = models.TextField()
    vaqt = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.ism

class Davlat(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(default='')


    def __str__(self):
        return self.title