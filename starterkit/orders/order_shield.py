from starterkit.game_message import Station
from starterkit.orders.order import Order


class OrderShield(Order):
    def __init__(self, station: Station):
        super().__init__(station)

    def execute(self):
        self.station.operator = self.crew_id
