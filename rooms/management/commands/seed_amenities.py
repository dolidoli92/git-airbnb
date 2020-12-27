from django.core.management.base import BaseCommand
from rooms.models import Amenity


# e.g. python manage.py loveyou --time 50
class Command(BaseCommand):
    help = "This command helps create amenities"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", help="How many amenities do you want to create!"
        )
        parser.add_argument(
            "--times", help="How many times amenities do you want to create!"
        )

    def handle(self, *args, **options):
        amenities = [
            "Air conditioning",
            "Alarm Clock",
            "Balcony",
            "Bathroom",
            "Bathtub",
            "Bed Linen",
            "Boating",
            "Cable TV",
            "Carbon monoxide detectors",
            "Chairs",
            "Children Area",
            "Coffee Maker in Room",
            "Cooking hob",
            "Cookware & Kitchen Utensils",
            "Dishwasher",
            "Double bed",
            "En suite bathroom",
            "Free Parking",
            "Free Wireless Internet",
            "Freezer",
            "Fridge / Freezer",
            "Golf",
            "Hair Dryer",
            "Heating",
            "Hot tub",
            "Indoor Pool",
            "Ironing Board",
            "Microwave",
            "Outdoor Pool",
            "Outdoor Tennis",
            "Oven",
            "Queen size bed",
            "Restaurant",
            "Shopping Mall",
            "Shower",
            "Smoke detectors",
            "Sofa",
            "Stereo",
            "Swimming pool",
            "Toilet",
            "Towels",
            "TV",
        ]

        if options["number"]:
            for a in amenities:
                Amenity.objects.create(name=a)

            self.stdout.write(self.style.SUCCESS("Amenities created"))
