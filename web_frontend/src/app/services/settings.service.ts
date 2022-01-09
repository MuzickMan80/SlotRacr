import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { catchError, map, tap } from "rxjs/operators";
import { environment } from "src/environments/environment";

export interface Setting {
    type: string;
    name: string;
    default: any;
    description: string;
    value: any;
    group: string;
}

export type Settings = [string, Setting][]
export class SettingsMap extends Map<string, Setting> {}
export type BackendSettings = {[name: string]: Setting}

@Injectable({
    providedIn: 'root'
  })
export class SettingsService {
    constructor (private http: HttpClient) {
    }

    getSettings(path: string): Observable<SettingsMap> {
        console.log("Get settings");
        return this.http.get<BackendSettings>(`${environment.api_url}/settings/${path}`)
            .pipe(
                map((d) => new SettingsMap(Object.entries(d))),
                tap((d) => d.forEach(element => {element.group = path})),
                catchError(this.handleError([]))
            )
    }

    setSetting(group: string, key: string, value: any): Observable<any> {
        return this.http.put<any>(`${environment.api_url}/settings/${group}/${key}/${value}`,value)
            .pipe(
                catchError(this.handleError(''))
            )
    }

    getRaceSettings() : Observable<SettingsMap> {
        return this.getSettings('race');
    }

    getPitSettings() : Observable<SettingsMap> {
        return this.getSettings('pit');
    }

    handleError<T>(response: T) : (e: any) => T {
        return (e: any) => {
            console.log(e);
            return response;
        }
    }
}