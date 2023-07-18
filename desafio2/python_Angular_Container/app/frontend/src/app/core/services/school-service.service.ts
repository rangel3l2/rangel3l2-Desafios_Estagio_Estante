import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { catchError, Observable, throwError } from 'rxjs';
import { School } from '../models/school';
import { API_CONFIG } from '../config/config';
@Injectable({
  providedIn: 'root'
})
export class SchoolServiceService {
  baseUrl = API_CONFIG.baseUrl
  constructor(private http: HttpClient) {}
  save(school: School) :Observable<School>{
    console.log('clicou')
    return this.http.post<School>(this.baseUrl, school, {
       headers: new HttpHeaders({
        'Content-Type': 'application/json'
       })
    })
    .pipe(catchError(this.handleError));
  }
  private handleError(errorResponse: HttpErrorResponse){
    if(errorResponse.error instanceof ErrorEvent){
      console.error('Client Side Error: ',errorResponse.error.message);

    }
    else{
      console.error('Serve Side Error: ', errorResponse);
    }
    return throwError(()=>'There is a problem with the service. We are notified & working on it. Please try again later.')
    }
  getSchoolFile(): Observable<School>{
    return this.http.get<School>(this.baseUrl,{
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
      
    })
    .pipe(catchError(this.handleError));
  }

} 
  
  

