from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, viewsets
from cars.models import Car_miles,Car_roof,Car_engine,Car_service,UserDetails
from cars.api.serializers import CarMilesSerializer,CarRoofSerializer,CarEngineSerializer,CarServiceSerializer,UserDetailsSerializer,ClassUserDetailsSerializer
from rest_framework.permissions import AllowAny

#Model ViewSet

#Function Based Views
#ex: http://127.0.0.1:8000/api/showcars/28/  use GET type in postman
@api_view(['GET', ])
def get_car(request, pk):
    try:
        car = UserDetails.objects.get(pk=pk)
    except UserDetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserDetailsSerializer(car)
        return Response(serializer.data)

#ex: http://127.0.0.1:8000/api/showcars/  use POST type in postman
@api_view(['POST', ])
def create_car(request):
    if request.method == 'POST':
        cars_data = request.data
        new_cars = UserDetails.objects.create(
            car_name = cars_data["car_name"],
            owner_name = cars_data["owner_name"],
            owner_age = cars_data["owner_age"],
            year_of_purchase = cars_data["year_of_purchase"],
            roof = Car_roof.objects.get(id=cars_data["roof"]),#This is for ForeignKey field
            miles = Car_miles.objects.get(id=cars_data["miles"]),#This is for ForeignKey field
            car_color = cars_data["car_color"],
            engine = Car_engine.objects.get(id=cars_data["engine"]),#This is for ForeignKey field
            user_image = cars_data["user_image"],
            insurance = cars_data["insurance"]
        )
        new_cars.save()

        for services in cars_data["servicing"]:#This is for ManyToMany field
            services_obj = Car_service.objects.get(service_type=services["service_type"])
            new_cars.servicing.add(services_obj)

        serializer = UserDetailsSerializer(new_cars)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

#Class Based Views
#@permission_classes([AllowAny])(we can if we want to allow anyone to view this view or only authenticated users by using IsAuthenticated)
class CarSpecsViewSet(viewsets.ModelViewSet):
    serializer_class = ClassUserDetailsSerializer
#Get all cars also gives post option to create (ex:api/car_specs/)
    def get_queryset(self):
        car_specs = UserDetails.objects.all()
        return car_specs

#Filter by car_id (ex:api/car_specs/3)single parameter GET type
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        car_id = UserDetails.objects.filter(id=params['pk'])
        serializer = ClassUserDetailsSerializer(car_id, many=True)
        return Response(serializer.data)

#Filter by car_name and year_of_purchase, 2 parameters(ex:api/car_specs/BMW-2014)if there is a space in car name use ASCII code(ex: api/car_specs/BMW%20X5-2014) %20 is ASCII code for space
    #def retrieve(self, request, *args, **kwargs):
    #    params = kwargs
    #    params_list = params['pk'].split('-')
    #    car_name_year = UserDetails.objects.filter(car_name=params_list[0], year_of_purchase=params_list[1])
    #    serializer = ClassUserDetailsSerializer(car_name_year, many=True)
    #    return Response(serializer.data)

#Filter by car_name,year_of_purchase and engine 3 parameters(ex:api/car_specs/BMW-2014-5) here 5 is engine_ID .if there is a space in car name use ASCII code(ex: api/car_specs/BMW%20X5-2014-5) %20 is ASCII code for space
    #def retrieve(self, request, *args, **kwargs):
    #    params = kwargs
    #    params_list = params['pk'].split('-')
    #    car_name_year_engine = UserDetails.objects.filter(car_name=params_list[0], year_of_purchase=params_list[1], engine=params_list[2])
    #    serializer = ClassUserDetailsSerializer(car_name_year_engine, many=True)
    #    return Response(serializer.data)

#Over ride Create action
#how to Post in Postman (use POST option )
#example: put this is Body , select raw and JSON type (url: http://127.0.0.1:8000/api/car_specs/)
#{
#        "car_name": "Audi R8",
#        "owner_name": "Jones",
#        "owner_age": 18,
#        "year_of_purchase": 2016,
#        "roof": 3,
#        "miles": 3,
#        "car_color": "Blue",
#        "engine": 2,
#        "user_image": "http://127.0.0.1:8000/media/car_image/audi.png",
#        "servicing": [
#            {
#                "service_type": "Air filter"
#            },
#            {
#                "service_type": "All Lights"
#            },
#            {
#                "service_type": "Suspension"
#            }
#        ],
#        "insurance": true
#    }
    def create(self, request, *args, **kwargs):
        car_data = request.data
        new_car = UserDetails.objects.create(
            car_name = car_data["car_name"],
            owner_name = car_data["owner_name"],
            owner_age = car_data["owner_age"],
            year_of_purchase = car_data["year_of_purchase"],
            roof = Car_roof.objects.get(id=car_data["roof"]),#This is for ForeignKey field
            miles = Car_miles.objects.get(id=car_data["miles"]),#This is for ForeignKey field
            car_color = car_data["car_color"],
            engine = Car_engine.objects.get(id=car_data["engine"]),#This is for ForeignKey field
            user_image = car_data["user_image"],
            insurance = car_data["insurance"]
        )
        new_car.save()

        for service in car_data["servicing"]:#This is for ManyToMany field
            service_obj = Car_service.objects.get(service_type=service["service_type"])
            new_car.servicing.add(service_obj)

        serializer = ClassUserDetailsSerializer(new_car)
        return Response(serializer.data)

#Delete selected  items only if you are an admin
    def destroy(self, request, *args, **kwargs):
        loggedin_user = request.user
        if(loggedin_user == "admin"):
            car = self.get_object()
            car.delete()
            response_message={"message": "Item has been deleted"}
        else:
            response_message={"message": "not allowed to delete"}

        return Response(response_message)

    def update(self, request, *args, **kwargs):
        car_object = self.get_object()
        data = request.data

        miles = Car_miles.objects.get(miles_on_car=data["miles_on_car"])
        roof = Car_roof.objects.get(roof_type=data["roof_type"])
        engine = Car_engine.objects.get(engine_capacity=data["engine_capacity"])

        for service in data["servicing"]:#(Tried working on updating ManyToMany field but update is not working for ManyToMany field)
            servicing = Car_service.objects.get(service_type=service["service_type"])
            car_object.servicing = servicing

        car_object.car_name = data["car_name"]
        car_object.owner_name = data["owner_name"]
        car_object.owner_age = data["owner_age"]
        car_object.year_of_purchase = data["year_of_purchase"]
        car_object.roof = roof
        car_object.miles = miles
        car_object.car_color = data["car_color"]
        car_object.engine = engine
        car_object.user_image = data["user_image"]
        car_object.insurance = data["insurance"]
