import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CommonModule } from '@angular/common';
import { TourService } from '../../services/tour.service';
import { Tour } from '../../models/tour.model';
import { NgFor } from '@angular/common';
import { RouterModule, Router } from '@angular/router';

@Component({
  standalone: true,
  selector: 'app-tour-details',
  templateUrl: './tour-details.component.html',
  styleUrls: ['./tour-details.component.css'],
  imports: [CommonModule,RouterModule]
})
export class TourDetailsComponent implements OnInit {
  tour!: Tour | undefined;
  currentImageIndex: number = 0;
  

  constructor(private route: ActivatedRoute, 
    private tourService: TourService,
    private router: Router) {}

  ngOnInit(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.tourService.getTours().subscribe(tours => {
      this.tour = tours.find(t => t.id === id);
    });
  }
  goBack(): void {
    history.back();
  }
  get images() {
    return this.tour && this.tour.images && this.tour.images.length > 0 ? this.tour.images : [];
  }

  nextImage() {
    if (this.images.length > 0) {
      this.currentImageIndex = (this.currentImageIndex + 1) % this.images.length;
    }
  }

  previousImage() {
    if (this.images.length > 0) {
      this.currentImageIndex = (this.currentImageIndex - 1 + this.images.length) % this.images.length;
    }
  }
}
