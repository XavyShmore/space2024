from abc import ABC, abstractmethod
import math
from type_of_action import TypeOfAction
from type_of_target import TypeOfTarget


class PossibleAction(ABC):
    priority = 0
    type_of_action = None

    def __init__(self, bot):
        self.bot = bot

    @abstractmethod
    def do_action(self):
        pass

    @abstractmethod
    def update_priority(self, game_message):
        pass


class recharge_shields(PossibleAction):
    priority = 0
    type_of_action = TypeOfAction.RECHARGE_SHIELD

    
    def do_action(self):
        pass
    def update_priority(self, game_message):
        self.priority = 25
        
        team_id = game_message.currentTeamId

        shield = game_message.ships[team_id].currentShield
        health = game_message.ships[team_id].currentHealth
    
        if shield < 100:
            self.priority = 50
        elif shield > 150:
            self.priority = 10
        if health < 50:
            self.priority *= 1.5


class shoot(PossibleAction):
    priority = 0
    type_of_action = TypeOfAction.SHOOT
    targetID = None
    targetType = None
    
    def do_action(self):
        pass
    def update_priority(self, game_message):
        self.priority = 30

        station_position = game_message.shipsPositions[game_message.currentTeamId]

        #print(game_message)
        ship_radius = 100

        def distance_between_line_and_point(point1, line_vector, line_point):
            #calculate distance between station and debris trajectory line
            #point1 is station position
            #line_vector is debris velocity
            #line_point is debris position

            r = {"x":(point1.x - line_point.x), 
                 "y":(point1.y - line_point.y)}
            
            #vector perpendicular to line_vector
            s = {"x": -line_vector.y, 
                 "y": line_vector.x}
            #make sure s is a unit vector
            s_magnitude = math.sqrt(s["x"]**2 + s["y"]**2)
            s["x"] /= s_magnitude
            s["y"] /= s_magnitude

            #project r onto s
            dist = {"x": r["x"]*s["x"], 
                    "y": r["y"]*s["y"]}
            
            return math.sqrt(dist["x"]**2 + dist["y"]**2)

        # test colisions with asteroids
        for debris in game_message.debris:
            #calculate distance between station and debris trajectory line
            debris_position = debris.position
            debris_velocity = debris.velocity
            debris_radius = debris.radius

            if distance_between_line_and_point(station_position, debris_velocity, debris_position) < ship_radius + debris_radius:
                self.targetID = debris
                self.targetType = TypeOfTarget.DEBRIS
                self.priority = 45
                break

        for ship in game_message.ships:
            #print(ship)
            #print(game_message.currentTeamId)
            if ship != game_message.currentTeamId:
                if ship in self.bot.still_alive_players_set:
                    self.targetID = ship
                    self.targetType = TypeOfTarget.SHIP
                    self.priority = 40
                    break

class use_radar(PossibleAction):
    priority = 0
    type_of_action = TypeOfAction.USE_RADAR

    PRIORITY_SLOPE = 0.8

    MAX_PRIORITY = 40

    def do_action(self):
        pass
    def update_priority(self, game_message):
        if self.bot.last_tick_the_radar_was_used < game_message.currentTickNumber:
            self.priority += self.PRIORITY_SLOPE
        if self.priority > self.MAX_PRIORITY:
            self.priority = self.MAX_PRIORITY
        


