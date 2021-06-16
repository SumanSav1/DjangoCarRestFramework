from django.contrib import admin
from .models import CarPredictionModel
# Register your models here.


@admin.register(CarPredictionModel)
class CarPredictionAdmin(admin.ModelAdmin):
    list_display = ['year', 'price', 'kilometers', 'owners', 'fueltype', 'dealer', 'transmissiontype']

