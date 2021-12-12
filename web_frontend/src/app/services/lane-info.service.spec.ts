import { TestBed } from '@angular/core/testing';

import { LaneInfoService } from './lane-info.service';

describe('LaneInfoService', () => {
  let service: LaneInfoService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(LaneInfoService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
