import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NavbarComponent } from '../../components/navbar/navbar.component';
import { TourService } from '../../services/tour.service';
import { CustomRequest } from '../../models/tour.model';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-requests',
  standalone: true,
  imports: [CommonModule, NavbarComponent],
  templateUrl: './requests.component.html',
  styleUrls: ['./requests.component.css'],
})
export class RequestsComponent implements OnInit {
  requests: CustomRequest[] = [];
  error = '';
  isAuthenticated = false;

  constructor(
    private tourService: TourService,
    private authService: AuthService
  ) {}

  ngOnInit(): void {
    this.isAuthenticated = this.authService.isAuthenticated();
    console.log('Token from localStorage:', localStorage.getItem('token'));
    if (!this.isAuthenticated) {
      return;
    }
    this.fetchRequests();
  }

  fetchRequests(): void {
    this.tourService.getCustomRequestList().subscribe({
      next: (data) => {
        this.requests = data;
      },
      error: (err) => {
        console.error(err);
        this.error = 'Failed to fetch requests. Please try again later.';
      },
    });
  }
}
