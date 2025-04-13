import { bootstrapApplication } from '@angular/platform-browser';
import { provideRouter } from '@angular/router';

import { AppComponent } from './app/app.component';
import { HomeComponent } from './app/pages/home/home.component';
import { PopularToursComponent } from './app/components/popular-tours/popular-tours.component';
import { ReviewsComponent } from './app/components/reviews/reviews.component';

import { AboutComponent } from './app/pages/about/about.component';
import { ContactComponent } from './app/pages/contact/contact.component';

bootstrapApplication(AppComponent, {
  providers: [
    provideRouter([
      { path: '', component: HomeComponent },
      { path: 'tours', component: PopularToursComponent },
      { path: 'reviews', component: ReviewsComponent },
      { path: 'about', component: AboutComponent },
      { path: 'contact', component: ContactComponent },
      { path: '**', redirectTo: '' }
    ])
  ]
}).catch(err => console.error(err));
