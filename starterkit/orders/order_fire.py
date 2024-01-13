from starterkit.orders.order import Order
from starterkit.game_message import Vector, TurretStation, TurretType
from starterkit.actions import TurretShootAction, TurretLookAtAction
from starterkit.math import Math


class OrderFire(Order):

    ALIGNED_OFFSET = 2.0

    def __init__(self, station: TurretStation, target_position: Vector):
        super().__init__(station)
        self.target_position = target_position

    def __is_aligned(self) -> bool:
        angle: float = Math.angle_between_vectors(self.station.worldPosition, self.target_position)
        return self.station.orientationDegrees - self.ALIGNED_OFFSET < angle < self.station.orientationDegrees + self.ALIGNED_OFFSET

    def execute(self):
        self.station.operator = self.crew_id

        if not self.__is_aligned and (self.station.turretType == TurretType.Normal or self.station.turretType == TurretType.EMP):
            return TurretLookAtAction(target=self.target_position, stationId=self.station.id)

        if self.__is_aligned():
            if self.station.cooldown == 0:
                return TurretShootAction(stationId=self.station.id)
