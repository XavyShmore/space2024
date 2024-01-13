from enum import unique, Enum

@unique
class TypeOfAction(int, Enum):
    RECHARGE_SHIELD = 0,
    SHOOT = 2,
    USE_RADAR = 3
