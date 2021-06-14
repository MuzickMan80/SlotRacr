import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FlexLayoutModule } from '@angular/flex-layout';
import { CdkTableModule } from '@angular/cdk/table';
import { LaneTableComponent } from './lane-table/lane-table.component';
import { RoutingModule } from './routing/routing.module';
import { LayoutComponent } from './layout/layout.component';
import { MatSidenavContent, MatSidenav} from '@angular/material/sidenav';

@NgModule({
  declarations: [
    AppComponent,
    LaneTableComponent,
    LayoutComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    FlexLayoutModule,
    CdkTableModule,
    RoutingModule,
    MatSidenavContent,
    MatSidenav
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
