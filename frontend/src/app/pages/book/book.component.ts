import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { NavbarComponent } from '../../components/navbar/navbar.component';
import { TourService } from '../../services/tour.service';
import { Application } from '../../models/tour.model';

@Component({
  selector: 'app-book',
  standalone: true,
  imports: [CommonModule, FormsModule, NavbarComponent],
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
  showCustomAlert: boolean = false;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private tourService: TourService
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
    const application: Application = {
      id: 0, // will be set by the backend
      name: this.bookingData.name,
      phone: this.bookingData.phone,
      email: this.bookingData.email,
      tour: this.tour.id, // only tour id
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
      total_price: this.total_price,
      status: 'new',
      created_at: new Date(),
      updated_at: new Date(),
    };

    //console.log('Application Payload:', application);

    this.tourService.createApplication(application).subscribe({
      next: () => {
        this.success = 'Thank you for booking with us!';
        this.error = '';
        this.bookingData = { name: '', phone: '', email: '' };

        this.showCustomAlert = true;
      },
      error: (err) => {
        console.error(err);
        this.error = 'Failed to book tour. Try again later.';
        this.success = '';
      },
    });
  }

  closeCustomAlert(): void {
    this.showCustomAlert = false;
    this.router.navigate(['/']);
  }
}
