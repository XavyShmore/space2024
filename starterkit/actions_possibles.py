from abc import ABC, abstractmethod

class PossibleAction(ABC):
    priority = 0
    type_of_action = None

    @abstractmethod
    def do_action(self):
        pass

    @abstractmethod
    def update_priority(self, game_message):
        pass


class recharge_shields(PossibleAction):
    priority = 0
    type_of_action = "recharge_shields"

    def __init__(self, bot):
        self.bot = bot
    
    def do_action(self):
        pass
    def update_priority(self, game_message):
        priority = 25
        
        team_id = game_message.currentTeamId

        shield = game_message.ships[team_id].currentShield
        health = game_message.ships[team_id].currentHealth

        if shield < 100:
            priority = 50
        if health < 50:
            priority *= 1.5

class recharge_turrets(PossibleAction):
    priority = 0
    type_of_action = "recharge_turrets"

    def __init__(self, bot):
        self.bot = bot
    
    def do_action(self):
        pass
    def update_priority(self, game_message):
        priority = 0


class shoot(PossibleAction):
    priority = 0
    type_of_action = "shoot"
    targetID = None
    targetType = None

    def __init__(self, bot):
        self.bot = bot
    
    def do_action(self):
        pass
    def update_priority(self, game_message):
        priority = 30

        for ship in game_message.ships:
            if ship.teamId != game_message.currentTeamId:
                self.targetID = ship.id
                self.targetType = "ship"
                break

class use_radar(PossibleAction):
    priority = 0
    type_of_action = "use_radar"

    def __init__(self, bot):
        self.bot = bot
    
    def do_action(self):
        pass
    def update_priority(self, game_message):
        priority = 0


