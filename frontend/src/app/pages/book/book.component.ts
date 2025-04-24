import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-book',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './book.component.html',
  styleUrls: ['./book.component.css']
})
export class BookComponent implements OnInit {
  bookingData = {
    name: '',
    phone: '',
    email: ''
  };

  success = '';
  error = '';
  tourId!: number;
  tour: any = null;
  selectedFlightTo: any = null;
  selectedFlightBack: any = null;

  constructor(
    private http: HttpClient,
    private route: ActivatedRoute,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.tourId = Number(this.route.snapshot.paramMap.get('id'));

    const tourData = localStorage.getItem('tourDetails');
    if (tourData) {
      const parsed = JSON.parse(tourData);
      this.tour = parsed.tour;
      this.selectedFlightTo = parsed.selectedFlightTo || parsed.connectionTo;
      this.selectedFlightBack = parsed.selectedFlightBack || parsed.connectionBack;
    }
  }

  submitBooking(): void {
    const getFlightIds = (flight: any): number[] => {
      if (!flight) return [];
      if (flight.id) return [flight.id]; // обычный прямой рейс
      if (flight.firstLeg && flight.secondLeg) {
        return [flight.firstLeg.id, flight.secondLeg.id]; // connecting flight
      }
      return [];
    };
  
    const payload = {
      name: this.bookingData.name,
      phone: this.bookingData.phone,
      email: this.bookingData.email,
      tour: this.tourId,
      flights_to: getFlightIds(this.selectedFlightTo),
      flights_back: getFlightIds(this.selectedFlightBack)
    };
  
    this.http.post('/api/applications/', payload).subscribe({
      next: () => {
        this.success = 'Thank you for booking with us!';
        this.error = '';
        this.bookingData = { name: '', phone: '', email: '' };
      },
      error: (err) => {
        console.error(err);
        this.error = 'Failed to book tour. Try again later.';
        this.success = '';
      }
    });
  }
  
}
