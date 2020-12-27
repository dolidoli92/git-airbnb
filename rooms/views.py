from django.utils import timezone
from django.utils.text import slugify
from django.views.generic import ListView, DetailView
from django_countries import countries
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    # reference : http://ccbv.co.uk/
    model = models.Room
    paginate_by = 10
    ordering = "created"
    paginate_orphans = 3
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now

        return context


"""
def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        # return render(request, "404.html")
        raise Http404("This Page does not exist")
        # return redirect(reverse("core:home"))
"""


class RoomDetail(DetailView):

    model = models.Room


def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))

    price = int(request.GET.get("price", 0))
    guests = int(request.GET.get("guests", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    beds = int(request.GET.get("beds", 0))
    baths = int(request.GET.get("baths", 0))

    # Room type
    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()

    instant = request.GET.get("instant", False)
    super_host = request.GET.get("super_host", False)

    # selected
    s_amenities = request.GET.getlist("amenities")
    s_facilities = request.GET.getlist("facilities")

    # s_amenities = list(map(int, s_amenities))
    # s_facilities = list(map(int, s_facilities))

    form = {
        "city": city,
        "s_room_type": room_type,
        "s_country": country,
        "price": price,
        "guests": guests,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
        "s_amenities": s_amenities,
        "s_facilities": s_facilities,
        "instant": instant,
        "super_host": super_host,
    }

    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
    }

    qs = models.Room.objects.filter()

    if price != 0:
        qs = qs.filter(price__lte=price)

    return render(request, "rooms/search.html", {**form, **choices})
