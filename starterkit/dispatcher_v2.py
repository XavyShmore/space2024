from actions_possibles import PossibleAction, recharge_shields, shoot, use_radar
from game_message import GameMessage
from orders.order import Order
from orders.order_fire import OrderFire
from orders.order_scan import OrderScan
from orders.order_shield import OrderShield
from type_of_action import TypeOfAction
from type_of_target import TypeOfTarget


class DispatcherV2:
    def __init__(self):
        self.crewmates = []
        self.game_message: GameMessage = None

    def set_crewmates(self, crewmates: list):
        self.crewmates = crewmates

    def create_fire_order(self, possible_order: PossibleAction) -> Order:
        if possible_order.targetType == TypeOfTarget.SHIP:
            return OrderFire(self.game_message.ships[self.game_message.currentTeamId].stations.turrets[0],
                             self.game_message.ships[possible_order.targetID].worldPosition)
        else:
            for d in self.game_message.debris:
                if d.id == possible_order.targetID:
                    return OrderFire(self.game_message.ships[self.game_message.currentTeamId].stations.turrets[0],
                                     self.game_message.debris[possible_order.targetID].position)

    def map_order(self, possible_order: PossibleAction) -> Order:
        if possible_order.type_of_action == TypeOfAction.RECHARGE_SHIELD:
            return OrderShield(self.game_message.ships[self.game_message.currentTeamId].stations.shields[0])
        elif possible_order.type_of_action == TypeOfAction.SHOOT:
            return self.create_fire_order(possible_order)
        elif possible_order.type_of_action == TypeOfAction.USE_RADAR:
            return OrderScan(self.game_message.ships[self.game_message.currentTeamId].stations.radars[0])
        return self.create_fire_order(possible_order)

    def update(self, game_message: GameMessage):
        self.game_message = game_message

    def do(self, priority_list: list) -> []:
        actions = []
        for i, crewmate in enumerate(self.crewmates):
            order = self.map_order(priority_list[(-1 - i) % 3])
            if order is not None:
                crewmate.set_order(order)
                action = crewmate.do()
                if action is not None:
                    actions.append(action)
        return actions
