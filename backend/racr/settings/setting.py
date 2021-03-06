
import inspect


class SettingType:
    BOOL_SETTING="bool"
    INT_SETTING="int"
    STRING_SETTING="string"
    COLOR_SETTING="color"
    FLOAT_SETTING="float"

class Setting:
    def __init__(self,type,name,default,description,setter=None) -> None:
        self.type=type
        self.name=name
        self.default=default
        self.description=description
        self.value=default
        self.setter=setter

    def normalize(self, value):
        return value

    async def set_value(self, value):
        self.value = self.normalize(value)
        if self.setter:
            result = self.setter(self.value)            
            if inspect.isawaitable(result):
                await result

class BoolSetting(Setting):
    def __init__(self,name,default,description="",setter=None):
        super().__init__(SettingType.BOOL_SETTING,name,default,description,setter)
    def normalize(self, value):
        return bool(value)

class IntSetting(Setting):
    def __init__(self,name,default,min,max,units="",description="",setter=None):
        super().__init__(SettingType.INT_SETTING,name,default,description,setter)
        self.min=min
        self.max=max
        self.units=units
    def normalize(self, value):
        normalized_val = int(value)
        if normalized_val < self.min:
            normalized_val = self.min
        if normalized_val > self.max:
            normalized_val = self.max
        return normalized_val

class FloatSetting(Setting):
    def __init__(self,name,default,min,max,units="",description="",setter=None):
        super().__init__(SettingType.FLOAT_SETTING,name,default,description,setter)
        self.min=min
        self.max=max
        self.units=units
    def normalize(self, value):
        normalized_val = float(value)
        if normalized_val < self.min:
            normalized_val = self.min
        if normalized_val > self.max:
            normalized_val = self.max
        return normalized_val

# class ProbabilitySetting(IntSetting):
#     def __init__(self,name,default,min=0,max=100,units="%",description="",setter=None):
#         super().__init__(SettingType.INT_SETTING,name,default,min,max,units,description,setter)

class StringSetting(Setting):
    def __init__(self,name,default="",maxlen=None,description="",setter=None):
        super().__init__(SettingType.STRING_SETTING,name,default,description,setter)
        self.maxlen=maxlen
    def normalize(self, value):
        return str(value)
