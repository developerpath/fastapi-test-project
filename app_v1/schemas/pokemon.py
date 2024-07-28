from pydantic import BaseModel, ConfigDict, PositiveInt, NonNegativeInt, AnyHttpUrl
from typing import Dict, List

from app_v1.schemas.common import BoolStr


class SpeciesItem(BaseModel):
    model_config = ConfigDict(str_to_lower=True)

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


class SpeciesList(BaseModel):
    species: List[SpeciesItem]


class PokemonPayload(BaseModel):
    name: str
    max_moves: NonNegativeInt


class PokemonItem(BaseModel):
    model_config = ConfigDict(str_to_lower=True)

    name: str
    abilities: List[str]
    base_experience: NonNegativeInt
    forms: List[str]
    height: NonNegativeInt
    weight: NonNegativeInt
    moves: List[str]
    sprites: Dict[str, AnyHttpUrl]
