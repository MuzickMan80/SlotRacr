import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FlexLayoutModule } from '@angular/flex-layout';
import { CdkTableModule } from '@angular/cdk/table';
import { LaneTableComponent } from './lane-table/lane-table.component';
import { RoutingModule } from './routing/routing.module';
import { LayoutComponent } from './layout/layout.component';
import { MatSidenavModule} from '@angular/material/sidenav';
import { NavigationComponent } from './navigation/navigation.component';
import { LayoutModule } from '@angular/cdk/layout';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatListModule } from '@angular/material/list';
import { MatButtonToggleModule } from '@angular/material/button-toggle';
import { HttpClientModule } from '@angular/common/http';
import { SettingsModule } from './settings/settings.module';
import { RaceManagerComponent } from './race-manager/race-manager.component';
import { TrackTestingComponent } from './track-testing/track-testing.component';
import { MatSlideToggleModule } from '@angular/material/slide-toggle';
import { RaceResetComponent } from './race-reset/race-reset.component';

@NgModule({
  declarations: [
    AppComponent,
    LaneTableComponent,
    LayoutComponent,
    NavigationComponent,
    RaceManagerComponent,
    TrackTestingComponent,
    RaceResetComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    FlexLayoutModule,
    CdkTableModule,
    RoutingModule,
    LayoutModule,
    MatToolbarModule,
    MatButtonModule,
    MatSidenavModule,
    MatIconModule,
    MatListModule,
    MatButtonToggleModule,
    MatSlideToggleModule,
    HttpClientModule,
    SettingsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
