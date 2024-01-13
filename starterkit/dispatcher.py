from starterkit.actions_possibles import recharge_shields
from starterkit.orders.order_shield import OrderShield


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
