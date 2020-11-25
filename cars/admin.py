from django.contrib import admin
from cars.models import UserDetails,Car_miles,Car_roof,Car_engine,Car_service
# Register your models here.
admin.site.register(UserDetails)
admin.site.register(Car_miles)
admin.site.register(Car_roof)
admin.site.register(Car_engine)
admin.site.register(Car_service)
