from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


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
        "count_photos",
        "total_rating",
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

    # count_amenities.short_description = "Hello Sexy"

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ """

    pass
