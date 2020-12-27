from django.contrib import admin
from . import models
from django.utils.html import mark_safe

# Register your models here.


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    # Photo in Room admin
    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "city", "address", "price")},
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

    # change the host name to number(pk, number)
    raw_id_fields = ("host",)

    search_fields = ("=city", "host__username")
    filter_horizontal = (
        "amenities",
        "facilities",
        "houserules",
    )

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

    def count_amenities(self, obj):
        return obj.amenities.count()

    # count_amenities.short_description = "Hello Sexy"

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "PHOTO COUNT"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="150px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
