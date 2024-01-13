from game_message import *
from actions import *
import random
from actions_possibles import *

class Bot:

    priority_queue = []

    most_recent_game_state = None

    def __init__(self):
        self.priority_queue.append(recharge_shields(self))
        self.priority_queue.append(recharge_turrets(self))
        self.priority_queue.append(shoot(self))
        self.priority_queue.append(use_radar(self))


        print("Initializing your super mega duper bot")


    def get_next_move(self, game_message: GameMessage):

        print("Starting to think about my next move")
        for action in self.priority_queue:
            action.update_priority(game_message)
        self.priority_queue.sort(key=lambda x: x.priority)


