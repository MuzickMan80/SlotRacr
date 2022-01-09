import { Component, Input, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
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
    for(const setting in this.settings) {
      this.service.setSetting(setting.)
    }
  }
}
