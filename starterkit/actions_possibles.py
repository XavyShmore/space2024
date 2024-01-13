from abc import ABC, abstractmethod

class PossibleAction(ABC):
    priority = 0

    @abstractmethod
    def method_a(self):
        pass

    @abstractmethod
    def method_b(self):
        pass


class rotate_ship(PossibleAction):
    def __init__(self, bot):
        self.bot = bot
    
    def do_action(self):
        pass

    def update_priority(self):
        priority = 0


class recharge_shields(PossibleAction):
    def __init__(self, bot):
        self.bot = bot
    
    def do_action(self):
        pass

    def update_priority(self):
        priority = 0


class recharge_turrets(PossibleAction):
    def __init__(self, bot):
        self.bot = bot
    
    def do_action(self):
        pass

    def update_priority(self):
        priority = 0


class shoot(PossibleAction):
    def __init__(self, bot):
        self.bot = bot
    
    def do_action(self):
        pass

    def update_priority(self):
        priority = 0


class use_radar(PossibleAction):
    def __init__(self):
        pass
    
    def do_action(self):
        pass

    def update_priority(self):
        priority = 0
