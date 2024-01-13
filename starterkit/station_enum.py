from enum import unique, Enum


@unique
class StationEnum(int, Enum):
    SHIELDS = 0,
    TURRETS = 1,
    RADARS = 2,
    HELMS = 3
