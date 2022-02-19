import { Component } from "@angular/core";
import { Observable } from "rxjs";
import { map, tap } from "rxjs/operators";
import { SettingsService } from "../services/settings.service";
import { SettingBase } from "./setting-base";
import { SettingsFactory } from "./setting-factory";

@Component({
    selector: 'app-pit-settings',
    template: `
      <div class="settings-container">
        <h2>Pit Settings</h2>
        <div *ngIf="(setting$ | async)">
            <app-settings [settings]="settings"></app-settings>
        </div>
      </div>`,
    styles: ['.settings-container { background-color: white; }']
  })
  export class PitSettingsComponent {
    setting$: Observable<SettingBase[]>;
    settings: SettingBase[] | null = [];
  
    constructor(private service: SettingsService) {
      this.setting$ = this.service.getPitSettings()
        .pipe(
          map((d) => Array.from(d.entries()).map(([k,v]) => SettingsFactory.Create(k,v))),
          tap((d) => this.settings = d)
        );
    }
  }