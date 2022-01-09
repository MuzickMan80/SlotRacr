import { Component, Input, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { forkJoin, Observable, of } from 'rxjs';
import { SettingsService } from '../services/settings.service';
import { SettingBase } from './setting-base';
import { SettingControlService } from './setting-control.service';

@Component({
  selector: 'app-settings',
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.scss']
})
export class SettingsComponent implements OnInit {
  @Input() settings: SettingBase[] | null = [];
  form!: FormGroup;

  constructor(private settingControl: SettingControlService, private service: SettingsService) { }

  ngOnInit(): void {
    this.form = this.settingControl.toFormGroup(this.settings || []);
  }

  onSubmit(): void {
    const settings = this.settings || []
    const observables : Observable<any>[] = settings.map(s => {
      const control = this.form.controls[s.name];
      if (control.dirty) {
        return this.service.setSetting(s.group, s.name, control.value);
      } else {
        return of<any>({});
      }
    });
    forkJoin(observables).subscribe();
  }
}
