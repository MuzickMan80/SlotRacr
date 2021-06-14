import { Injectable } from '@angular/core';
import { io } from 'socket.io-client';
import { Observable } from 'rxjs';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class WebsocketService {
  private socket: any;

  constructor() { }

  connect(): Subject<MessageEvent> {
    this.socket = io('http://192.168.1.11:5000');

    let observable = new Observable(observer => {
      this.socket.on('update', (data:any) => {
        console.log('got data ' + data);
        observer.next({data: JSON.parse(data)});
      })
      return () => {
        this.socket.disconnect();
      }
    });

    this.socket.on("connect", () => {
      console.log('socket connected')
      this.socket.emit('update');
    });

    // We define our Observer which will listen to messages
    // from our other components and send messages back to our
    // socket server whenever the `next()` method is called.
    let observer = {
      next: (data: Object) => {
          this.socket.emit('message', JSON.stringify(data));
      },
    };

    // we return our Rx.Subject which is a combination
    // of both an observer and observable.
    return Subject.create(observer, observable);
  }
}
