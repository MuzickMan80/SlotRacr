import { Injectable } from '@angular/core';
import { WebsocketService } from './websocket.service';
import { Subject } from 'rxjs';
import { stringify } from '@angular/compiler/src/util';

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
  
  subject: Subject<MessageEvent<LaneInfo[]>>;

  constructor(private wsService: WebsocketService) {
    this.subject = <Subject<any>>wsService
      .connect()
  }

  getLaneInfos() { return this.subject.asObservable(); }
  requestUpdate() { this.subject.next(); }
}
