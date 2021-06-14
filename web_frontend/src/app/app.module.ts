import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FlexLayoutModule } from '@angular/flex-layout';
import { CdkTableModule } from '@angular/cdk/table';
import { LaneTableComponent } from './lane-table/lane-table.component';
import { RoutingModule } from './routing/routing.module';

@NgModule({
  declarations: [
    AppComponent,
    LaneTableComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    FlexLayoutModule,
    CdkTableModule,
    RoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
