import random
from django.core.management.base import BaseCommand
from api.models import Hotel, City

class Command(BaseCommand):
    help = 'Generate hotels for each city (2 per city with 5 images each)'

    def handle(self, *args, **kwargs):
        # Hotel.objects.all().delete()

        Hotel.objects.create(
                    name="NH Collection New York Madison Avenue",
                    city=City.objects.get(id=1),
                    address="22 East 38th Street, New York, NY 10016",
                    rating=4.0,
                    description="Reopened on May 2021 after a full renovation, the NH Collection New York Madison Avenue is about as central as it gets. This 100-year-old building offers an ideal location at Madison Avenue and 38th street, within walking distance to some of the big attractions, like the Empire State Building. Step inside to enjoy cutting-edge interior design, with nods to Madison Avenue's golden age of advertising.",
                    images=["https://img.nh-hotels.net/1g8Ez/N0gDJ/original/NH_Collection_New_York_Madison_Avenue_Views_night_facade_Empire.jpg?output-quality=80&resize=1110:*&composite-to=center,center|1110:380&background-color=white",
                            "https://img.nh-hotels.net/1g8Ez/vEX24q/original/NH_Collection_New_York_Madison_Avenue_Room_Suite_Penthouse_Empire_State_Living_Room_Sunset.jpg?output-quality=80&resize=1110:*&composite-to=center,center|1110:380&background-color=white",
                            "https://img.nh-hotels.net/1g8Ez/B8lkN/original/NH_Collection_New_York_Madison_Avenue_Room_junior_suite_skyline.jpg?output-quality=80&resize=1110:*&composite-to=center,center|1110:380&background-color=white",
                            "https://img.nh-hotels.net/1g8Ez/r9JZg/original/NH_Collection_New_York_Madison_Avenue_Room_suite_empire_state_bathroom.jpg?output-quality=80&resize=1110:*&composite-to=center,center|1110:380&background-color=white",
                            "https://img.nh-hotels.net/1g8Ez/aVlw8/original/NH_Collection_New_York_Madison_Avenue_Bar_interior_empty_panoramic_view.jpg?output-quality=80&resize=1110:*&composite-to=center,center|1110:380&background-color=white"],
                )
        
        Hotel.objects.create(
                    name="Hyatt Place New York City - Times Square",
                    city=City.objects.get(id=1),
                    address="350 W 39th St, New York, NY 10018",
                    rating=4.5,
                    description="Hyatt Place New York City/Times Square features air-conditioned rooms with satellite flat-screen TV in the Hell's Kitchen district of New York City. Among the facilities of this property are a restaurant, a 24-hour front desk and a shared lounge, along with free WiFi throughout the property. The hotel has newspapers and an ATM machine that guests can use.",
                    images=["https://cf.bstatic.com/xdata/images/hotel/max1280x900/487340251.jpg?k=b732283c1716030abfac949c760791ac407630ae4d73b5fa8671bfb40b477c35&o=&hp=1",
                            "https://cf.bstatic.com/xdata/images/hotel/max1280x900/535073146.jpg?k=10c717871b485d48829f95d871d64c73d3ace64a3bed63619ae829bffe6dd58a&o=&hp=1",
                            "https://cf.bstatic.com/xdata/images/hotel/max1280x900/535073128.jpg?k=7c6d3c7d53bbb87171936efc28cd87d002e1dcf236765c78c53db52b0cf5fc8e&o=&hp=1",
                            "https://cf.bstatic.com/xdata/images/hotel/max1280x900/535073139.jpg?k=ba35be9ea9ccd96469642c6e4ac1d2330bb7fa57eea3aed7a8a429fbc9ac8977&o=&hp=1",
                            "https://cf.bstatic.com/xdata/images/hotel/max1280x900/535073123.jpg?k=f6e0fc8ab297c39597831e2a2425aa78522d5919b988cb509be7dee14d8f2cbf&o=&hp=1"],
                )
        
        Hotel.objects.create(
                    name="Hampton Inn & Suites by Hilton Toronto Downtown",
                    city=City.objects.get(id=2),
                    address="300 Jarvis Street, M5B 2C5 Toronto, CanadaAfter booking, all of the property’s details, including telephone and address, are provided in your booking confirmation and your account.",
                    rating=3.0,
                    description="Located in downtown Toronto, the Hampton Inn & Suites by Hilton Toronto Downtown features a state-of-the-art fitness center. The shops and restaurants of Yonge Street are less than 10 minutes' walk away.",
                    images=["https://cf.bstatic.com/xdata/images/hotel/max1280x900/521029731.jpg?k=5639ce0f4fb1e73837b43ea4e746e4069239a7b2307c883750b8772a8b8e29db&o=&hp=1",
                            "https://cf.bstatic.com/xdata/images/hotel/max1280x900/498456729.jpg?k=7d3a71459e6438d8854e5dfe3599bd526581f61f53b29da0ffdfb7141d4fb782&o=&hp=1",
                            "https://cf.bstatic.com/xdata/images/hotel/max1280x900/498456689.jpg?k=35027f5f0f4dc79c12a8aaa4659cb0f6d694c82396d207bc58478fe99924b75d&o=&hp=1",
                            "https://cf.bstatic.com/xdata/images/hotel/max1280x900/515242629.jpg?k=0186f69fa83f02dada34b50f65f8f465c04d5563efe528023c89ffe2047aa05d&o=&hp=1",
                            "https://cf.bstatic.com/xdata/images/hotel/max1280x900/515242667.jpg?k=35dfa3e9672f14d056e2789ceefb4e5051f66ffaeacb884dc1733210bceaafca&o=&hp=1"],
                )
        
        Hotel.objects.create(
                    name="The Novotel Toronto Centre",
                    city=City.objects.get(id=2),
                    address="45 The Esplanade, M5E 1W2 Toronto, Canada",
                    rating=4.0,
                    description="Featuring an indoor pool, hot tub and spa, Novotel Toronto Center is located within a 10-minute walk of Toronto Union Station and Air Canada Center. Guests can enjoy the on-site restaurant and free WiFi available throughout the property.",
                    images=["https://cf.bstatic.com/xdata/images/hotel/max1024x768/251699828.jpg?k=4607836fd7960a655da708a52b652d52b797c5cb6576dbcdc584d3bc5f7404bc&o=",
                            "https://cf.bstatic.com/xdata/images/hotel/max1280x900/567236688.jpg?k=348daa94290b94c35c532c88046b0b8b3cc180534ed9fe247ec5381780a18f63&o=&hp=1",
                            "https://cf.bstatic.com/xdata/images/hotel/max1280x900/251699829.jpg?k=ae8584011b4ad639f0717e7c3ff00fbc3038c59bd347dc84103bfc28b951a26e&o=&hp=1",
                            "https://cf.bstatic.com/xdata/images/hotel/max1280x900/642500088.jpg?k=2bd171ff6141324f1bc685a4b1b1496dc875372e81e90134b3623094090e3c0a&o=&hp=1",
                            "https://cf.bstatic.com/xdata/images/hotel/max1280x900/567236609.jpg?k=eeb191f86bda8dc7f35ea072b4c6e37fdc83ad378be8c3921470f624051497e5&o=&hp=1"],
                )
        
        Hotel.objects.create(
                    name="Hôtel Paris Bastille Boutet - MGallery",
                    city=City.objects.get(id=3),
                    address="22 24 Rue Faidherbe, 11th arr., 75011 Paris, France",
                    rating=5.0,
                    description="Get the celebrity treatment with world-class service at Hôtel Paris Bastille Boutet - MGallery. Located in the heart of Paris just 0.6 mi from Opéra Bastille, Hotel Paris Bastille Boutet – MGallery Collection offers accommodations with a spa center and indoor heated swimming pool.",
                    images=["https://cf.bstatic.com/xdata/images/hotel/max1280x900/326418860.jpg?k=b5dd1d959643741b37ae9445bf24078deac0c714328362044c922c4f083595cc&o=&hp=1",
                            "https://cf.bstatic.com/xdata/images/hotel/max1280x900/326418863.jpg?k=18e7825c227b85cfd3e6de72c082a8f2e594240242fb4d288b95f255073486f0&o=&hp=1",
                            "https://cf.bstatic.com/xdata/images/hotel/max1280x900/326418878.jpg?k=05301541df65e98bd67f3a116b26b8ab37f82d1aa665acf9d5494d86bafb5d3b&o=&hp=1",
                            "https://cf.bstatic.com/xdata/images/hotel/max1280x900/666130459.jpg?k=37ce54376dc707a3eed0cfc04859ac0d384ef87421e057b114303e139ae3a755&o=&hp=1",
                            "https://cf.bstatic.com/xdata/images/hotel/max1280x900/665318185.jpg?k=489c7007422344bf4ea1ac82fe512dcd4179a0f086f6a25c7cd70643b664b9e3&o=&hp=1"
                        ],
                )

        # Здесь надо продолжить создание отелей для других городов 
        # Hotel.objects.create(
        #             name=hotel_name,
        #             city=City.objects.get(id=3),  # Paris
        #             address=f"{random.randint(1, 100)} {city.name} Street",
        #             rating=round(random.uniform(3.0, 5.0), 1),
        #             description=f"A comfortable hotel located in {city.name}.",
        #             images=["",
        #                     "",
        #                     "",
        #                     "",
        #                     ""],
        #         )
        
        # Hotel.objects.create(
        #             name=hotel_name,
        #             city=City.objects.get(id=4), # Berlin
        #             address=f"{random.randint(1, 100)} {city.name} Street",
        #             rating=round(random.uniform(3.0, 5.0), 1),
        #             description=f"A comfortable hotel located in {city.name}.",
        #             images=["",
        #                     "",
        #                     "",
        #                     "",
        #                     ""],
        #         )
        
        # Hotel.objects.create(
        #             name=hotel_name,
        #             city=City.objects.get(id=4), # Berlin
        #             address=f"{random.randint(1, 100)} {city.name} Street",
        #             rating=round(random.uniform(3.0, 5.0), 1),
        #             description=f"A comfortable hotel located in {city.name}.",
        #             images=["",
        #                     "",
        #                     "",
        #                     "",
        #                     ""],
        #         )
        
        # Hotel.objects.create(
        #             name=hotel_name,
        #             city=City.objects.get(id=5), # Sydney
        #             address=f"{random.randint(1, 100)} {city.name} Street",
        #             rating=round(random.uniform(3.0, 5.0), 1),
        #             description=f"A comfortable hotel located in {city.name}.",
        #             images=["",
        #                     "",
        #                     "",
        #                     "",
        #                     ""],
        #         )
        
        # Hotel.objects.create(
        #             name=hotel_name,
        #             city=City.objects.get(id=5), # Sydney
        #             address=f"{random.randint(1, 100)} {city.name} Street",
        #             rating=round(random.uniform(3.0, 5.0), 1),
        #             description=f"A comfortable hotel located in {city.name}.",
        #             images=["",
        #                     "",
        #                     "",
        #                     "",
        #                     ""],
        #         )
        
        # Hotel.objects.create(
        #             name=hotel_name,
        #             city=City.objects.get(id=6), # Almaty
        #             address=f"{random.randint(1, 100)} {city.name} Street",
        #             rating=round(random.uniform(3.0, 5.0), 1),
        #             description=f"A comfortable hotel located in {city.name}.",
        #             images=["",
        #                     "",
        #                     "",
        #                     "",
        #                     ""],
        #         )
        
        # Hotel.objects.create(
        #             name=hotel_name,
        #             city=City.objects.get(id=6), # Almaty
        #             address=f"{random.randint(1, 100)} {city.name} Street",
        #             rating=round(random.uniform(3.0, 5.0), 1),
        #             description=f"A comfortable hotel located in {city.name}.",
        #             images=["",
        #                     "",
        #                     "",
        #                     "",
        #                     ""],
        #         )
        
        # Hotel.objects.create(
        #             name=hotel_name,
        #             city=City.objects.get(id=7), # Astana
        #             address=f"{random.randint(1, 100)} {city.name} Street",
        #             rating=round(random.uniform(3.0, 5.0), 1),
        #             description=f"A comfortable hotel located in {city.name}.",
        #             images=["",
        #                     "",
        #                     "",
        #                     "",
        #                     ""],
        #         )
        
        # Hotel.objects.create(
        #             name=hotel_name,
        #             city=City.objects.get(id=7), # Astana
        #             address=f"{random.randint(1, 100)} {city.name} Street",
        #             rating=round(random.uniform(3.0, 5.0), 1),
        #             description=f"A comfortable hotel located in {city.name}.",
        #             images=["",
        #                     "",
        #                     "",
        #                     "",
        #                     ""],
        #         )
        
        # Hotel.objects.create(
        #             name=hotel_name,
        #             city=City.objects.get(id=8), #Istanbul
        #             address=f"{random.randint(1, 100)} {city.name} Street",
        #             rating=round(random.uniform(3.0, 5.0), 1),
        #             description=f"A comfortable hotel located in {city.name}.",
        #             images=["",
        #                     "",
        #                     "",
        #                     "",
        #                     ""],
        #         )
        
        # Hotel.objects.create(
        #             name=hotel_name,
        #             city=City.objects.get(id=8), #Istanbul
        #             address=f"{random.randint(1, 100)} {city.name} Street",
        #             rating=round(random.uniform(3.0, 5.0), 1),
        #             description=f"A comfortable hotel located in {city.name}.",
        #             images=["",
        #                     "",
        #                     "",
        #                     "",
        #                     ""],
        #         )
        
        # Hotel.objects.create(
        #             name=hotel_name,
        #             city=City.objects.get(id=9), #Doha
        #             address=f"{random.randint(1, 100)} {city.name} Street",
        #             rating=round(random.uniform(3.0, 5.0), 1),
        #             description=f"A comfortable hotel located in {city.name}.",
        #             images=["",
        #                     "",
        #                     "",
        #                     "",
        #                     ""],
        #         )
        
        # Hotel.objects.create(
        #             name=hotel_name,
        #             city=City.objects.get(id=9), #Doha
        #             address=f"{random.randint(1, 100)} {city.name} Street",
        #             rating=round(random.uniform(3.0, 5.0), 1),
        #             description=f"A comfortable hotel located in {city.name}.",
        #             images=["",
        #                     "",
        #                     "",
        #                     "",
        #                     ""],
        #         )
        
        # Hotel.objects.create(
        #             name=hotel_name,
        #             city=City.objects.get(id=10), #Dubai
        #             address=f"{random.randint(1, 100)} {city.name} Street",
        #             rating=round(random.uniform(3.0, 5.0), 1),
        #             description=f"A comfortable hotel located in {city.name}.",
        #             images=["",
        #                     "",
        #                     "",
        #                     "",
        #                     ""],
        #         )
        
        # Hotel.objects.create(
        #             name=hotel_name,
        #             city=City.objects.get(id=10), #Dubai
        #             address=f"{random.randint(1, 100)} {city.name} Street",
        #             rating=round(random.uniform(3.0, 5.0), 1),
        #             description=f"A comfortable hotel located in {city.name}.",
        #             images=["",
        #                     "",
        #                     "",
        #                     "",
        #                     ""],
        #         )

       
        self.stdout.write(self.style.SUCCESS("All hotels created successfully."))
