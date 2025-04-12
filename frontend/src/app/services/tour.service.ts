import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { map } from 'rxjs/operators';
import { Tour, Country, City, MealType, Flight, Hotel } from '../models/tour.model';

@Injectable({
  providedIn: 'root'
})
export class TourService {
  // Database of countries
  private countries: Country[] = [
    { id: 1, name: 'France', image: 'https://images.unsplash.com/photo-1503917988258-f87a78e3c995' },
    { id: 2, name: 'Italy', image: 'https://images.unsplash.com/photo-1491562021826-11439dee0a7e' },
    { id: 3, name: 'Japan', image: 'https://images.unsplash.com/photo-1492571350019-22de08371fd3' }
  ];

  // Database of cities
  private cities: City[] = [
    { id: 1, name: 'Paris', country: this.countries[0], image: 'https://images.unsplash.com/photo-1431274172761-fca41d930114' },
    { id: 2, name: 'Nice', country: this.countries[0], image: 'https://images.unsplash.com/photo-1513635269975-59663e0ac1ad' },
    { id: 3, name: 'Rome', country: this.countries[1], image: 'https://images.unsplash.com/photo-1529260830199-42c24126f198' },
    { id: 4, name: 'Venice', country: this.countries[1], image: 'https://images.unsplash.com/photo-1514890547357-a9ee288728e0' },
    { id: 5, name: 'Tokyo', country: this.countries[2], image: 'https://images.unsplash.com/photo-1540959733332-eab4deabeeaf' },
    { id: 6, name: 'Kyoto', country: this.countries[2], image: 'https://images.unsplash.com/photo-1492571350019-22de08371fd3' }
  ];

  // Database of meal types
  private mealTypes: MealType[] = [
    { id: 1, type: 'Breakfast Only' },
    { id: 2, type: 'Half Board' },
    { id: 3, type: 'Full Board' },
    { id: 4, type: 'All Inclusive' }
  ];

  // Database of flights
  private flights: Flight[] = [
    {
      id: 1,
      airline: 'Air France',
      flight_number: 'AF123',
      departure: '08:00',
      arrival: '11:30',
      origin: this.cities[0], // Paris
      destination: this.cities[2], // Rome
      icon: 'https://logo.clearbit.com/airfrance.com'
    },
    {
      id: 2,
      airline: 'Lufthansa',
      flight_number: 'LH456',
      departure: '14:00',
      arrival: '08:00+1',
      origin: this.cities[2], // Rome
      destination: this.cities[4], // Tokyo
      icon: 'https://logo.clearbit.com/lufthansa.com'
    },
    {
      id: 3,
      airline: 'Japan Airlines',
      flight_number: 'JL789',
      departure: '10:30',
      arrival: '12:00',
      origin: this.cities[4], // Tokyo
      destination: this.cities[5], // Kyoto
      icon: 'https://logo.clearbit.com/jal.com'
    }
  ];

  // Database of hotels
  private hotels: Hotel[] = [
    {
      id: 1,
      name: 'Hôtel Plaza Athénée',
      city: this.cities[0], // Paris
      address: '25 Avenue Montaigne, 75008 Paris',
      rating: 5,
      description: 'Luxury hotel with views of the Eiffel Tower',
      images: [
        'https://images.unsplash.com/photo-1431274172761-fca41d930114',
        'https://images.unsplash.com/photo-1499856871958-5b9627545d1a',
        'https://images.unsplash.com/photo-1523531294919-4bcd7c65e216'
      ]
      
    },
    {
      id: 2,
      name: 'Hotel Negresco',
      city: this.cities[1], // Nice
      address: '37 Promenade des Anglais, 06000 Nice',
      rating: 4,
      description: 'Iconic beachfront hotel on the French Riviera',
      images: [
        'https://images.unsplash.com/photo-1431274172761-fca41d930114',
        'https://images.unsplash.com/photo-1499856871958-5b9627545d1a',
        'https://images.unsplash.com/photo-1523531294919-4bcd7c65e216'
      ]
    },
    {
      id: 3,
      name: 'Hotel Hassler Roma',
      city: this.cities[2], // Rome
      address: 'Piazza della Trinità dei Monti, 6, 00187 Roma',
      rating: 5,
      description: 'Luxury hotel at the top of the Spanish Steps',
      images: [
        'https://images.unsplash.com/photo-1431274172761-fca41d930114',
        'https://images.unsplash.com/photo-1499856871958-5b9627545d1a',
        'https://images.unsplash.com/photo-1523531294919-4bcd7c65e216'
      ]
    },
    {
      id: 4,
      name: 'The Ritz-Carlton, Tokyo',
      city: this.cities[4], // Tokyo
      address: 'Tokyo Midtown 9-7-1 Akasaka, Minato-ku, Tokyo 107-6245',
      rating: 5,
      description: 'High-rise luxury hotel with panoramic city views',
      images: [
        'https://images.unsplash.com/photo-1431274172761-fca41d930114',
        'https://images.unsplash.com/photo-1499856871958-5b9627545d1a',
        'https://images.unsplash.com/photo-1523531294919-4bcd7c65e216'
      ]
    }
  ];

