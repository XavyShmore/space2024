import math

from orders.order import Order
from game_message import Vector, TurretStation, TurretType
from actions import TurretShootAction, TurretLookAtAction, TurretChargeAction


class OrderFire(Order):

    ALIGNED_OFFSET = 2.0

    def __init__(self, station: TurretStation, target_position: Vector):
        super().__init__(station)
        self.target_position = target_position

    def __angle_between_vectors(self, vector1, vector2) -> float:
        dot_product = vector1.x * vector2.x + vector1.y * vector2.y
        magnitude_product = math.sqrt(vector1.x ** 2 + vector1.y ** 2) * math.sqrt(vector2.x ** 2 + vector2.y ** 2)

        cosine_similarity = dot_product / magnitude_product
        angle_radians = math.acos(cosine_similarity)

        angle_degrees = math.degrees(angle_radians)

        return angle_degrees

    def __is_aligned(self) -> bool:
        angle: float = self.__angle_between_vectors(self.station.worldPosition, self.target_position)
        return self.station.orientationDegrees - self.ALIGNED_OFFSET < angle < self.station.orientationDegrees + self.ALIGNED_OFFSET

    def execute(self):
        self.station.operator = self.crew_id

        # if not self.__is_aligned and (self.station.turretType == TurretType.Normal or self.station.turretType == TurretType.EMP):
        #     return TurretLookAtAction(target=self.target_position, stationId=self.station.id)

        # if self.__is_aligned():
        # if self.station.cooldown == 0:
        print("FVSDGHFGDSHGFHJDSGFHJDSGHJFGSDHFGSD")
        if self.station.charge <= 0:
            return TurretChargeAction(stationId=self.station.id)

        return TurretShootAction(stationId=self.station.id)
