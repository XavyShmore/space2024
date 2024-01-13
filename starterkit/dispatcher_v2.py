from actions_possibles import PossibleAction
from game_message import GameMessage, TurretType, Vector
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
        self.assigned_turret = {}

    def set_crewmates(self, crewmates: list):
        self.crewmates = crewmates

    def find_unoccupied_turret(self):
        for turret in self.game_message.ships[self.game_message.currentTeamId].stations.turrets:
            if turret.operator is None and (turret.turretType == TurretType.Normal or turret.turretType == TurretType.EMP):
                if turret.id not in self.assigned_turret.keys():
                    return turret
        return None

    def create_fire_order(self, possible_order: PossibleAction) -> Order:
        turret = self.find_unoccupied_turret()
        if turret is None:
            return None

        self.assigned_turret[turret.id] = 1
        return OrderFire(turret, Vector(10, 10))

        # if possible_order.targetType == TypeOfTarget.SHIP:
        #     return OrderFire(turret,
        #                      self.game_message.ships[possible_order.targetID].worldPosition)
        # else:
        #     for d in self.game_message.debris:
        #         if d.id == possible_order.targetID:
        #             return OrderFire(turret,
        #                              self.game_message.debris[possible_order.targetID].position)

    def map_order(self, possible_order: PossibleAction) -> Order:
        # if possible_order.type_of_action == TypeOfAction.RECHARGE_SHIELD:
        #     return OrderShield(self.game_message.ships[self.game_message.currentTeamId].stations.shields[0])
        # elif possible_order.type_of_action == TypeOfAction.SHOOT:
        #     return self.create_fire_order(possible_order)
        # elif possible_order.type_of_action == TypeOfAction.USE_RADAR:
        #     return OrderScan(self.game_message.ships[self.game_message.currentTeamId].stations.radars[0])
        return self.create_fire_order(possible_order)

    def update(self, game_message: GameMessage):
        self.game_message = game_message

    def do(self, priority_list: list) -> []:
        actions = []
        for i, crewmate in enumerate(self.crewmates):
            order = self.map_order(priority_list[i % 3])
            if order is not None:
                if not crewmate.has_action():
                    crewmate.set_order(order)

            if crewmate.has_action():
                action = crewmate.do()
                if action is not None:
                    actions.append(action)
        return actions
