import { Component, OnInit } from '@angular/core';
import { TourService } from '../../services/tour.service';
import { Tour } from '../../models/tour.model';
import { RouterModule, Router } from '@angular/router';
import { CommonModule } from '@angular/common';
import { NavbarComponent } from '../../components/navbar/navbar.component';

@Component({
  standalone: true,
  selector: 'app-tour-list',
  templateUrl: './tour-list.component.html',
  styleUrls: ['./tour-list.component.css'],
  imports: [RouterModule, CommonModule, NavbarComponent],
})
export class TourListComponent implements OnInit {
  tours: Tour[] = []; // Initialize tours as an empty array

  constructor(private tourService: TourService, private router: Router) {}

  ngOnInit(): void {
    this.tourService.getTours().subscribe({
      next: (data) => {
        console.log('Tours data received:', data); // Debug log
        this.tours = data;
      },
      error: (err) => {
        console.error('Error loading tours:', err);
      },
    });
  }

  viewDetails(tourId: number | undefined): void {
    if (tourId !== undefined) {
      this.router.navigate(['/tours', tourId]);
    } else {
      console.error('Invalid tour ID:', tourId);
    }
  }
}
