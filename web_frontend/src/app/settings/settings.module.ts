import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';
import { MatSlideToggleModule } from '@angular/material/slide-toggle';
import { MatButtonModule } from '@angular/material/button';
import { SettingComponent } from './setting.component';
import { SettingsComponent } from './settings.component';
import { RaceSettingsComponent } from './race-settings.component';
import { FlexLayoutModule } from '@angular/flex-layout';
import { PitSettingsComponent } from './pit-settings.component';
import { LaneSettingsComponent } from './lane-settings.component';

@NgModule({
  declarations: [
    SettingsComponent,
    SettingComponent,
    RaceSettingsComponent,
    PitSettingsComponent,
    LaneSettingsComponent
  ],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    MatSlideToggleModule,
    MatButtonModule,
    FlexLayoutModule
  ]
})
export class SettingsModule { }
