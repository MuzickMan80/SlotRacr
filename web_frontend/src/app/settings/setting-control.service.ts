import { Injectable } from "@angular/core";
import { FormControl, FormGroup } from "@angular/forms";
import { SettingBase } from "./setting-base";

@Injectable({
    providedIn: 'root'
  })
export class SettingControlService {
    constructor() {}

    toFormGroup(settings: SettingBase[]) {
        const group: any = {};

        settings.forEach(setting => {
            group[setting.name] = new FormControl(setting.value)
        });

        console.log(JSON.stringify(group));
        return new FormGroup(group);
    }
}