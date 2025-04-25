import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { NavbarComponent } from '../../components/navbar/navbar.component';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, FormsModule, NavbarComponent],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent {
  username = '';
  password = '';
  error = '';

  constructor(private authService: AuthService, private router: Router) {}

  login() {
    this.authService.login(this.username, this.password).subscribe({
      next: (res) => {
        console.log('Login success:', res);
        localStorage.setItem('token', res.access);
        localStorage.setItem('refresh', res.refresh);
        this.router.navigate(['/requests']);
      },
      error: (err) => {
        console.error('Login error:', err);
        this.error = err.error?.detail || 'Invalid credentials';
      },
    });
  }
}
