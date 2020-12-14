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

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        (
            "Times",
            {"fields": ("check_in", "check_out")},
        ),
        (
            "Space",
            {
                "fields": (
                    "beds",
                    "bathrooms",
                    "baths",
                    "guests",
                )
            },
        ),
        (
            "More About the Spac",
            {"fields": ("amenities", "facilities", "houserules")},
        ),
        (
            "Last Details",
            {"fields": ("host",)},
        ),
    )

    list_display = (
        "name",
        "description",
        "country",
        "city",
        "price",
        "beds",
        "bathrooms",
        "baths",
        "guests",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
    )

    ordering = ("-name", "country")

    list_filter = (
        "instant_book",
        "city",
        "country",
    )
    search_fields = ("=city", "host__username")
    filter_horizontal = (
        "amenities",
        "facilities",
        "houserules",
    )

    def count_amenities(self, obj):
        return obj.amenities.count()

    count_amenities.short_description = "Hello Sexy"


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
