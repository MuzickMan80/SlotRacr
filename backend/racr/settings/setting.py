
class SettingType:
    BOOL_SETTING="bool"
    INT_SETTING="int"
    STRING_SETTING="string"
    COLOR_SETTING="color"

class Setting:
    def __init__(self,type,name,default,description,setter=None) -> None:
        self.type=type
        self.name=name
        self.default=default
        self.description=description
        self.value_=default
        self.setter=setter

    @property
    def value(self):
        return self.value_

    @value.setter
    def value(self, value):
        self.value_ = value
        if self.setter:
            self.setter(value)

class BoolSetting(Setting):
    def __init__(self,name,default,description="",setter=None):
        super().__init__(SettingType.BOOL_SETTING,name,default,description,setter)

class IntSetting(Setting):
    def __init__(self,name,default,min,max,units="",description="",setter=None):
        super().__init__(SettingType.INT_SETTING,name,default,description,setter)
        self.min=min
        self.max=max
        self.units=units

# class ProbabilitySetting(IntSetting):
#     def __init__(self,name,default,min=0,max=100,units="%",description="",setter=None):
#         super().__init__(SettingType.INT_SETTING,name,default,min,max,units,description,setter)

class StringSetting(Setting):
    def __init__(self,name,default="",maxlen=None,description="",setter=None):
        super().__init__(SettingType.STRING_SETTING,name,default,description,setter)
        self.maxlen=maxlen
        