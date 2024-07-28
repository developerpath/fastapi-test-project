from pydantic import (
    BaseModel,
    NegativeFloat,
    NegativeInt,
    PositiveFloat,
    PositiveInt,
    NonNegativeFloat,
    NonNegativeInt,
    NonPositiveFloat,
    NonPositiveInt,
    conbytes,
    condecimal,
    confloat,
    conint,
    conlist,
    conset,
    constr,
    Field,
    AnyHttpUrl
)

from enum import Enum

from typing import (
    Deque, Dict, FrozenSet, List, Optional, Sequence, Set, Tuple, Union, Literal
)

from v1.schemas.common import BoolStr


class PokemonItem(BaseModel):
    id: PositiveInt
    image: AnyHttpUrl
    name: str
    base_happiness: NonNegativeInt
    capture_rate: NonNegativeInt
    colors: List[str]
    growth_rates: List[str]
    habitats: List[str]
    is_legendary: BoolStr
    egg_groups: List[str]
    shapes: List[str]

    class Config:
        str_to_lower = True

class PokemonList(BaseModel):
    species: List[PokemonItem]

class PokemonDetails(BaseModel):
    name: str
    abilities: List[str]
    base_experience: NonNegativeInt
    forms: List[str]
    height: NonNegativeInt
    weight: NonNegativeInt
    moves: List[str]
    sprites: Dict[str, AnyHttpUrl]

    class Config:
        str_to_lower = True
