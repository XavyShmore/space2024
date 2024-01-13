from typing import List

from actions_possibles import recharge_shields, shoot, PossibleAction
from crewmate import Crewmate
from game_message import CrewDistance, GameMessage, TurretStation
from orders.order_shield import OrderShield
from starterkit.orders.order_fire import OrderFire
from starterkit.type_of_target import TypeOfTarget
from station_enum import StationEnum


class Dispatcher:
    def __init__(self):
        self._crewmates = []
        self.game_message: GameMessage = None
        # self.usID = self.game_message.currentTeamId
        self.dispatch_orders = {}
        # self.turrets:List[TurretStation] = self.game_message.ships[self.usID].stations.turrets

    def update(self, priorities: List[PossibleAction], game_message):
        self.game_message: GameMessage = game_message
        self.usID = self.game_message.currentTeamId
        self.turrets: List[TurretStation] = self.game_message.ships[self.usID].stations.turrets
        self.dispatch(priorities, game_message)

    def dispatch(self, priorities: List[PossibleAction], game_message):

        for priority in priorities:
            if isinstance(priority, recharge_shields):
                npc, station = self.get_nearest_npc_and_station(StationEnum.SHIELDS)
                npc.set_order(OrderShield(station))
                self.dispatch_orders[npc] = priority

            if isinstance(priority, shoot):
                npc, turret = self.get_nearest_npc_and_station(StationEnum.TURRETS)

                if priority.targetType == TypeOfTarget.SHIP:
                    npc.set_order(OrderFire(turret,
                                            self.game_message.ships[priority.targetID].worldPosition))
                else:
                    for d in self.game_message.debris:
                        if d.id == priority.targetID:
                            npc.set_order(OrderFire(turret,
                                                    self.game_message.debris[priority.targetID].position))

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

    def get_optimal_turret(self, prio: shoot):
        if prio.targetType is TypeOfTarget.SHIP:
            if (self.target_has_lot_of_shield(prio.targetID)):
                pass

    def has_turretType(self, TurretType):
        for station in self.turrets:
            if station.turretType == TurretType:
                return True
        return False

    def target_has_lot_of_shield(self, targetID):
        # self.game_message[]
        pass

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
