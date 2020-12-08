from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.RoomType)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    pass


@admin.register(models.Amenity)
class RoomAdmin(admin.ModelAdmin):

    """ Amenity Admin Definition """

    pass


@admin.register(models.Facility)
class RoomAdmin(admin.ModelAdmin):

    """ Facility Admin Definition """

    pass


@admin.register(models.HouseRule)
class RoomAdmin(admin.ModelAdmin):

    """ HouseRule Admin Definition """

    pass


@admin.register(models.Photo)
class RoomAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    pass
