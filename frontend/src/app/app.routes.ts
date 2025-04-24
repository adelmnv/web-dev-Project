import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { AboutComponent } from './pages/about/about.component';
import { ContactComponent } from './pages/contact/contact.component';
import { TourListComponent } from './pages/tour-list/tour-list.component';
import { TourDetailsComponent } from './pages/tour-details/tour-details.component';
import { LoginComponent } from './pages/login/login.component';          
import { RequestsComponent } from './pages/requests/requests.component'; 
import { BookComponent } from './pages/book/book.component'; 

export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'home', component: HomeComponent },
  { path: 'about', component: AboutComponent },
  { path: 'contact', component: ContactComponent },
  { path: 'tours', component: TourListComponent },
  { path: 'tours/:id', component: TourDetailsComponent },
  { path: 'login', component: LoginComponent },      
  { path: 'requests', component: RequestsComponent }, 
  { path: 'book/:id', component: BookComponent }, 
];
