import { Injectable } from '@angular/core';
import { WebsocketService } from './websocket.service';
import { Observable, Subject } from 'rxjs';

export interface LaneInfo {
  state: string;
  lane: number;
  best: string;
  last: string;
  laps: number;
  started: boolean;
  pos: number;
  accident: boolean;
  pitinfo: string;
}

@Injectable({
  providedIn: 'root'
})
export class LaneInfoService {
  
  subject: Observable<MessageEvent<LaneInfo[]>>;

  constructor(private wsService: WebsocketService) {
    this.subject = <Observable<any>>wsService.connect()
  }

  getLaneInfos() { return this.subject; }
  requestUpdate() { this.wsService.request_update(); }
}
