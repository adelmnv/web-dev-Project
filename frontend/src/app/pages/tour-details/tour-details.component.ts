import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CommonModule } from '@angular/common';
import { TourService } from '../../services/tour.service';
import { Flight, Tour } from '../../models/tour.model';
import { NgFor } from '@angular/common';
import { RouterModule, Router } from '@angular/router';
import { NavbarComponent } from '../../components/navbar/navbar.component';

@Component({
  standalone: true,
  selector: 'app-tour-details',
  templateUrl: './tour-details.component.html',
  styleUrls: ['./tour-details.component.css'],
  imports: [CommonModule, RouterModule, NavbarComponent],
})
export class TourDetailsComponent implements OnInit {
  tour!: Tour | undefined;
  currentImageIndex: number = 0;
  flightsTo: Flight[] = [];
  flightsBack: Flight[] = [];
  flightPairs: { to: Flight; back: Flight }[] = [];
  selectedFlightPair: { to: Flight; back: Flight } | null = null;

  constructor(
    private route: ActivatedRoute,
    private tourService: TourService,
    private router: Router
  ) {}

  ngOnInit(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.tourService.getTourById(id).subscribe((tour) => {
      this.tour = tour;
      console.log('Tour details:', this.tour); // Debug log

      // Default values for testing
      const originId = 4; // Default origin city ID
      const destinationId = this.tour?.hotel?.city?.id || 0; // Destination city ID from the tour
      const departureDate = '2025-04-30'; // Default departure date
      const returnDate = '2025-05-07';   // Default return date
      console.log(returnDate); // Debug log

      if (destinationId) {
        this.tourService
          .findFlights(originId, destinationId, departureDate, returnDate)
          .subscribe((flights) => {
            this.flightsTo = flights.flights_to;
            this.flightsBack = flights.flights_back;
            this.pairFlights();
          });
      }
    });
  }

  pairFlights(): void {
    this.flightPairs = [];
    for (const to of this.flightsTo) {
      for (const back of this.flightsBack) {
        this.flightPairs.push({ to, back });
      }
    }
  }

  selectFlightPair(flightPair: { to: Flight; back: Flight }): void {
    this.selectedFlightPair = flightPair;
    console.log('Selected flight pair:', flightPair);
  }

  goBack(): void {
    history.back();
  }

  get images(): string[] {
    const hotelImages = this.tour?.hotel?.images || [];
    const cityImage = this.tour?.hotel?.city?.images || [];
    return [...hotelImages, ...cityImage];
  }

  nextImage(): void {
    if (this.images.length > 0) {
      this.currentImageIndex =
        (this.currentImageIndex + 1) % this.images.length;
    }
  }

  previousImage(): void {
    if (this.images.length > 0) {
      this.currentImageIndex =
        (this.currentImageIndex - 1 + this.images.length) % this.images.length;
    }
  }
  
}
