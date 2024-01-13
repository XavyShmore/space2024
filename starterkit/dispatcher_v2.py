from starterkit.actions_possibles import PossibleAction, recharge_shields, recharge_turrets, shoot, use_radar
from starterkit.game_message import GameMessage
from starterkit.orders.order import Order
from starterkit.orders.order_fire import OrderFire
from starterkit.orders.order_scan import OrderScan
from starterkit.orders.order_shield import OrderShield


class DispatcherV2:
    def __init__(self):
        self.crewmates = []
        self.game_message: GameMessage = None

    def set_crewmates(self, crewmates: list):
        self.crewmates = crewmates

    def map_order(self, possible_order: PossibleAction) -> Order:
        if possible_order is isinstance(recharge_shields):
            return OrderShield(self.game_message.ships[self.game_message.currentTeamId].stations["shields"])
        elif possible_order is isinstance(recharge_turrets):
            return OrderFire(self.game_message.ships[self.game_message.currentTeamId].stations["turrets"], self.game_message.ships[self.game_message.currentTeamId].position)
        elif possible_order is isinstance(shoot):
            return OrderFire(self.game_message.ships[self.game_message.currentTeamId].stations["turrets"], self.game_message.ships[self.game_message.currentTeamId].position)
        elif possible_order is isinstance(use_radar):
            return OrderScan(self.game_message.ships[self.game_message.currentTeamId].stations["radars"])

    def update(self, game_message: GameMessage):
        self.game_message = game_message

    def do(self, priority_list: list):
        for i, crewmate in enumerate(self.crewmates):
            order = priority_list[-1 - i]
            crewmate.set_order(order)
