import { Injectable } from '@angular/core';
import { io } from 'socket.io-client';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class WebsocketService {
  private socket: any;

  constructor() { this.connect(); }

  connect(): Observable<any> {
    this.socket = io(`${environment.api_url}`);

    let observable = new Observable(observer => {
      this.socket.on('update', (data:any) => {
        console.log('got data ' + data);
        observer.next({data: JSON.parse(data).lanes});
      })
      return () => {
        this.socket.disconnect();
      }
    });

    this.socket.on("connect", () => {
      console.log('socket connected')
      this.socket.emit('update');
    });

    return observable;
  }

  request_update() {
    this.socket.emit('update');
  }

  send_message(data: any) {
    this.socket.emit('message', JSON.stringify(data));
  }
  
  simulate_activity(on: boolean, rate: number) {
    this.socket.emit('simulate_activity', JSON.stringify({ 'enable': on, 'rate': rate }));
  }
}
