import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-requests',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './requests.component.html',
  styleUrls: ['./requests.component.css']
})
export class RequestsComponent implements OnInit {
  requests: any[] = [];

  constructor(private http: HttpClient) {}

  ngOnInit() {
    const token = localStorage.getItem('token');
    if (token) {
      this.http.get('http://localhost:8000/api/custom-requests/', {
        headers: { Authorization: `Bearer ${token}` }
      }).subscribe((data: any) => {
        this.requests = data;
      });
    }
  }

  updateRequest(id: number, field: string, value: string) {
    const token = localStorage.getItem('token');
    if (token) {
      this.http.patch(`http://localhost:8000/api/custom-requests/${id}/`, { [field]: value }, {
        headers: { Authorization: `Bearer ${token}` }
      }).subscribe();
    }
  }
}
