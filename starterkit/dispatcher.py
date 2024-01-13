from typing import List

from starterkit.actions_possibles import recharge_shields
from starterkit.crewmate import Crewmate
from starterkit.game_message import CrewDistance
from starterkit.orders.order_shield import OrderShield
from starterkit.station_enum import StationEnum


class Dispatcher:
    def __init__(self, crewmates):
        self._crewmates = crewmates

    def dispatch(self, priorities, game_message):
        dispatch_orders = {}

        # Get Priority
        priority = next(iter(priorities), None)

        if priority is None:
            return

        # Get Free CrewMember
        npc = self.get_npc(dispatch_orders)

        if isinstance(priority, recharge_shields):
            self.get_nearest_npc_and_station(StationEnum.SHIELDS)
            npc.set_order(OrderShield())

    def get_npc(self, dispatch_orders):
        for npc in self._crewmates:
            if self.is_free(npc, dispatch_orders):
                return npc
        return self._crewmates[0]

    @staticmethod
    def is_free(npc, dispatch_orders):
        return npc.current_order is None and npc not in dispatch_orders

    def everyone_on_shield(self):
        for npc in self._crewmates:
            npc.set_order(OrderShield())

    def get_nearest_npc_and_station(self, station):
        near_npc:Crewmate = None
        near_npc_station:CrewDistance = None

        for npc in self._crewmates:
            stations:List[CrewDistance] = npc.get_distance_from_stations(station)
            nearStation:CrewDistance = self.get_nearest_station(stations)

            if near_npc_station is None or near_npc_station.distance > nearStation.distance:
                near_npc = npc
                near_npc_distance = nearStation
        return near_npc, near_npc_station

    def get_nearest_station(self, stations:List[CrewDistance]):
        near:CrewDistance = stations[0].distance
        for station in stations:
            if station.distance < near.distance:
                near = station
        return near




