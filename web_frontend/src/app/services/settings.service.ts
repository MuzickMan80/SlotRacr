import { HttpClient, HttpHeaders } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { catchError, filter, map, tap } from "rxjs/operators";
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
export class LaneSettingsMap extends Map<string, SettingsMap> {}
export type BackendSettings = {[name: string]: Setting}
export type BackendLaneSettings = {[name: string]: BackendSettings}

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
                map((d: BackendSettings) => this.convertSettings(path, d)),
                catchError(this.handleError([]))
            )
    }

    convertSettings(group: string, backend: BackendSettings): SettingsMap {
        var s = new SettingsMap(Object.entries(backend));
        s.forEach((setting) => { setting.group = group });
        return s;            
    }

    setSetting(group: string, key: string, value: any): Observable<any> {
        
    const httpOptions = {
        headers: new HttpHeaders({
        'Content-Type':  'application/json'
        })
    };
    return this.http.put<any>(`${environment.api_url}/settings/${group}/${key}/value`,JSON.stringify(value),httpOptions)
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

    getLaneSettings() : Observable<LaneSettingsMap> {
        console.log("Get settings");
        return this.http.get<BackendLaneSettings>(`${environment.api_url}/settings`)
            .pipe(
                map((groups) => this.convertLaneSettings(groups)),
                catchError(this.handleError([]))
            );
    }

    convertLaneSettings(laneSettings: BackendLaneSettings): LaneSettingsMap {
        return new LaneSettingsMap(
            Object.entries(laneSettings)
                .filter(([groupName, _]) => groupName.startsWith("lane"))
                .map(([groupName, s]) => [groupName, this.convertSettings(groupName, s)])
        )
    }

    handleError<T>(response: T) : (e: any) => T {
        return (e: any) => {
            console.log(e);
            return response;
        }
    }
}