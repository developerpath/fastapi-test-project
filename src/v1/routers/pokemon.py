from fastapi import APIRouter, HTTPException
from typing import Optional
from pydantic import PositiveInt

from services.http_client import HttpClient
from services.utilities import error_to_list
from v1.schemas.pokemon import SpeciesItem, SpeciesList, PokemonItem, PokemonPayload
from v1.schemas.common import BoolStr

router = APIRouter()


@router.get("/species", response_model=SpeciesList)
async def get_pokemon_list(count: PositiveInt = 20, index: Optional[PositiveInt] = None):
    url = "https://pokeapi.co/api/v2/pokemon-species"
    offset = index * count if index else 0
    params = {"limit": count, "offset": offset}

    client = HttpClient()
    data = await client.get(url, params)

    if data.get('error', None):
        raise HTTPException(status_code=500, detail=error_to_list(str(data['error'])))

    urls = [itm["url"] for itm in data["results"]]
    aggregated_response = await client.make_requests(urls)
    await client.close()

    species_computed = []
    for itm in aggregated_response:
        try:
            item = SpeciesItem(
                id = itm["id"],
                image = f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{itm['id']:03}.png",
                name = itm["name"],
                base_happiness = itm["base_happiness"],
                capture_rate = itm["capture_rate"],
                colors = [itm["color"]["name"]],
                growth_rates = [itm["growth_rate"]["name"]],
                habitats = [itm["habitat"]["name"]],
                is_legendary = BoolStr.true if itm["is_legendary"] else BoolStr.false,
                egg_groups = [itm["name"] for itm in itm["egg_groups"]],
                shapes = [itm["shape"]["name"]]
            )
            species_computed.append(item)
        except Exception as e:
            raise HTTPException(status_code=500, detail=error_to_list(str(e)))

    return {"species": species_computed}


@router.post("/pokemon", response_model=PokemonItem)
async def fetch_pokemon_details(payload: PokemonPayload):
    name = payload.name.lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"

    client = HttpClient()
    data = await client.get(url)
    await client.close()

    if data.get('error', None):
        raise HTTPException(status_code=500, detail=error_to_list(str(data['error'])))

    try:
        item = PokemonItem(
            name = data["name"],
            abilities = [ability["ability"]["name"] for ability in data["abilities"]],
            base_experience = data["base_experience"],
            forms = [form["name"] for form in data["forms"]],
            height = data["height"],
            weight = data["weight"],
            moves = [move["move"]["name"] for idx, move in enumerate(data["moves"]) if idx < payload.max_moves],
            sprites = {k: v for k, v in data["sprites"].items() if isinstance(v, str) and v.startswith("http")}
        )
        return item
    except Exception as e:
        raise HTTPException(status_code=500, detail=error_to_list(str(e)))
