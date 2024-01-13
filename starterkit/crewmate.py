from starterkit.orders.order import Order
from starterkit.game_message import CrewMember
from starterkit.actions import CrewMoveAction


class Crewmate:
    def __init__(self, crew_member: CrewMember):
        self.crew_member = crew_member
        self.current_order: Order = None

    def set_order(self, order: Order):
        self.current_order = order
        self.current_order.set_crew_id(self.crew_member.id)

    def has_action(self) -> bool:
        return self.current_order is not None

    def do(self):
        if self.crew_member.gridPosition is not self.current_order.station.gridPosition:
            return CrewMoveAction(self.crew_member.id, self.current_order.station.gridPosition)

        return self.current_order.execute()
