import { Component, OnInit } from '@angular/core';
import { RaceManagerService } from '../services/race-manager.service';

@Component({
  selector: 'app-race-reset',
  templateUrl: './race-reset.component.html',
  styleUrls: ['./race-reset.component.scss']
})
export class RaceResetComponent implements OnInit {

  constructor(private service: RaceManagerService) { }

  ngOnInit(): void {
  }

  reset(): void {
    this.service.reset().subscribe();
  }
}
