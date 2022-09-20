import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TrackTestingComponent } from './track-testing.component';

describe('TrackTestingComponent', () => {
  let component: TrackTestingComponent;
  let fixture: ComponentFixture<TrackTestingComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TrackTestingComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TrackTestingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
