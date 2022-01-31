import { formatNumber } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { LaneInfoService, LaneInfo } from '../services/lane-info.service'

@Component({
  selector: 'app-lane-table',
  templateUrl: './lane-table.component.html',
  styleUrls: ['./lane-table.component.scss']
})
export class LaneTableComponent implements OnInit {
  lanes: LaneInfo[] = [];
  columnsToDisplay = ["pit", "name", "lane", "laps", "top", "last"];

  constructor(private service: LaneInfoService) { }

  ngOnInit(): void {
    this.service.getLaneInfos().subscribe(update =>
      this.updateLanes(update.data));
    this.service.requestUpdate();
  }

  updateLanes(update: LaneInfo[]) {
    this.lanes = update.sort((a,b) => a.pos-b.pos);

    console.log(this.lanes);
  }

  formatTime(lane: LaneInfo, time: number) {
    if (!lane.started) {
      return '!!!!!';
    }
    else if (time == null) {
      return '-----';
    }
    else {
      return this.pad(time.toFixed(3), 6);
    }
  }

  formatLaps(lane: LaneInfo) {
    if (!lane.started) {
      return '---';
    }
    return this.pad(lane.laps.toString(), 3);
  }

  pad(str: string, width: number) {
    while (str.length < width) {
      str = '!' + str;
    }
    return str;
  }
}
