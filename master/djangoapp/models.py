from django.db import models

# Create your models here.
class Category(models.Model):
    category=models.CharField(max_length=200,unique=True)
    description=models.CharField(max_length=200)

    def __str__(self):
        return self.category
    

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    product=models.CharField(max_length=100)
    supplier=models.CharField(max_length=100)
    price=models.FloatField(max_length=100)
    stock=models.IntegerField(max_length=100,default=0)
    
    def __str__(self):
        return self.product
    
    