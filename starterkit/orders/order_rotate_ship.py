from starterkit.game_message import Station, Vector
from starterkit.actions import ShipLookAtAction
from starterkit.orders.order import Order


class OrderRotateShip(Order):
    def __init__(self, station: Station, target_position: Vector):
        super().__init__(station)
        self.target_position = target_position

    def execute(self):
        self.station.operator = self.crew_id
        return ShipLookAtAction(target=self.target_position)
