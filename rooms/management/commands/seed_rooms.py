import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from django.contrib.admin.utils import flatten
from users import models as user_models
from rooms import models as room_models


# e.g. python manage.py loveyou --time 50
class Command(BaseCommand):
    help = "This command helps create rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many rooms do you want to create!",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "price": lambda x: random.randint(1, 300),
                "beds": lambda x: random.randint(1, 10),
                "bathrooms": lambda x: random.randint(1, 10),
                "baths": lambda x: random.randint(1, 10),
                "guests": lambda x: random.randint(1, 10),
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        houserules = room_models.HouseRule.objects.all()

        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 30)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"room_photos/{random.randint(1,31)}.webp",
                )

            for a in amenities:
                rn = random.randint(0, 15)
                if rn % 2 == 0:
                    room.amenities.add(a)

            for f in facilities:
                rn = random.randint(0, 15)
                if rn % 2 == 0:
                    room.facilities.add(f)

            for h in houserules:
                rn = random.randint(0, 15)
                if rn % 2 == 0:
                    room.houserules.add(h)

        # seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} rooms created"))
