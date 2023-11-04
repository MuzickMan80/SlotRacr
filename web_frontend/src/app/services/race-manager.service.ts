import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { environment } from 'src/environments/environment';
import { WebsocketService } from './websocket.service';

@Injectable({
  providedIn: 'root'
})
export class RaceManagerService {
  
  constructor(private wsService: WebsocketService, private http: HttpClient) {
  }

  
  getAccident(lane: number): Observable<boolean> {
    return this.http.get<boolean>(`${environment.api_url}/race/lane/${lane}/accident`)
        .pipe(
            catchError(this.handleError([]))
        )
  }

  setAccident(lane: number, value: boolean): Observable<string> {      
      const httpOptions = {
          headers: new HttpHeaders({
          'Content-Type':  'application/json'
          })
      };
      return this.http.put<string>(`${environment.api_url}/race/lane/${lane}/accident`,JSON.stringify(value),httpOptions)
          .pipe(
              catchError(this.handleError(''))
          )
  }

  reset(): Observable<string> {
    const httpOptions = {
        headers: new HttpHeaders({
        'Content-Type':  'application/json'
        })
    };
    return this.http.post<string>(`${environment.api_url}/race/reset`,JSON.stringify(""),httpOptions)
    .pipe(
        catchError(this.handleError(''))
    )
  }
 
  handleError<T>(response: T) : (e: any) => T {
    return (e: any) => {
        console.log(e);
        return response;
    }
}

}
