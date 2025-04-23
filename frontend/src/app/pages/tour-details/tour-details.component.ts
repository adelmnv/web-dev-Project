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
  connectingFlightsTo: { firstLeg: Flight; secondLeg: Flight }[] = [];
  flightsBack: Flight[] = [];
  connectingFlightsBack: { firstLeg: Flight; secondLeg: Flight }[] = [];
  selectedFlightPair: { to: Flight; back: Flight } | null = null;
  selectedFlightTo: Flight | { firstLeg: Flight; secondLeg: Flight } | null =
    null;
  selectedFlightBack: Flight | { firstLeg: Flight; secondLeg: Flight } | null =
    null;

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

      const originId = 5; // Default origin city ID
      const destinationId = this.tour?.hotel?.city?.id || 0; // Destination city ID from the tour
      const departureDate = '2025-04-30'; // Default departure date
      const returnDate = '2025-05-07'; // Default return date

      if (destinationId) {
        this.tourService
          .findFlights(originId, destinationId, departureDate, returnDate)
          .subscribe((flights) => {
            this.flightsTo = flights.flights_to || [];
            this.connectingFlightsTo = (
              flights.connecting_flights_to || []
            ).map((connection: any) => ({
              firstLeg: connection.first_leg,
              secondLeg: connection.second_leg,
            }));
            console.log(
              'Transformed Connecting Flights to:',
              this.connectingFlightsTo
            );

            this.flightsBack = flights.flights_back || [];
            this.connectingFlightsBack = (
              flights.connecting_flights_back || []
            ).map((connection: any) => ({
              firstLeg: connection.first_leg,
              secondLeg: connection.second_leg,
            }));
            console.log(
              'Transformed Connecting Flights back:',
              this.connectingFlightsBack
            );
          });
      }
    });
  }

  selectFlightPair(flightPair: { to: Flight; back: Flight }): void {
    this.selectedFlightPair = flightPair;
    console.log('Selected flight pair:', flightPair);
  }

  selectFlightTo(flight: Flight): void {
    this.selectedFlightTo = flight;
    console.log('Selected direct flight to:', flight);
  }

  selectConnectingFlightTo(connection: {
    firstLeg: Flight;
    secondLeg: Flight;
  }): void {
    this.selectedFlightTo = connection;
    console.log('Selected connecting flight to:', connection);
  }

  selectFlightBack(flight: Flight): void {
    this.selectedFlightBack = flight;
    console.log('Selected direct flight back:', flight);
  }

  selectConnectingFlightBack(connection: {
    firstLeg: Flight;
    secondLeg: Flight;
  }): void {
    this.selectedFlightBack = connection;
    console.log('Selected connecting flight back:', connection);
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
