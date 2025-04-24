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
  styleUrls: ['./book.component.css'],
})
export class BookComponent implements OnInit {
  bookingData = {
    name: '',
    phone: '',
    email: '',
  };

  success = '';
  error = '';
  tourId!: number;
  tour: any = null;
  selectedFlightTo: any = null;
  selectedFlightBack: any = null;
  total_price: number = 0;

  constructor(
    private http: HttpClient,
    private route: ActivatedRoute,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.tourId = Number(this.route.snapshot.paramMap.get('id'));

    const bookingData = localStorage.getItem('bookingDetails');
    if (bookingData) {
      const parsed = JSON.parse(bookingData);
      this.tour = parsed.tour;
      this.selectedFlightTo = parsed.selectedFlightTo || parsed.connectionTo;
      this.selectedFlightBack =
        parsed.selectedFlightBack || parsed.connectionBack;
      this.total_price = parsed.total_price || 0;
    }
  }

  submitBooking(): void {
    const payload = {
      name: this.bookingData.name,
      phone: this.bookingData.phone,
      email: this.bookingData.email,
      tour: this.tour.id,
      flights_to: this.selectedFlightTo.id
        ? [this.selectedFlightTo.id]
        : [
            this.selectedFlightTo.firstLeg.id,
            this.selectedFlightTo.secondLeg.id,
          ],
      flights_back: this.selectedFlightBack.id
        ? [this.selectedFlightBack.id]
        : [
            this.selectedFlightBack.firstLeg.id,
            this.selectedFlightBack.secondLeg.id,
          ],
    };

    console.log('Payload:', payload); // Debug log

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
      },
    });
  }
}
