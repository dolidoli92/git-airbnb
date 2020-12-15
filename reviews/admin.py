from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    """ Review Admin Definition """

    # '__str__' :
    # if anaother function exists in models.py, lose it when you write it
    list_display = ("__str__", "room", "rating_average")
