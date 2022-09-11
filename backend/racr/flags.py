
class Flags():
    green="green"
    white="white"
    checkered="checkered"
    yellow="yellow"
    red="red"
    all=[green,white,checkered,yellow,red]

    def parse(string: str):
        if str == Flags.green:
            return Flags.green
        if str == Flags.yellow:
            return Flags.yellow
        if str == Flags.red:
            return Flags.red
