import { Injectable } from '@angular/core';
import {
  HttpEvent,
  HttpHandler,
  HttpInterceptor,
  HttpRequest,
  HttpErrorResponse,
} from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, switchMap } from 'rxjs/operators';
import { AuthService } from '../services/auth.service';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  constructor(private authService: AuthService) {}

  intercept(
    req: HttpRequest<any>,
    next: HttpHandler
  ): Observable<HttpEvent<any>> {
    //console.log('Interceptor triggered for URL:', req.url);

    const token = localStorage.getItem('token');
    let authReq = req;

    if (token && !req.url.includes('/login') && !req.url.includes('/refresh')) {
      authReq = req.clone({
        setHeaders: {
          Authorization: `Bearer ${token}`,
        },
      });
      //console.log('AuthInterceptor: Added Authorization header', authReq);
    }

    return next.handle(authReq).pipe(
      catchError((error: HttpErrorResponse) => {
        //console.error('AuthInterceptor: Error occurred', error);
        if (error.status === 401) {
          const refreshToken = localStorage.getItem('refresh');
          if (refreshToken) {
            return this.authService.refreshToken(refreshToken).pipe(
              switchMap((res) => {
                localStorage.setItem('token', res.access);
                const newAuthReq = req.clone({
                  setHeaders: {
                    Authorization: `Bearer ${res.access}`,
                  },
                });
                return next.handle(newAuthReq);
              }),
              catchError((refreshError) => {
                localStorage.removeItem('token');
                localStorage.removeItem('refresh');
                window.location.href = '/login';
                return throwError(refreshError);
              })
            );
          } else {
            localStorage.removeItem('token');
            localStorage.removeItem('refresh');
            window.location.href = '/login';
          }
        }
        return throwError(error);
      })
    );
  }
}
