from django.db import models

class Model_truck(models.Model):
    Model_truck = models.CharField(max_length=32)    
    Model_max_weight=models.CharField(max_length=32,blank=True, null=True)
    Model_current_weight=models.CharField(max_length=32,blank=True, null=True)
    def __str__(self):
        return self.Model_truck
    
class Garage(models.Model):
    GarageNo = models.CharField(max_length=32)
    model = models.ForeignKey(Model_truck,on_delete=models.CASCADE)
    poid=models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.GarageNo
# Create your models here.

