from django.core.management.base import BaseCommand
from api.models import City, Flight
from django.utils import timezone
import random
from datetime import timedelta


class Command(BaseCommand):
    help = 'Generate round-trip and connecting flights between all cities'

    def handle(self, *args, **kwargs):
        cities = list(City.objects.all())
        airlines = [
            {"name": "Air Astana", "icon": "https://ir.airastana.com/media/nihfojzd/logo-01-2x.png"},
            {"name": "Emirates", "icon": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Emirates_logo.svg/1200px-Emirates_logo.svg.png"},
            {"name": "FlyDubai", "icon": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKoxkOBG9bbrcSZDosb8Aa6ZQeXPKDM4v3Ew&s"},
            {"name": "Turkish Airlines", "icon": "https://logowik.com/content/uploads/images/thy-turkish-airlines-new6886.jpg"},
            {"name": "Lufthansa", "icon": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTeOHLVuw7CBlCocxdWz6Nd8x2kzsSujChgFQ&s"},
            {"name": "Qatar Airways", "icon": "https://d21buns5ku92am.cloudfront.net/69647/images/433143-QR%20Logo%20Horizontal%20White-6a70c4-medium-1654772384.png"},
            {"name": "British Airways", "icon": "https://mediacentre.britishairways.com/contents/archives/216/86/images/thumb1280x1683_width/britishairways_216861253015751_thumb.jpg"},
            {"name": "Air France", "icon": "https://download.logo.wine/logo/Air_France/Air_France-Logo.wine.png"},
            {"name": "KLM", "icon": "https://1000logos.net/wp-content/uploads/2021/03/KLM-logo.jpg"},
        ]

        flight_counter = 1000  # unique flight number start

        for origin in cities:
            for destination in cities:
                if origin == destination:
                    continue

                # Прямой рейс туда
                days_offset = random.randint(1, 10)
                departure = timezone.now() + timedelta(days=days_offset)
                arrival = departure + timedelta(hours=random.randint(3, 12))
                airline = random.choice(airlines)

                Flight.objects.create(
                    airline=airline["name"],
                    flight_number=f"{airline['name'][:2].upper()}{flight_counter}",
                    departure=departure,
                    arrival=arrival,
                    origin=origin,
                    destination=destination,
                    icon=airline["icon"]
                )
                flight_counter += 1

                # Обратный рейс
                return_departure = arrival + timedelta(days=random.randint(2, 10))
                return_arrival = return_departure + timedelta(hours=random.randint(3, 12))

                Flight.objects.create(
                    airline=airline["name"],
                    flight_number=f"{airline['name'][:2].upper()}{flight_counter}",
                    departure=return_departure,
                    arrival=return_arrival,
                    origin=destination,
                    destination=origin,
                    icon=airline["icon"]
                )
                flight_counter += 1

                # Пересадочный вариант (через другой город)
                connections = [c for c in cities if c != origin and c != destination]
                if connections:
                    layover_city = random.choice(connections)

                    leg1_dep = timezone.now() + timedelta(days=random.randint(1, 5))
                    leg1_arr = leg1_dep + timedelta(hours=random.randint(2, 6))
                    leg2_dep = leg1_arr + timedelta(hours=random.randint(2, 6))
                    leg2_arr = leg2_dep + timedelta(hours=random.randint(2, 6))

                    airline = random.choice(airlines)

                    Flight.objects.create(
                        airline=airline["name"],
                        flight_number=f"{airline['name'][:2].upper()}{flight_counter}",
                        departure=leg1_dep,
                        arrival=leg1_arr,
                        origin=origin,
                        destination=layover_city,
                        icon=airline["icon"]
                    )
                    flight_counter += 1

                    Flight.objects.create(
                        airline=airline["name"],
                        flight_number=f"{airline['name'][:2].upper()}{flight_counter}",
                        departure=leg2_dep,
                        arrival=leg2_arr,
                        origin=layover_city,
                        destination=destination,
                        icon=airline["icon"]
                    )
                    flight_counter += 1

        self.stdout.write(self.style.SUCCESS('Successfully generated flights!'))
