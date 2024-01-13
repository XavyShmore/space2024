from starterkit.actions_possibles import PossibleAction, recharge_shields, recharge_turrets, shoot, use_radar
from starterkit.game_message import GameMessage
from starterkit.orders.order import Order
from starterkit.orders.order_fire import OrderFire
from starterkit.orders.order_scan import OrderScan
from starterkit.orders.order_shield import OrderShield
from starterkit.type_of_action import TypeOfAction


class DispatcherV2:
    def __init__(self):
        self.crewmates = []
        self.game_message: GameMessage = None

    def set_crewmates(self, crewmates: list):
        self.crewmates = crewmates

    def map_order(self, possible_order: PossibleAction) -> Order:
        if possible_order.type_of_action == TypeOfAction.RECHARGE_SHIELD:
            return OrderShield(self.game_message.ships[self.game_message.currentTeamId].stations.shields[0])
        elif possible_order.type_of_action == TypeOfAction.RECHARGE_TURRET:
            return OrderFire(self.game_message.ships[self.game_message.currentTeamId].stations.turrets[0], self.game_message.ships[possible_order.targetID].worldPosition)
        elif possible_order.type_of_action == TypeOfAction.SHOOT:
            return OrderFire(self.game_message.ships[self.game_message.currentTeamId].stations.turrets[0], self.game_message.ships[possible_order.targetID].worldPosition)
        elif possible_order.type_of_action == TypeOfAction.USE_RADAR:
            return OrderScan(self.game_message.ships[self.game_message.currentTeamId].stations.radars[0])
        return OrderShield(self.game_message.ships[self.game_message.currentTeamId].stations.shields[0])

    def update(self, game_message: GameMessage):
        self.game_message = game_message

    def do(self, priority_list: list) -> []:
        actions = []
        for i, crewmate in enumerate(self.crewmates):
            order = self.map_order(priority_list[-1 - i])
            if order is not None:
                crewmate.set_order(order)
                print(order)
                action = crewmate.do()
                if action is not None:
                    actions.append(action)
        return actions
