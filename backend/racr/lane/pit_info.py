import random
from typing import List

normal_infos = [
    "Refuelling car",
    "Replacing tires",
    "Adjusting spoiler"
]

out_of_fuel_infos = [
    "Refuelling car",
    "Replacing tires",
    "Adjusting spoiler",
    "Trying to restart engine",
    "Engine flooded",
    "Cooling engine",
]

accident_infos = [
    "Sawing off passenger side panel",
    "Crew hammering on trunk",
    "Replacing right side window and pouch",
    "Crew jumping on front spoiler",
    "Removing front hood and panels",
    "Crew jumping on rear panel",
    "Crew taping right front quarter panel",
    "Crew taping right rear quarter panel",
    "Crew taping left front quarter panel",
    "Crew taping left rear quarter panel",
    "Crew taping right side door plate",
    "Crew taping left side door plate",
    "Crew jumping on hood",
    "Crew jumping on trunk",
    "Crew replacing damaged tire",
    "Crew bending out wheel well",
    "Crew arguing with driver",
    "Car left early and crew pushing car back",
    "Putting out engine fire",
    "Trying to restart engine",
    "Crew having trouble jacking damaged car",
    "Crew can't get gas can into damaged car",
]

def _get_pit_info(infos:List[str]) -> str:
    return random.choice(infos)

def get_pit_info(oog:bool, accident:bool) -> str:
    if accident:
        return _get_pit_info(accident_infos)
    if oog:
        return _get_pit_info(out_of_fuel_infos)
    
    return _get_pit_info(normal_infos)
