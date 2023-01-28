import random
from typing import List

def normal_infos(good_crew: str, bad_crew: str):
    return [
        f'Refuelling car',
        f'Replacing tires',
        f'Adjusting spoiler',
        f'Increase left trim',
        f'Decrease left trim',
        f'Increase right trim',
        f'Decrease right trim',
        f'{good_crew} removes hot dog wrapper from grill',
        f'Adjust left suspension',
        f'Adjust right suspension',
        f'Get driver a drink of water',
        f'Replace outside tires only',
        f'Minor trouble  with gear box',
        f'Wipe front window',
        f'{bad_crew} lost tire during replacement',
        f'Left front tire not lining up',
        f'Bad tire hand off',
        f'Gas going in slow',
        f'Driver states car is too loose',
        f'Driver states car is too tight',
        f'Driver states slight sputter',
        f'Driver states brake trouble',
        f'Come on hurry up {bad_crew}',
        f'Lets go - lets go - lets go',
        f'Driver pounding on steering wheel',
        f'{bad_crew} causes pit fuel fire',
        f'{bad_crew} makes rookie mistake',
        f'{bad_crew} tripped on pit wall',
        f'{bad_crew} bent body with jack',
        f'Car bumped you in pit area',
        f'{bad_crew} left gas can in car',
        f'{bad_crew} eating chili dog; not ready',
        f'Car stalled in pit',
        f'Bee distracts {bad_crew}',
        f'{bad_crew} gazing at hot race babe',
        f'Driver says car has too much push',
        f'Car overshoots pit area',
        f'{good_crew} changes tire in record time',
        f'{good_crew} shares car strategy',
        f'{good_crew} correcting oil leak',
        f'{bad_crew} dropped wrench',
        f'{bad_crew} slips on oil',
        f'{good_crew} adjusts suspension',
        f'Four fresh Goodyear tires installed',
        f'Replaced two outside tires',
        f'Driver flips {bad_crew} the bird',
    ]

def out_of_fuel_infos(good_crew: str, bad_crew: str):
    return [
        f'Refuelling car',
        f'Replacing tires',
        f'Adjusting spoiler',
        f'Trying to restart engine',
        f'Engine flooded',
        f'Cooling engine',
        f'Trouble retstarting engine',
        f'Bleed gas line',
        f'Hot engine froze up',
        f'Starter not kicking in',
        f'Changing tires',
        f'Pit crew pushes car to pit area',
        f'{bad_crew} trips while pushing car',
        f'Car not starting'
    ]

def accident_infos(good_crew: str, bad_crew: str):
    return [
        f'Sawing off passenger side panel',
        f'{good_crew} hammering on trunk',
        f'Replacing right side window and pouch',
        f'{good_crew} jumping on front spoiler',
        f'Removing front hood and panels',
        f'{good_crew} jumping on rear panel',
        f'{good_crew} taping right front quarter panel',
        f'{good_crew} taping right rear quarter panel',
        f'{good_crew} taping left front quarter panel',
        f'{good_crew} taping left rear quarter panel',
        f'{good_crew} taping right side door plate',
        f'{good_crew} taping left side door plate',
        f'{good_crew} jumping on hood',
        f'{good_crew} jumping on trunk',
        f'{good_crew} replacing damaged tire',
        f'{good_crew} bending out wheel well',
        f'{bad_crew} arguing with driver',
        f'Car left early and {good_crew} pushing car back',
        f'Putting out engine fire',
        f'Trying to restart engine',
        f'{bad_crew} having trouble jacking damaged car',
        f'{bad_crew} can\'t get gas can into damaged car',
        f'{good_crew} shares details of damaged car',
        f'{bad_crew} can\'t get tire into bent fender',
        f'{good_crew} corrects loose steering',
        f'{good_crew} repairing bent spoiler',
        f'{bad_crew} adjusts suspension incorrectly',
    ]

good_crew_names = [
    "Bobby",
    "Ace",
    "Ricky",
    "Buck",
    "Duke",
    "Rocky",
    "Clem",
    "Jed",
]

bad_crew_names = [
    "Bubba",
    "Chubby",
    "Skeeter",
    "Rusty",
    "Shaggy",
    "Slim",
    "Slick",
    "Scrappy",
]

def _get_pit_info(infos:List[str]) -> str:
    return random.choice(infos)

def get_pit_info(oog:bool, accident:bool, penalty: bool, lane:int) -> str:
    good_crew = good_crew_names[lane]
    bad_crew = bad_crew_names[lane]
    if penalty:
        return "Penalty for coming in too fast"
    if accident:
        return _get_pit_info(accident_infos(good_crew, bad_crew))
    if oog:
        return _get_pit_info(out_of_fuel_infos(good_crew, bad_crew))
    
    return _get_pit_info(normal_infos(good_crew, bad_crew))
