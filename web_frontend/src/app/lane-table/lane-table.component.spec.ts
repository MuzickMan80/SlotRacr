import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LaneTableComponent } from './lane-table.component';

describe('LaneTableComponent', () => {
  let component: LaneTableComponent;
  let fixture: ComponentFixture<LaneTableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LaneTableComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LaneTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
