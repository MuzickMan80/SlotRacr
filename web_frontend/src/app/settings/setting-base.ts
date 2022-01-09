import { Setting } from "../services/settings.service";
import { TextboxSetting } from "./setting-textbox";
import { ToggleSetting } from "./setting-toggle";
import { SettingComponent } from "./setting.component";

export class SettingBase<T=any> {
    value: T|undefined;
    name: string;
    label: string;
    controlType: string;
    type: string;
    group: string;
    options: {key: string, value: string}[];

    constructor(options: {
        value?: T;
        name?: string;
        label?: string;
        controlType?: string;
        type?: string;
        group?: string;
        options?: {key: string, value: string}[];
    } = {}) {
        this.value = options.value;
        this.name = options.name || '';
        this.label = options.label || '';
        this.controlType = options.controlType || '';
        this.type = options.type || '';
        this.group = options.group || '';
        this.options = options.options || [];
    }
}
