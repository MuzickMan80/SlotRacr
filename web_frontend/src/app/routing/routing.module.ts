import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { LaneTableComponent } from '../lane-table/lane-table.component';
import { SettingsComponent } from '../settings/settings.component';

const routes: Routes = [
  { path: 'home', component: LaneTableComponent},
  { path: 'settings', component: SettingsComponent},
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
