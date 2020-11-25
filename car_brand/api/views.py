from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from .serializer import CarSpecsSerializer
from car_brand.models import CarSpecs, CarPlan
import json
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
import os

class CarSpecsViewset(viewsets.ModelViewSet):
    serializer_class = CarSpecsSerializer

    def get_queryset(self):
        car_specs = CarSpecs.objects.all()
        return car_specs

    # def retrieve(self, request, *args, **kwargs):
    #     params = kwargs
    #     print(params['pk'])
    #     params_list = params['pk'].split('-')
    #     cars = CarSpecs.objects.filter(
    #         car_brand=params_list[0], car_model=params_list[1])
    #     serializer = CarSpecsSerializer(cars, many=True)
    #     return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        car_data = request.data

        new_car = CarSpecs.objects.create(car_plan=CarPlan.objects.get(id=car_data["car_plan"]), car_brand=car_data["car_brand"], car_model=car_data[
            "car_model"], production_year=car_data["production_year"], car_body=car_data["car_body"], engine_type=car_data["engine_type"])

        new_car.save()

        serializer = CarSpecsSerializer(new_car)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        logedin_user = request.user
        if(logedin_user == "admin"):
            car = self.get_object()
            car.delete()
            response_message = {"message": "Item has been deleted"}
        else:
            response_message = {"message": "Not Allowed"}

        return Response(response_message)

    def update(self, request, *args, **kwargs):
        car_object = self.get_object()
        data = request.data

        car_plan = CarPlan.objects.get(plan_name=data["plan_name"])

        car_object.car_plan = car_plan
        car_object.car_brand = data["car_brand"]
        car_object.car_model = data["car_model"]
        car_object.production_year = data["production_year"]
        car_object.car_body = data["car_body"]
        car_object.engine_type = data["engine_type"]

        car_object.save()

        serializer = CarSpecsSerializer(car_object)

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):#ex: http://127.0.0.1:8000/car-brand/car-specs/1/
        car_object = self.get_object()
        data = request.data

        try:
            car_plan = CarPlan.objects.get(plan_name=data["plan_name"])
            car_object.car_plan = car_plan
        except KeyError:
            pass

        car_object.car_brand = data.get("car_brand", car_object.car_brand)
        car_object.car_model = data.get("car_model", car_object.car_model)
        car_object.production_year = data.get("production_year", car_object.production_year)
        car_object.car_body = data.get("car_body", car_object.car_body)
        car_object.engine_type = data.get("engine_type", car_object.engine_type)

        car_object.save()

        serializer = CarSpecsSerializer(car_object)

        return Response(serializer.data)
        #ex:
        #{
        #    "production_year": "2019", (Changed value from 2018 to 2019
        #    "plan_name": "Third Plan" (changed value from First Plan to Third Plan , also this is a Foreign key)
        #}
