import { Component, Input, OnInit } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { SettingBase } from './setting-base';

@Component({
  selector: 'app-setting',
  templateUrl: './setting.component.html',
  styleUrls: ['./settings.component.scss']
})
export class SettingComponent implements OnInit {
  @Input() setting!: SettingBase<string>;
  @Input() form!: FormGroup;

  constructor() { }

  ngOnInit(): void {
  }
}
