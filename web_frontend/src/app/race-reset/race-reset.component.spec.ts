import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RaceResetComponent } from './race-reset.component';

describe('RaceResetComponent', () => {
  let component: RaceResetComponent;
  let fixture: ComponentFixture<RaceResetComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RaceResetComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RaceResetComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
