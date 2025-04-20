export interface Country {
    id: number;
    name: string;
    image: string;
  }
  
  export interface City {
    id: number;
    name: string;
    country: Country;
    images: string[];
  }
  
  export interface MealType {
    id: number;
    type: string;
    description: string;
  }
  
  export interface Flight {
    id: number;
    airline: string;
    flight_number: string;
    departure: Date;
    arrival: Date;
    origin: City;
    destination: City;
    prcie: number;
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
    duration: number;
    price: number;
    hotel: Hotel;
    meal_type: MealType;
    is_active: boolean;
  }
  