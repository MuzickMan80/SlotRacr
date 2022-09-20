import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { LaneInfo, LaneInfoService } from '../services/lane-info.service';
import { RaceManagerService } from '../services/race-manager.service';

@Component({
  selector: 'app-race-manager',
  templateUrl: './race-manager.component.html',
  styleUrls: ['./race-manager.component.scss']
})
export class RaceManagerComponent implements OnInit {
  laneInfo$ = new Observable<LaneInfo[]>()
  laneInfoCache: LaneInfo[] = []
  columns = ["lane","color","car","accident","state","pitinfo"]
  constructor(private service: RaceManagerService, private lanes: LaneInfoService) {}

  ngOnInit(): void {
    this.laneInfo$ = this.lanes.getLaneInfos().pipe(
      map(message => this.updateLaneInfos(message.data))
    );
  }

  updateLaneInfos(lanes: LaneInfo[]) : LaneInfo[]
  {
    if (lanes.length != this.laneInfoCache.length) {
      this.laneInfoCache = lanes;
    }
    else {
      for (var lane of lanes) {
        var cache = this.laneInfoCache[lane.lane-1];
        cache.accident = lane.accident;
        cache.state = lane.state;
        cache.pitinfo = lane.pitinfo;
      }
    }

    return this.laneInfoCache;
  }

  toggleAccident(lane: LaneInfo) {
    this.service.setAccident(lane.lane-1, !lane.accident).subscribe();
  }
}
