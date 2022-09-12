
class Flags():
    green="green"
    white="white"
    checkered="checkered"
    yellow="yellow"
    red="red"
    all=[green,white,checkered,yellow,red]

    def parse(string: str):
        if string == Flags.green:
            return Flags.green
        if string == Flags.yellow:
            return Flags.yellow
        if string == Flags.red:
            return Flags.red
