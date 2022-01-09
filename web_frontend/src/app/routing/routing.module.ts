import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { LaneTableComponent } from '../lane-table/lane-table.component';
import { RaceSettingsComponent } from '../settings/race-settings.component';
import { PitSettingsComponent } from '../settings/pit-settings.component';

const routes: Routes = [
  { path: 'home', component: LaneTableComponent},
  { path: 'race-settings', component: RaceSettingsComponent},
  { path: 'pit-settings', component: PitSettingsComponent},
  { path: '', redirectTo: '/home', pathMatch: 'full'}
]

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    RouterModule.forRoot(routes)
  ],
  exports: [
    RouterModule
  ]
})
export class RoutingModule { }
