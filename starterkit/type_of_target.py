from enum import unique, Enum

@unique
class TypeOfTarget(int, Enum):
    DEBRIS = 0
    SHIP = 1
    ROCKET = 2