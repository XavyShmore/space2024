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
            return self.current_order["distanceFromStations"]["turrets"]
        elif station_enum == StationEnum.SHIELDS:
            return self.current_order["distanceFromStations"]["shields"]
        elif station_enum == StationEnum.RADARS:
            return self.current_order["distanceFromStations"]["radars"]
        return self.current_order["distanceFromStations"]["helms"]

    def set_order(self, order: Order):
        self.current_order = order
        self.current_order.set_crew_id(self.crew_member.id)

    def has_action(self) -> bool:
        return self.current_order is not None


    def do(self):
        if self.crew_member.gridPosition.x != self.current_order.station.gridPosition.x and \
                self.crew_member.gridPosition.y != self.current_order.station.gridPosition.y:
            return CrewMoveAction(self.crew_member.id, self.current_order.station.gridPosition)

        return self.current_order.execute()
