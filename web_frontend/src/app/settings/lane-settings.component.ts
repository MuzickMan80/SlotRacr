import { Component } from "@angular/core";
import { Observable } from "rxjs";
import { map, tap } from "rxjs/operators";
import { LaneSettingsMap, SettingsMap, SettingsService } from "../services/settings.service";
import { SettingBase } from "./setting-base";
import { SettingsFactory } from "./setting-factory";

@Component({
    selector: 'app-lane-settings',
    template: `
      <div class="settings-container">
        <h2>Lane Settings</h2>
        <div *ngIf="(setting$ | async)">
            <div *ngFor="let lane of settings | keyvalue">
            <h3>{{ lane.key }}</h3>
            <app-settings [settings]="lane.value"></app-settings>
            </div>
        </div>
      </div>`,
      styles: ['.settings-container { background-color: white; }']
  })
  export class LaneSettingsComponent {
    setting$: Observable<Map<string,SettingBase[]>>;
    settings: Map<string,SettingBase[]> | null = new Map<string,SettingBase[]>();
  
    constructor(private service: SettingsService) {
      this.setting$ = this.service.getLaneSettings()
        .pipe(
          map((d: LaneSettingsMap) =>  this.getLaneSettings(d)),
          tap((d) => this.settings = d)
        );
    }

    getLaneSettings(laneSettings: LaneSettingsMap): Map<string,SettingBase[]> {
      return new Map<string,SettingBase[]>(
        Array.from(laneSettings.entries()).map(([k,v])=>[k,this.getSettings(k,v)])
        );
    }
    getSettings(lane: string, settings: SettingsMap): SettingBase[] {
      return Array.from(settings.entries()).map(([k,v]) => SettingsFactory.Create(k,v))
    }
  }