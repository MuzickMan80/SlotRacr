import { SettingBase } from "./setting-base";

export class ToggleSetting extends SettingBase<boolean> {
    controlType: string = 'toggle';
}