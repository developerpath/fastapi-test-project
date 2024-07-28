from pydantic import BaseModel, PositiveInt, NonNegativeInt, AnyHttpUrl
from typing import Dict, List

from v1.schemas.common import BoolStr

class SpeciesItem(BaseModel):
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

class SpeciesList(BaseModel):
    species: List[SpeciesItem]

class PokemonPayload(BaseModel):
    name: str
    max_moves: NonNegativeInt

class PokemonItem(BaseModel):
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
