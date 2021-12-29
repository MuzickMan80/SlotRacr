
class Setting:
    BOOL_SETTING="bool"
    INT_SETTING="int"
    STRING_SETTING="string"
    COLOR_SETTING="color"

    def __init__(self,type,name,default,description) -> None:
        self.type=type
        self.name=name
        self.default=default
        self.description=description
        self.value=default

class BoolSetting(Setting):
    def __init__(self,name,default,description=""):
        super().__init__(Setting.BOOL_SETTING,name,default,description)

class IntSetting(Setting):
    def __init__(self,name,default,min,max,units="",description=""):
        super().__init__(Setting.INT_SETTING,name,default,description)
        self.min=min
        self.max=max
        self.units=units

class ProbabilitySetting(IntSetting):
    def __init__(self,name,default,min=0,max=100,units="%",description=""):
        super().__init__(Setting.INT_SETTING,name,default,min,max,units,description)

class StringSetting(Setting):
    def __init__(self,name,default="",maxlen=None,description=""):
        super().__init__(Setting.STRING_SETTING,name,default,description)
        self.maxlen=maxlen
    
        