from django.db import models

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)


    def __str__(self):
        return self.name


class Marca(models.Model):
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    price = models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    info = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.name