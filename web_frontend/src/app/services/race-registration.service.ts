import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { catchError, map } from 'rxjs/operators';
import { environment } from 'src/environments/environment';
import { WebsocketService } from './websocket.service';

export interface BadgeInfo {
    name: string;
    badge: string;
}

interface RegistrationInfo {
    badge: BadgeInfo[]
}

@Injectable({
  providedIn: 'root'
})

export class RaceRegistrationService {
  
  constructor(private http: HttpClient) {
  }
  
  getBadges(): Observable<BadgeInfo[]> {
    return this.http.get<RegistrationInfo>(`${environment.api_url}/registration`)
        .pipe(
            map(v => v.badge),
            catchError(this.handleError([]))
        )
  }

  setBadgeName(badgeId: string, name: string): Observable<string> {
    const httpOptions = {
        headers: new HttpHeaders({
        'Content-Type':  'application/json'
        })
    };
    return this.http.put<string>(`${environment.api_url}/registration/badge/${badgeId}/name`, JSON.stringify(name), httpOptions)
        .pipe(
            catchError(this.handleError([]))
        )
  }

  handleError<T>(response: T) : (e: any) => T {
    return (e: any) => {
        console.log(e);
        return response;
    }
  }
}
