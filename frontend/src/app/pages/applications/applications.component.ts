import { Component, OnInit } from '@angular/core';
import { TourService } from '../../services/tour.service';
import { Application, Tour, Flight } from '../../models/tour.model';
import { CommonModule } from '@angular/common';
import { NavbarComponent } from '../../components/navbar/navbar.component';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-applications',
  standalone: true,
  imports: [CommonModule, NavbarComponent],
  templateUrl: './applications.component.html',
  styleUrls: ['./applications.component.css'],
})
export class ApplicationsComponent implements OnInit {
  applicationsNew: Application[] = [];
  applicationsPending: Application[] = [];
  applicationsProcessed: Application[] = [];
  selectedApplication: Application | null = null;
  selectedTour: Tour | null = null;
  selectedFlight: Flight | null = null;
  error = '';
  isAuthenticated = false;
  
  constructor(private tourService: TourService, private authService: AuthService) {}

  ngOnInit(): void {
    this.isAuthenticated = this.authService.isAuthenticated();
    if (!this.isAuthenticated) {
      return;
    }
    this.fetchApplications();
  }

  fetchApplications(): void {
    this.tourService.getApplicationList().subscribe({
      next: (applications) => {
        this.applicationsNew = applications.filter(
          (app) => app.status === 'new'
        );
        this.applicationsPending = applications.filter(
          (app) => app.status === 'pending'
        );
        this.applicationsProcessed = applications.filter(
          (app) => app.status === 'approved' || app.status === 'rejected'
        );
      },

      error: (err) => {
        console.error(err);
        this.error = 'Failed to fetch applications. Please try again later.';
      },
    });
  }

  updateStatus(application: Application, newStatus: string): void {
    const updatedApplication = { ...application, status: newStatus };

    this.tourService
      .updateApplication(updatedApplication.id, updatedApplication)
      .subscribe({
        next: () => {
          this.fetchApplications();
        },
        error: (err) => {
          console.error(err);
          this.error = 'Failed to update application status. Please try again.';
        },
      });
  }

  openTourDetails(tourId: number): void {
    this.tourService.getTourById(tourId).subscribe({
      next: (tour) => {
        this.selectedTour = tour;
      },
      error: (err) => {
        console.error(err);
        this.error = 'Failed to fetch tour details.';
      },
    });
  }

  closeTourDetails(): void {
    this.selectedTour = null;
  }

  openFlightDetails(flightId: number): void {
    this.tourService.getFlightById(flightId).subscribe({
      next: (flight) => {
        this.selectedFlight = flight;
      },
      error: (err) => {
        console.error(err);
        this.error = 'Failed to fetch flight details.';
      },
    });
  }

  closeFlightDetails(): void {
    this.selectedFlight = null;
  }
}
