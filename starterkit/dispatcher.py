from typing import List

from starterkit.actions_possibles import recharge_shields, PossibleAction, shoot
from starterkit.crewmate import Crewmate
from starterkit.game_message import CrewDistance, GameMessage, TurretStation
from starterkit.orders.order_shield import OrderShield
from starterkit.station_enum import StationEnum
from starterkit.type_of_target import TypeOfTarget


class Dispatcher:
    def __init__(self, crewmates):
        self._crewmates = crewmates
        self.game_message: GameMessage = None
        self.usID = self.game_message.currentTeamId
        self.dispatch_orders = {}
        self.turrets:List[TurretStation] = self.game_message.ships[self.usID].stations.turrets

    def update(self, priorities: List[PossibleAction], game_message):
        self.game_message: GameMessage = game_message
        self.turrets:List[TurretStation] = self.game_message.ships[self.usID].stations.turrets
        self.dispatch(priorities, game_message)

    def dispatch(self, priorities: List[PossibleAction], game_message):
        # Get Priority
        priority = next(iter(priorities), None)

        if priority is None:
            return

        if isinstance(priority, recharge_shields):
            npc, station = self.get_nearest_npc_and_station(StationEnum.SHIELDS)
            npc.set_order(OrderShield(station))
            self.dispatch_orders[npc] = priority

        if isinstance(priority, shoot):
            turret:TurretStation = self.get_nearest_npc_and_station(StationEnum.TURRETS)




    def get_npc(self, dispatch_orders):
        for npc in self._crewmates:
            if self.is_free(npc):
                return npc
        return self._crewmates[0]

    def is_free(self, npc: Crewmate):
        return npc.current_order is None and npc not in self.dispatch_orders.keys()

    def get_nearest_npc_and_station(self, stationEnum):
        near_npc: Crewmate = None
        near_npc_station: CrewDistance = None

        for npc in self._crewmates:
            stations: List[CrewDistance] = npc.get_distance_from_stations(stationEnum)
            near_station: CrewDistance = self.get_crewDistance(stations)

            if near_npc_station is None or near_npc_station.distance > near_station.distance:
                near_npc = npc
                near_npc_station = near_station

        station = self.get_station_from_id(near_npc_station.stationId, stationEnum)

        return near_npc, station

    def get_crewDistance(self, stations: List[CrewDistance]):
        near: CrewDistance = stations[0]
        for station in stations:
            if station.distance < near.distance:
                near = station
        return near

    def get_optimal_turret(self, prio:shoot):
        if prio.targetType is TypeOfTarget.SHIP:
            if(self.target_has_lot_of_shield(prio.targetID)):
                pass




    def has_turretType(self, TurretType):
        for station in self.turrets:
            if station.turretType == TurretType:
                return True
        return False

    def target_has_lot_of_shield(self, targetID):
        self.game_message[]

    def get_station_from_id(self, id, stationType):
        if stationType == StationEnum.SHIELDS:
            for station in self.game_message.ships[self.usID].stations.shields:
                if id == station.id:
                    return station
        if stationType == StationEnum.HELMS:
            for station in self.game_message.ships[self.usID].stations.helms:
                if id == station.id:
                    return station
        if stationType == StationEnum.RADARS:
            for station in self.game_message.ships[self.usID].stations.radars:
                if id == station.id:
                    return station
        if stationType == StationEnum.TURRETS:
            for station in self.game_message.ships[self.usID].stations.turrets:
                if id == station.id:
                    return station
