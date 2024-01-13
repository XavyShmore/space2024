from game_message import *
from actions import *
import random
from actions_possibles import *
from starterkit.crewmate import Crewmate
from starterkit.dispatcher_v2 import DispatcherV2


class Bot:

    priority_queue = []

    most_recent_game_state = None

    def __init__(self):
        self.priority_queue.append(recharge_shields(self))
        self.priority_queue.append(recharge_turrets(self))
        self.priority_queue.append(shoot(self))
        self.priority_queue.append(use_radar(self))

        self.dispatcher = DispatcherV2()
        self.crewmates = []

        print("Initializing your super mega duper bot")

    def get_next_move(self, game_message: GameMessage):
        if game_message.tick == 1:
            for i in range(4):
                self.crewmates.append(Crewmate(game_message.ships[game_message.currentTeamId][i]))
            self.dispatcher.set_crewmates(self.crewmates)

        print("Starting to think about my next move")

        for action in self.priority_queue:
            action.update_priority(game_message)
        self.priority_queue.sort(key=lambda x: x.priority)

        self.dispatcher.do(self.priority_queue)


