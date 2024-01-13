from enum import unique, Enum

@unique
class TypeOfAction(int, Enum):
    RECHARGE_SHIELD = 0,
    RECHARGE_TURRET = 1,
    SHOOT = 2,
    USE_RADAR = 3
