import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  username = '';
  password = '';
  error = '';

  constructor(private http: HttpClient, private router: Router) {}

  login() {
    console.log('🔐 Login clicked:', this.username, this.password);

    this.http.post('http://localhost:8000/api/login/', {
      username: this.username,
      password: this.password
    }).subscribe({
      next: (res: any) => {
        console.log('✅ Login success:', res);
        localStorage.setItem('token', res.access);
        this.router.navigate(['/requests']);
      },
      error: (err) => {
        console.error('❌ Login error:', err);
        this.error = err.error?.detail || 'Invalid credentials';
      }
    });
  }
}
