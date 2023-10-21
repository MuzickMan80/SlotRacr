import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { LaneTableComponent } from '../lane-table/lane-table.component';
import { RaceSettingsComponent } from '../settings/race-settings.component';
import { PitSettingsComponent } from '../settings/pit-settings.component';
import { LaneSettingsComponent } from '../settings/lane-settings.component';
import { RegistrationComponent } from '../settings/registration/registration.component';
import { RaceManagerComponent } from '../race-manager/race-manager.component';
import { TrackTestingComponent } from '../track-testing/track-testing.component';

const routes: Routes = [
  { path: 'home', component: LaneTableComponent},
  { path: 'race-settings', component: RaceSettingsComponent},
  { path: 'pit-settings', component: PitSettingsComponent},
  { path: 'lane-settings', component: LaneSettingsComponent},
  { path: 'track-test', component: TrackTestingComponent},
  { path: 'race-manager', component: RaceManagerComponent},
  { path: 'badge-manager', component: RegistrationComponent},
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
