from django.db import models

# Create your models here.

class Car_miles(models.Model):
    miles_on_car = models.CharField(max_length=100)
    def __str__(self):
        return self.miles_on_car

class Car_roof(models.Model):
    roof_type = models.CharField(max_length=100)
    glass_color = models.CharField(max_length=100)
    def __str__(self):
        return self.roof_type

class Car_engine(models.Model):
    engine_capacity = models.CharField(max_length=100)
    def __str__(self):
        return self.engine_capacity

class Car_service(models.Model):
    service_type = models.CharField(max_length=100)
    def __str__(self):
        return self.service_type

class UserDetails(models.Model):

    car_name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    owner_age = models.IntegerField(null=True,blank=True)
    year_of_purchase = models.IntegerField()
    roof = models.ForeignKey(Car_roof,on_delete=models.CASCADE,related_name='carroof',null=True,blank=True)
    miles = models.ForeignKey(Car_miles,on_delete=models.CASCADE,related_name='carmiles')
    car_color = models.CharField(max_length=100)
    engine = models.ForeignKey(Car_engine,on_delete=models.CASCADE,related_name='carengine')
    user_image = models.ImageField(upload_to='car_image')
    servicing = models.ManyToManyField(Car_service,related_name='car_services')
    insurance =  models.BooleanField(null=True,blank=True)

    def __str__(self):
        return self.car_name
