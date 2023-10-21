import json

class TrackRegistration:
    def __init__(self, track):
        self.registration = {}
        self.track = track
        self._filename = 'registration.json'
        self.load()

    def load(self):
        try:
            with open(self._filename) as jsonfile:
                self.registration = json.load(jsonfile)
        except Exception as err:
            print(err)

    def save(self):
        try:
            with open(self._filename, 'w') as jsonfile:
                json.dump(self.registration, jsonfile)
        except Exception as err:
            print(err)

    def get_badges(self):
        badges = []
        for key, value in self.registration.items():
            badges.append({'badge': key, 'name': value})
        return badges
    
    def get_badge(self, id: str) -> str:
        return self.registration[id]
    
    def set_badge(self, id: str, name: str):
        self.registration[id] = name
        self.save()

    def register_badge_on_lane(self, id: str, lane: int):
        self.track.lanes[lane].badge = id
        self.track.lanes[lane].name = self.get_badge(id)
