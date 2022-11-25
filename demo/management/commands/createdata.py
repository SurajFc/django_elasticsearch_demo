import random
from django.core.management.base import BaseCommand
from faker import Faker
from demo.models import Artist, Movie

fake = Faker()


class Command(BaseCommand):
    help = "Command information"

    def get_artist(self):
        return Artist.objects.get(id=random.randint(1, 200))

    def handle(self, *args, **kwargs):
        for _ in range(200):
            print("creating artists", _)
            Artist.objects.create(name=fake.unique.name(),
                                  email=fake.unique.free_email())

        for _ in range(100):
            print("creating movie", _)
            Movie.objects.create(name=fake.unique.paragraph(1), artist=self.get_artist(),
                                 rating=random.randint(1, 10),
                                 description=fake.paragraph(nb_sentences=15))
