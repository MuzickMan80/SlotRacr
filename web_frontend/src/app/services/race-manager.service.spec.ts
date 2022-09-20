import { TestBed } from '@angular/core/testing';

import { RaceManagerService } from './race-manager.service';

describe('RaceManagerService', () => {
  let service: RaceManagerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(RaceManagerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
