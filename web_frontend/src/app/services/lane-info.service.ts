import { Injectable } from '@angular/core';
import { WebsocketService } from './websocket.service';
import { Observable, Subject } from 'rxjs';

export interface LaneInfo {
  lane: number;
  best: string;
  last: string;
  laps: number;
  started: boolean;
  pos: number;
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
