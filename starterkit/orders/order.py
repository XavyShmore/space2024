from abc import ABC, abstractmethod
from starterkit.game_message import Station


class Order(ABC):
    def __init__(self, station: Station):
        self.station = station
        self.crew_id = None

    def set_crew_id(self, crew_id: str):
        self.crew_id = crew_id

    @abstractmethod
    def execute(self):
        pass