  // Main tours database
  private tours: Tour[] = [
    {
      id: 1,
      name: 'Romantic Paris Getaway',
      description: '4-day luxury stay in Paris with Eiffel Tower views',
      start_date: '2023-06-15',
      end_date: '2023-06-19',
      price: 2500,
      flight: this.flights[0],
      hotel: this.hotels[0],
      meal_type: this.mealTypes[1],
      is_active: true,
      images: [
        'https://images.unsplash.com/photo-1431274172761-fca41d930114',
        'https://images.unsplash.com/photo-1499856871958-5b9627545d1a',
        'https://images.unsplash.com/photo-1523531294919-4bcd7c65e216'
      ]
    },
    {
      id: 2,
      name: 'Italian Cultural Journey',
      description: '7-day tour of Rome and Venice with guided historical tours',
      start_date: '2023-07-10',
      end_date: '2023-07-17',
      price: 3200,
      flight: this.flights[1],
      hotel: this.hotels[2],
      meal_type: this.mealTypes[2],
      is_active: true,
      images: [
        'https://images.unsplash.com/photo-1529260830199-42c24126f198',
        'https://images.unsplash.com/photo-1531572753322-ad063cecc140',
        'https://images.unsplash.com/photo-1552832230-c0197dd311b5'
      ]
    },
    {
      id: 3,
      name: 'Japanese Adventure',
      description: '10-day exploration of Tokyo and Kyoto with cultural experiences',
      start_date: '2023-09-01',
      end_date: '2023-09-11',
      price: 4500,
      flight: this.flights[2],
      hotel: this.hotels[3],
      meal_type: this.mealTypes[3],
      is_active: true,
      images: [
        'https://images.unsplash.com/photo-1540959733332-eab4deabeeaf',
        'https://images.unsplash.com/photo-1492571350019-22de08371fd3',
        'https://images.unsplash.com/photo-1491884662610-dfcd28f30cfb'
      ]
    },
    {
      id: 4,
      name: 'French Riviera Escape',
      description: '5-day relaxing stay in Nice with beach access',
      start_date: '2023-08-05',
      end_date: '2023-08-10',
      price: 1800,
      flight: this.flights[0],
      hotel: this.hotels[1],
      meal_type: this.mealTypes[0],
      is_active: true,
      images: [
        'https://images.unsplash.com/photo-1513635269975-59663e0ac1ad',
        'https://images.unsplash.com/photo-1503917988258-f87a78e3c995',
        'https://images.unsplash.com/photo-1520250497591-5f5bfd8aa9d3'
      ]
    }
  ];

  constructor() {
    console.log('TourService initialized with', this.tours.length, 'tours'); // Debug
  }

  getTours(): Observable<Tour[]> {
    return of(this.tours);
  }

  getTourById(id: number): Observable<Tour | undefined> {
    return of(this.tours.find(tour => tour.id === id));
  }

  // Additional useful methods
  getCountries(): Observable<Country[]> {
    return of(this.countries);
  }

  getCities(): Observable<City[]> {
    return of(this.cities);
  }

  getMealTypes(): Observable<MealType[]> {
    return of(this.mealTypes);
  }

  getToursByCountry(countryId: number): Observable<Tour[]> {
    return of(this.tours.filter(tour => 
      tour.hotel.city.country.id === countryId
    ));
  }

  getActiveTours(): Observable<Tour[]> {
    return of(this.tours.filter(tour => tour.is_active));
  }
}