from game_message import *
from actions import *
import random
from actions_possibles import *
from crewmate import Crewmate
from dispatcher_v2 import DispatcherV2
#from dispatcher import Dispatcher


class Bot:

    priority_queue = []

    most_recent_game_state = None

    def __init__(self):
        self.priority_queue.append(recharge_shields(self))
        self.priority_queue.append(shoot(self))
        self.priority_queue.append(use_radar(self))

        # self.dispatcher = Dispatcher()
        self.dispatcher_v2 = DispatcherV2()
        self.crewmates = []

        print("Initializing your super mega duper bot")

    def get_next_move(self, game_message: GameMessage):
        if game_message.tick == 1:
            for i in range(4):
                self.crewmates.append(Crewmate(game_message.ships[game_message.currentTeamId].crew[i]))
            # self.dispatcher._crewmates = self.crewmates
            self.dispatcher_v2.set_crewmates(self.crewmates)

        print("Starting to think about my next move")

        for action in self.priority_queue:
            action.update_priority(game_message)
        self.priority_queue.sort(key=lambda x: x.priority)

        self.dispatcher_v2.update(game_message)
        # self.dispatcher.update(self.priority_queue, game_message)
        actions = self.dispatcher_v2.do(self.priority_queue)

        return actions


