import { Component, Input, OnInit } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { Observable, forkJoin } from 'rxjs';
import { tap } from 'rxjs/operators';
import { BadgeInfo, RaceRegistrationService } from 'src/app/services/race-registration.service';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.scss']
})
export class RegistrationComponent implements OnInit {
  setting$: Observable<BadgeInfo[]>;
  settings: BadgeInfo[] = [];

  constructor(private service: RaceRegistrationService) {
    this.setting$ = this.service.getBadges()
      .pipe(
        tap((d) => this.settings = d.sort((a,b) => a.badge < b.badge ? -1 : 1))
      );
    }

  ngOnInit(): void {
  }

  setName(setting: BadgeInfo, event: any): void {
    setting.name = event.target.value;
  }

  onSubmit(): void {
    const observables : Observable<any>[] = this.settings.map(s => {
      return this.service.setBadgeName(s.badge, s.name)
    });
    forkJoin(observables).subscribe();
  }
}
