import { Setting } from "../services/settings.service";
import { SettingBase } from "./setting-base";
import { TextboxSetting } from "./setting-textbox";
import { ToggleSetting } from "./setting-toggle";

export class SettingsFactory {
    static Create(key: string, s: Setting) : SettingBase<any> {
        if (s.type === "bool") {
            return new ToggleSetting({
                name: key,
                label: s.name,
                value: s.value as boolean
            });
        }
        return new TextboxSetting({
            name: key,
            label: s.name,
            value: s.value
        });
    }
}