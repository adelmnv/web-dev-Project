export interface Country {
    id: number;
    name: string;
    image: string;
  }
  
  export interface City {
    id: number;
    name: string;
    country: Country;
    image: string;
  }
  
  export interface MealType {
    id: number;
    type: string;
  }
  
  export interface Flight {
    id: number;
    airline: string;
    flight_number: string;
    departure: string;
    arrival: string;
    origin: City;
    destination: City;
    icon: string;
  }
  
  export interface Hotel {
    id: number;
    name: string;
    city: City;
    address: string;
    rating: number;
    description: string;
    images: string[];
  }
  
  export interface Tour {
    id: number;
    name: string;
    description: string;
    start_date: string;
    end_date: string;
    price: number;
    flight: Flight;
    hotel: Hotel;
    meal_type: MealType;
    is_active: boolean;
    images: string[];
  }
  