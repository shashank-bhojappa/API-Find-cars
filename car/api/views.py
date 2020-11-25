from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import CarsSerializer
from car.models import Cars

#APIView
class CarsAPIView(APIView):
    serializer_class = CarsSerializer

    def get_queryset(self):
        cars = Cars.objects.all()
        return cars

    def get(self, request, *args, **kwargs):
        try:
            id = request.query_params["id"]#(ex: http://127.0.0.1:8000/cars-app/cars/?id=2) use GET request
            if id != None:
                car = Cars.objects.get(id=id)
                serializer = CarsSerializer(car)
        except:
            cars = self.get_queryset()
            serializer = CarsSerializer(cars, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):#use POST request
        car_data = request.data

        new_car = Cars.objects.create(car_brand=car_data["car_brand"], car_model=car_data["car_model"], production_year=car_data["production_year"], car_body=car_data["car_body"], engine_type=car_data["engine_type"])

        new_car.save()
        serializer = CarsSerializer(new_car)
        return Response(serializer.data)
        #{
        #"car_brand": "BMW",
        #"car_model": "M4",
        #"production_year": "2020",
        #"car_body": "coupe",
        #"engine_type": "Petrol"
    #}

    def put(self, request, *args, **kwargs):#(ex: http://127.0.0.1:8000/cars-app/cars/?id=1) use PUT request
        try:
            id = request.query_params["id"]
            if id != None:
                car_object = Cars.objects.get(id=id)

                data = request.data

                car_object.car_brand = data["car_brand"]
                car_object.car_model = data["car_model"]
                car_object.production_year = data["production_year"]
                car_object.car_body = data["car_body"]
                car_object.engine_type = data["engine_type"]

                car_object.save()
                serializer = CarsSerializer(car_object)

        except:
            cars = self.get_queryset()
            serializer = CarsSerializer(cars, many=True)
        return Response(serializer.data)
                #{
                #"id": 1,
                #"car_brand": "BMW",
                #"car_model": "M4",
                #"production_year": "2020",
                #"car_body": "coupe",
                #"engine_type": "Petrol"
            #} edit values

                #{
                #"id": 1,
                #"car_brand": "BMW",
                #"car_model": "M4",
                #"production_year": "2020",
                #"car_body": "coupe",
                #"engine_type": "Hybrid"  (value changed to Hybrid from Petrol)
            #}
    def patch(self, request, *args, **kwargs):#http://127.0.0.1:8000/cars-app/cars/?id=1
        try:
            id = request.query_params["id"]
            if id != None:
                car_object = Cars.objects.get(id=id)
                data = request.data

                car_object.car_brand = data.get("car_brand", car_object.car_brand)
                car_object.car_model = data.get("car_model", car_object.car_model)
                car_object.production_year = data.get("production_year", car_object.production_year)
                car_object.car_body = data.get("car_body", car_object.car_body)
                car_object.engine_type = data.get("engine_type", car_object.engine_type)

                car_object.save()
                serializer = CarsSerializer(car_object)
        except:
            cars = self.get_queryset()
            serializer = CarsSerializer(cars, many=True)
        return Response(serializer.data)
      #ex 1. only one value changed
      # {
      #       "engine_type": "Diesel"  (value changed to Diesel from Petrol)
      #  }
      #ex.2 Two values changed
        #{
        #    "production_year": "2019", (value changed from 2020 to 2019)
        #    "engine_type": "Petrol" (value changed from Diesel to Petrol)
        #}
