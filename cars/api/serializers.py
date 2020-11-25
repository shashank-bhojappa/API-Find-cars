from rest_framework import serializers
from cars.models import Car_miles,Car_roof,Car_engine,Car_service,UserDetails

class CarMilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car_miles
        fields = ('miles_on_car',)

class CarRoofSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car_roof
        fields = ('roof_type','glass_color')

class CarEngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car_engine
        fields = ('engine_capacity',)

class CarServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car_service
        fields = ('service_type',)

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ('id','car_name','owner_name','owner_age','year_of_purchase','roof','miles','car_color','engine','user_image','servicing','insurance')
        depth = 1
#Used For Class Based views
class ClassUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ('id','car_name','owner_name','owner_age','year_of_purchase','roof','miles','car_color','engine','user_image','servicing','insurance')
        depth = 1 #shows details of foreign key and many to many fields options
