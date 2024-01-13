from game_message import RadarStation
from orders.order import Order


class OrderScan(Order):
    def __init__(self, station: RadarStation):
        super().__init__(station)

    def execute(self):
        self.station.operator = self.crew_id
