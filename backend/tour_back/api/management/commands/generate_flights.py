from django.core.management.base import BaseCommand
from api.models import City, Flight
from django.utils import timezone
import random
from datetime import timedelta, datetime


class Command(BaseCommand):
    help = 'Generate realistic round-trip and connecting flights between cities with prices and schedules until the end of the year'

    def handle(self, *args, **kwargs):
        cities = list(City.objects.all())
        airlines = [
            {"name": "Air Astana", "icon": "https://ir.airastana.com/media/nihfojzd/logo-01-2x.png", "days": [0, 1, 2, 4, 5]},
            {"name": "Emirates", "icon": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Emirates_logo.svg/1200px-Emirates_logo.svg.png", "days": [0, 1, 2, 3, 4, 5, 6]},
            {"name": "FlyDubai", "icon": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKoxkOBG9bbrcSZDosb8Aa6ZQeXPKDM4v3Ew&s", "days": [[0, 1, 2, 3, 4, 5, 6]]},
            {"name": "Turkish Airlines", "icon": "https://logowik.com/content/uploads/images/thy-turkish-airlines-new6886.jpg", "days": [0, 1, 2, 3, 4, 5, 6]},
            {"name": "Lufthansa", "icon": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTeOHLVuw7CBlCocxdWz6Nd8x2kzsSujChgFQ&s", "days": [0, 1, 3, 5]},
            {"name": "Qatar Airways", "icon": "https://d21buns5ku92am.cloudfront.net/69647/images/433143-QR%20Logo%20Horizontal%20White-6a70c4-medium-1654772384.png", "days": [0, 1, 2, 3, 4, 5, 6]},
            {"name": "British Airways", "icon": "https://mediacentre.britishairways.com/contents/archives/216/86/images/thumb1280x1683_width/britishairways_216861253015751_thumb.jpg", "days": [1, 3, 5]},
            {"name": "Air France", "icon": "https://download.logo.wine/logo/Air_France/Air_France-Logo.wine.png", "days": [0, 2, 4, 6]},
            {"name": "KLM", "icon": "https://1000logos.net/wp-content/uploads/2021/03/KLM-logo.jpg", "days": [0, 2, 4, 6]},
        ]

        realistic_routes = {
            "Kazakhstan": ["Turkey", "UAE", "Germany", "Qatar", "Kazakhstan"],
            "Turkey": ["Kazakhstan", "UAE", "Germany", "France", "Qatar", "USA", "Canada"],
            "UAE": ["Kazakhstan", "Turkey", "Qatar", "Germany", "France", "USA", "Canada", "Australia"],
            "Germany": ["Kazakhstan", "Turkey", "France", "USA", "UAE", "Qatar", "Canada", "Australia"],
            "France": ["Germany", "USA", "Canada", "Turkey", "UAE", "Qatar"],
            "USA": ["France", "Canada", "Germany", "UAE", "Turkey", "Qatar"],
            "Canada": ["USA", "France", "Germany", "UAE", "Turkey", "Qatar"],
            "Qatar": ["Kazakhstan", "Turkey", "UAE", "Germany", "France", "USA", "Canada", "Australia"],
            "Australia": ["UAE", "Germany", "Qatar"],
        }

        today = timezone.now().date()
        end_of_year = datetime(today.year, 9, 30).date()

        for origin in cities:
            for destination in cities:
                if origin == destination:
                    continue

                if origin.country.name not in realistic_routes or destination.country.name not in realistic_routes[origin.country.name]:
                    continue

                for airline in airlines:
                    current_date = today
                    while current_date <= end_of_year:
                        if current_date.weekday() in airline["days"]:
                            for _ in range(random.randint(1, 3)):
                                departure_time = timezone.now().replace(hour=random.randint(6, 22), minute=0, second=0, microsecond=0)
                                departure = timezone.make_aware(datetime.combine(current_date, departure_time.time()))
                                arrival = departure + timedelta(hours=random.randint(3, 12))
                                price = random.randint(100, 1000)

                                random_digits = f"{random.randint(1, 9999):04}"
                                Flight.objects.create(
                                    airline=airline["name"],
                                    flight_number=f"{airline['name'][:2].upper()}{random_digits}",
                                    departure=departure,
                                    arrival=arrival,
                                    origin=origin,
                                    destination=destination,
                                    icon=airline["icon"],
                                    price=price
                                )

                                # Generate return flight
                                return_departure = arrival + timedelta(days=random.randint(1, 7))
                                return_arrival = return_departure + timedelta(hours=random.randint(3, 12))
                                return_price = random.randint(100, 1000)
                                random_digits_return = f"{random.randint(1, 9999):04}"  # Случайное число с ведущими нулями для обратного рейса
                                Flight.objects.create(
                                    airline=airline["name"],
                                    flight_number=f"{airline['name'][:2].upper()}{random_digits_return}",  # Уникальный номер с 4 цифрами
                                    departure=return_departure,
                                    arrival=return_arrival,
                                    origin=destination,
                                    destination=origin,
                                    icon=airline["icon"],
                                    price=return_price
                                )

                        current_date += timedelta(days=1)

        self.stdout.write(self.style.SUCCESS('Successfully generated flights until the end of the year!'))
