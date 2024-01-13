import math

from orders.order import Order
from game_message import CrewMember
from actions import CrewMoveAction
from station_enum import StationEnum


class Crewmate:
    def __init__(self, crew_member: CrewMember):
        self.crew_member = crew_member
        self.current_order: Order = None

    def get_distance_from_stations(self, station_enum: StationEnum) -> list:
        if station_enum == StationEnum.TURRETS:
            return self.crew_member.distanceFromStations.turrets
        elif station_enum == StationEnum.SHIELDS:
            return self.crew_member.distanceFromStations.shields
        elif station_enum == StationEnum.RADARS:
            return self.crew_member.distanceFromStations.radars
        return self.crew_member.distanceFromStations.helms

    def set_order(self, order: Order):
        self.current_order = order
        self.current_order.set_crew_id(self.crew_member.id)

    def has_action(self) -> bool:
        return self.current_order is not None

    def distance_between_vectors(self, vector1, vector2):
        distance = math.sqrt((vector2.x - vector1.x) ** 2 + (vector2.y - vector1.y) ** 2)
        return distance

    def do(self):
        # if int(self.crew_member.gridPosition.x) != int(self.current_order.station.gridPosition.x) and \
        #         int(self.crew_member.gridPosition.y) != int(self.current_order.station.gridPosition.y):
        dst = self.distance_between_vectors(self.crew_member.gridPosition, self.current_order.station.gridPosition)
        if dst > 4.15:
            return CrewMoveAction(self.crew_member.id, self.current_order.station.gridPosition)

        return self.current_order.execute()
