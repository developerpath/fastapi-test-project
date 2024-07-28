from fastapi import APIRouter, HTTPException

from v1.schemas.pokemon import PokemonItem, PokemonList
from v1.schemas.common import BoolStr
from services.http_client import HttpClient

# from enum import Enum

from typing import (
    Deque, Dict, FrozenSet, List, Optional, Sequence, Set, Tuple, Union, Literal, Any
)

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
    AnyHttpUrl,
    Json
)

router = APIRouter()

data = {'count': 1025, 'next': 'https://pokeapi.co/api/v2/pokemon-species?offset=20&limit=20', 'previous': None, 'results': [{'name': 'bulbasaur', 'url': 'https://pokeapi.co/api/v2/pokemon-species/1/'}, {'name': 'ivysaur', 'url': 'https://pokeapi.co/api/v2/pokemon-species/2/'}, {'name': 'venusaur', 'url': 'https://pokeapi.co/api/v2/pokemon-species/3/'}, {'name': 'charmander', 'url': 'https://pokeapi.co/api/v2/pokemon-species/4/'}, {'name': 'charmeleon', 'url': 'https://pokeapi.co/api/v2/pokemon-species/5/'}, {'name': 'charizard', 'url': 'https://pokeapi.co/api/v2/pokemon-species/6/'}, {'name': 'squirtle', 'url': 'https://pokeapi.co/api/v2/pokemon-species/7/'}, {'name': 'wartortle', 'url': 'https://pokeapi.co/api/v2/pokemon-species/8/'}, {'name': 'blastoise', 'url': 'https://pokeapi.co/api/v2/pokemon-species/9/'}, {'name': 'caterpie', 'url': 'https://pokeapi.co/api/v2/pokemon-species/10/'}, {'name': 'metapod', 'url': 'https://pokeapi.co/api/v2/pokemon-species/11/'}, {'name': 'butterfree', 'url': 'https://pokeapi.co/api/v2/pokemon-species/12/'}, {'name': 'weedle', 'url': 'https://pokeapi.co/api/v2/pokemon-species/13/'}, {'name': 'kakuna', 'url': 'https://pokeapi.co/api/v2/pokemon-species/14/'}, {'name': 'beedrill', 'url': 'https://pokeapi.co/api/v2/pokemon-species/15/'}, {'name': 'pidgey', 'url': 'https://pokeapi.co/api/v2/pokemon-species/16/'}, {'name': 'pidgeotto', 'url': 'https://pokeapi.co/api/v2/pokemon-species/17/'}, {'name': 'pidgeot', 'url': 'https://pokeapi.co/api/v2/pokemon-species/18/'}, {'name': 'rattata', 'url': 'https://pokeapi.co/api/v2/pokemon-species/19/'}, {'name': 'raticate', 'url': 'https://pokeapi.co/api/v2/pokemon-species/20/'}]}
aggregated_response = [
    {
      "base_happiness": 50,
      "capture_rate": 45,
      "color": {
        "name": "green",
        "url": "https://pokeapi.co/api/v2/pokemon-color/5/"
      },
      "egg_groups": [
        {
          "name": "monster",
          "url": "https://pokeapi.co/api/v2/egg-group/1/"
        },
        {
          "name": "plant",
          "url": "https://pokeapi.co/api/v2/egg-group/7/"
        }
      ],
      "evolution_chain": {
        "url": "https://pokeapi.co/api/v2/evolution-chain/1/"
      },
      "evolves_from_species": None,
      "flavor_text_entries": [
        {
          "flavor_text": "A strange seed was\nplanted on its\nback at birth.\fThe plant sprouts\nand grows with\nthis POKéMON.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "red",
            "url": "https://pokeapi.co/api/v2/version/1/"
          }
        },
        {
          "flavor_text": "A strange seed was\nplanted on its\nback at birth.\fThe plant sprouts\nand grows with\nthis POKéMON.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "blue",
            "url": "https://pokeapi.co/api/v2/version/2/"
          }
        },
        {
          "flavor_text": "It can go for days\nwithout eating a\nsingle morsel.\fIn the bulb on\nits back, it\nstores energy.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version/3/"
          }
        },
        {
          "flavor_text": "The seed on its\nback is filled\nwith nutrients.\fThe seed grows\nsteadily larger as\nits body grows.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "gold",
            "url": "https://pokeapi.co/api/v2/version/4/"
          }
        },
        {
          "flavor_text": "It carries a seed\non its back right\nfrom birth. As it\fgrows older, the\nseed also grows\nlarger.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "silver",
            "url": "https://pokeapi.co/api/v2/version/5/"
          }
        },
        {
          "flavor_text": "While it is young,\nit uses the\nnutrients that are\fstored in the\nseeds on its back\nin order to grow.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version/6/"
          }
        },
        {
          "flavor_text": "BULBASAUR can be seen napping in\nbright sunlight.\nThere is a seed on its back.\fBy soaking up the sun’s rays, the seed\ngrows progressively larger.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "ruby",
            "url": "https://pokeapi.co/api/v2/version/7/"
          }
        },
        {
          "flavor_text": "BULBASAUR can be seen napping in\nbright sunlight.\nThere is a seed on its back.\fBy soaking up the sun’s rays, the seed\ngrows progressively larger.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sapphire",
            "url": "https://pokeapi.co/api/v2/version/8/"
          }
        },
        {
          "flavor_text": "BULBASAUR can be seen napping in bright\nsunlight. There is a seed on its back.\nBy soaking up the sun’s rays, the seed\ngrows progressively larger.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version/9/"
          }
        },
        {
          "flavor_text": "There is a plant seed on its back right\nfrom the day this POKéMON is born.\nThe seed slowly grows larger.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "firered",
            "url": "https://pokeapi.co/api/v2/version/10/"
          }
        },
        {
          "flavor_text": "A strange seed was planted on its back at\nbirth. The plant sprouts and grows with\nthis POKéMON.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "leafgreen",
            "url": "https://pokeapi.co/api/v2/version/11/"
          }
        },
        {
          "flavor_text": "For some time after its birth, it\ngrows by gaining nourishment from\nthe seed on its back.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "diamond",
            "url": "https://pokeapi.co/api/v2/version/12/"
          }
        },
        {
          "flavor_text": "For some time after its birth, it\ngrows by gaining nourishment from\nthe seed on its back.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "pearl",
            "url": "https://pokeapi.co/api/v2/version/13/"
          }
        },
        {
          "flavor_text": "For some time after its birth, it\ngrows by gaining nourishment from\nthe seed on its back.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version/14/"
          }
        },
        {
          "flavor_text": "The seed on its back is filled\nwith nutrients. The seed grows\nsteadily larger as its body grows.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "heartgold",
            "url": "https://pokeapi.co/api/v2/version/15/"
          }
        },
        {
          "flavor_text": "It carries a seed on its back right\nfrom birth. As it grows older, the\nseed also grows larger.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "soulsilver",
            "url": "https://pokeapi.co/api/v2/version/16/"
          }
        },
        {
          "flavor_text": "Au matin de sa vie, la graine sur\nson dos lui fournit les éléments\ndont il a besoin pour grandir.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "For some time after its birth, it\ngrows by gaining nourishment from\nthe seed on its back.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "Au matin de sa vie, la graine sur\nson dos lui fournit les éléments\ndont il a besoin pour grandir.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "For some time after its birth, it\ngrows by gaining nourishment from\nthe seed on its back.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "For some time after its birth, it\ngrows by gaining nourishment from\nthe seed on its back.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black-2",
            "url": "https://pokeapi.co/api/v2/version/21/"
          }
        },
        {
          "flavor_text": "For some time after its birth, it\ngrows by gaining nourishment from\nthe seed on its back.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white-2",
            "url": "https://pokeapi.co/api/v2/version/22/"
          }
        },
        {
          "flavor_text": "うまれたときから　せなかに\nふしぎな　タネが　うえてあって\nからだと　ともに　そだつという。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "태어났을 때부터 등에\n이상한 씨앗이 심어져 있으며\n몸과 함께 자란다고 한다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Il a une étrange graine plantée sur son dos.\nElle grandit avec lui depuis sa naissance.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Dieses Pokémon trägt von Geburt an einen Samen\nauf dem Rücken, der mit ihm keimt und wächst.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Una rara semilla le fue plantada en el lomo al nacer.\nLa planta brota y crece con este Pokémon.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Alla nascita gli è stato piantato sulla schiena un seme\nraro. La pianta sboccia e cresce con lui.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "A strange seed was planted on its back at birth.\nThe plant sprouts and grows with this Pokémon.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "生まれたときから　背中に\n不思議な　タネが　植えてあって\n体と　ともに　育つという。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "うまれてから　しばらくの　あいだは\nせなかの　タネから　えいようを\nもらって　おおきく　そだつ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "태어나서부터 얼마 동안은\n등의 씨앗으로부터 영양을\n공급받아 크게 성장한다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Au matin de sa vie, la graine sur son dos lui fournit\nles éléments dont il a besoin pour grandir.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Nach der Geburt nimmt es für eine Weile Nährstoffe\nüber den Samen auf seinem Rücken auf.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Después de nacer, crece alimentándose de las\nsemillas de su lomo.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Dopo la nascita, cresce traendo nutrimento dal seme\npiantato sul suo dorso.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "For some time after its birth, it grows by gaining\nnourishment from the seed on its back.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "生まれてから　しばらくの　あいだは\n背中の　タネから　栄養を　もらって\n大きく　育つ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "ひなたで　ひるねを　する　すがたを　みかける。\nたいようの　ひかりを　いっぱい　あびることで\nせなかの　タネが　おおきく　そだつのだ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "양지에서 낮잠 자는 모습을 볼 수 있다.\n태양의 빛을 많이 받으면\n등의 씨앗이 크게 자란다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Bulbizarre passe son temps à faire la sieste sous le soleil.\nIl y a une graine sur son dos. Il absorbe les rayons du soleil\npour faire doucement pousser la graine.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Bisasam macht gern einmal ein Nickerchen im\nSonnenschein. Auf seinem Rücken trägt es einen\nSamen. Indem es Sonnenstrahlen aufsaugt,\nwird der Samen zunehmend größer.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "A Bulbasaur es fácil verle echándose una siesta al sol.\nLa semilla que tiene en el lomo va creciendo cada vez más\na medida que absorbe los rayos del sol.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "È possibile vedere Bulbasaur mentre schiaccia un pisolino\nsotto il sole. Ha un seme piantato sulla schiena. Grazie ai\nraggi solari il seme cresce ingrandendosi progressivamente.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Bulbasaur can be seen napping in bright sunlight.\nThere is a seed on its back. By soaking up the sun’s rays,\nthe seed grows progressively larger.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "日なたで　昼寝を　する　姿を　見かける。\n太陽の　光を　いっぱい　浴びることで\n背中の　タネが　大きく　育つのだ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "ひなたで　ひるねを　する　すがたを　みかける。\nたいようの　ひかりを　いっぱい　あびることで\nせなかの　タネが　おおきく　そだつのだ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "양지에서 낮잠 자는 모습을 볼 수 있다.\n태양의 빛을 많이 받으면\n등의 씨앗이 크게 자란다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Bulbizarre passe son temps à faire la sieste sous le soleil.\nIl y a une graine sur son dos. Il absorbe les rayons du soleil\npour faire doucement pousser la graine.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Bisasam macht gern einmal ein Nickerchen im\nSonnenschein. Auf seinem Rücken trägt es einen\nSamen. Indem es Sonnenstrahlen aufsaugt,\nwird er zunehmend größer.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "A Bulbasaur es fácil verle echándose una siesta al sol.\nLa semilla que tiene en el lomo va creciendo cada vez más\na medida que absorbe los rayos del sol.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "È possibile vedere Bulbasaur mentre schiaccia un pisolino\nsotto il sole. Ha un seme piantato sulla schiena. Grazie ai\nraggi solari il seme cresce ingrandendosi progressivamente.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Bulbasaur can be seen napping in bright sunlight.\nThere is a seed on its back. By soaking up the sun’s rays,\nthe seed grows progressively larger.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "日なたで　昼寝を　する　姿を　見かける。\n太陽の　光を　いっぱい　浴びることで\n背中の　タネが　大きく　育つのだ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "なんにちだって　なにも　たべなくても\nげんき！　せなかのタネに　たくさん\nえいようが　あるから　へいきだ！",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "며칠 동안 아무것도 먹지 않아도\n건강하다! 등에 있는 씨앗에는\n많은 영양분이 있어서 문제없다!",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "背上的種子裡存著很多營養，\n所以就算好幾天不吃東西\n也能活得好好的！",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Il peut survivre plusieurs jours sans manger\ngrâce aux nutriments contenus dans le bulbe\nsur son dos.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Es kommt tagelang ohne Nahrung aus, da es\nin den Samen auf seinem Rücken Nährstoffe\nspeichert.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Puede sobrevivir largo tiempo sin probar\nbocado gracias a los nutrientes que guarda\nen el bulbo del lomo.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Questo Pokémon può stare a lungo senza\nmangiare. Accumula energia nel bulbo che\nha sulla schiena.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "It can go for days without eating a single morsel.\nIn the bulb on its back, it stores energy.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "何日だって　なにも　食べなくても\n元気！　背中のタネに　たくさん\n栄養が　あるから　平気だ！",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "背上的种子里储存着营养，\n所以即使好几天不吃东西\n也可以活得好好的！",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "なんにちだって　なにも　たべなくても\nげんき！　せなかのタネに　たくさん\nえいようが　あるから　へいきだ！",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "며칠 동안 아무것도 먹지 않아도\n건강하다! 등에 있는 씨앗에는\n많은 영양분이 있어서 문제없다!",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "背上的種子裡存著很多營養，\n所以就算好幾天不吃東西\n也能活得好好的！",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Il peut survivre plusieurs jours sans manger\ngrâce aux nutriments contenus dans le bulbe\nsur son dos.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Es kommt tagelang ohne Nahrung aus, da es\nin den Samen auf seinem Rücken Nährstoffe\nspeichert.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Puede sobrevivir largo tiempo sin probar\nbocado gracias a los nutrientes que guarda\nen el bulbo del lomo.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Questo Pokémon può stare a lungo senza\nmangiare. Accumula energia nel bulbo che\nha sulla schiena.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "It can go for days without eating a single morsel.\nIn the bulb on its back, it stores energy.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "何日だって　なにも　食べなくても\n元気！　背中のタネに　たくさん\n栄養が　あるから　平気だ！",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "背上的种子里储存着营养，\n所以即使好几天不吃东西\n也可以活得好好的！",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "うまれたときから　せなかに\nしょくぶつの　タネが　あって\nすこしずつ　おおきく　そだつ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "태어났을 때부터 등에\n식물의 씨앗이 있으며\n조금씩 크게 자란다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "從出生的時候開始\n背上就有一顆植物種子。\n這顆種子會漸漸地長大。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Il y a une graine sur son dos depuis sa naissance.\nElle grossit un peu chaque jour.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Dieses Pokémon trägt von Geburt an einen\nSamen auf dem Rücken, der im Laufe der Zeit\nkeimt und wächst.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Este Pokémon nace con una semilla en el lomo,\nque brota con el paso del tiempo.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Fin dalla nascita questo Pokémon ha sulla schiena\nun seme che cresce lentamente.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "There is a plant seed on its back right from the\nday this Pokémon is born. The seed slowly\ngrows larger.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "生まれたときから　背中に\n植物の　タネが　あって\n少しずつ　大きく　育つ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "从出生的时候开始，\n背上就有一颗植物种子。\n这颗种子会渐渐地长大。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "うまれて　しばらくの　あいだ\nせなかの　タネに　つまった\nえいようを　とって　そだつ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "태어나서 얼마 동안\n등의 씨앗에 담긴\n영양을 섭취하며 자란다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "在出生後的一段時間內，\n牠會吸收背上種子裡\n儲存著的營養成長。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Quand il est jeune, il absorbe les nutriments\nconservés dans son dos pour grandir\net se développer.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Nach der Geburt nimmt es für eine Weile\nNährstoffe über den Samen auf seinem\nRücken auf.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Desde que nace, crece alimentándose de los\nnutrientes que contiene la semilla de su lomo.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Appena nato, trae nutrimento dalle sostanze\ncontenute nel seme sul dorso.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "While it is young, it uses the nutrients that are\nstored in the seed on its back in order to grow.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "生まれて　しばらくの　あいだ\n背中の　タネに　つまった\n栄養を　とって　育つ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "在出生后的一段时间内，\n它会吸收背上种子里\n储存着的营养成长。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        }
      ],
      "form_descriptions": [],
      "forms_switchable": False,
      "gender_rate": 1,
      "genera": [
        {
          "genus": "たねポケモン",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          }
        },
        {
          "genus": "씨앗포켓몬",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          }
        },
        {
          "genus": "種子寶可夢",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          }
        },
        {
          "genus": "Pokémon Graine",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          }
        },
        {
          "genus": "Samen-Pokémon",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        },
        {
          "genus": "Pokémon Semilla",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          }
        },
        {
          "genus": "Pokémon Seme",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          }
        },
        {
          "genus": "Seed Pokémon",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        },
        {
          "genus": "たねポケモン",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          }
        },
        {
          "genus": "种子宝可梦",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          }
        }
      ],
      "generation": {
        "name": "generation-i",
        "url": "https://pokeapi.co/api/v2/generation/1/"
      },
      "growth_rate": {
        "name": "medium-slow",
        "url": "https://pokeapi.co/api/v2/growth-rate/4/"
      },
      "habitat": {
        "name": "grassland",
        "url": "https://pokeapi.co/api/v2/pokemon-habitat/3/"
      },
      "has_gender_differences": False,
      "hatch_counter": 20,
      "id": 1,
      "is_baby": False,
      "is_legendary": False,
      "is_mythical": False,
      "name": "bulbasaur",
      "names": [
        {
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "name": "フシギダネ"
        },
        {
          "language": {
            "name": "roomaji",
            "url": "https://pokeapi.co/api/v2/language/2/"
          },
          "name": "Fushigidane"
        },
        {
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "name": "이상해씨"
        },
        {
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "name": "妙蛙種子"
        },
        {
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "name": "Bulbizarre"
        },
        {
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "name": "Bisasam"
        },
        {
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "name": "Bulbasaur"
        },
        {
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "name": "Bulbasaur"
        },
        {
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "name": "Bulbasaur"
        },
        {
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "name": "フシギダネ"
        },
        {
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "name": "妙蛙种子"
        }
      ],
      "order": 1,
      "pal_park_encounters": [
        {
          "area": {
            "name": "field",
            "url": "https://pokeapi.co/api/v2/pal-park-area/2/"
          },
          "base_score": 50,
          "rate": 30
        }
      ],
      "pokedex_numbers": [
        {
          "entry_number": 1,
          "pokedex": {
            "name": "national",
            "url": "https://pokeapi.co/api/v2/pokedex/1/"
          }
        },
        {
          "entry_number": 1,
          "pokedex": {
            "name": "kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/2/"
          }
        },
        {
          "entry_number": 226,
          "pokedex": {
            "name": "original-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/3/"
          }
        },
        {
          "entry_number": 231,
          "pokedex": {
            "name": "updated-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/7/"
          }
        },
        {
          "entry_number": 80,
          "pokedex": {
            "name": "kalos-central",
            "url": "https://pokeapi.co/api/v2/pokedex/12/"
          }
        },
        {
          "entry_number": 1,
          "pokedex": {
            "name": "letsgo-kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/26/"
          }
        },
        {
          "entry_number": 68,
          "pokedex": {
            "name": "isle-of-armor",
            "url": "https://pokeapi.co/api/v2/pokedex/28/"
          }
        },
        {
          "entry_number": 164,
          "pokedex": {
            "name": "blueberry",
            "url": "https://pokeapi.co/api/v2/pokedex/33/"
          }
        }
      ],
      "shape": {
        "name": "quadruped",
        "url": "https://pokeapi.co/api/v2/pokemon-shape/8/"
      },
      "varieties": [
        {
          "is_default": True,
          "pokemon": {
            "name": "bulbasaur",
            "url": "https://pokeapi.co/api/v2/pokemon/1/"
          }
        }
      ]
    },
    {
      "base_happiness": 50,
      "capture_rate": 45,
      "color": {
        "name": "green",
        "url": "https://pokeapi.co/api/v2/pokemon-color/5/"
      },
      "egg_groups": [
        {
          "name": "monster",
          "url": "https://pokeapi.co/api/v2/egg-group/1/"
        },
        {
          "name": "plant",
          "url": "https://pokeapi.co/api/v2/egg-group/7/"
        }
      ],
      "evolution_chain": {
        "url": "https://pokeapi.co/api/v2/evolution-chain/1/"
      },
      "evolves_from_species": {
        "name": "bulbasaur",
        "url": "https://pokeapi.co/api/v2/pokemon-species/1/"
      },
      "flavor_text_entries": [
        {
          "flavor_text": "When the bulb on\nits back grows\nlarge, it appears\fto lose the\nability to stand\non its hind legs.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "red",
            "url": "https://pokeapi.co/api/v2/version/1/"
          }
        },
        {
          "flavor_text": "When the bulb on\nits back grows\nlarge, it appears\fto lose the\nability to stand\non its hind legs.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "blue",
            "url": "https://pokeapi.co/api/v2/version/2/"
          }
        },
        {
          "flavor_text": "The bulb on its\nback grows by\ndrawing energy.\fIt gives off an\naroma when it is\nready to bloom.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version/3/"
          }
        },
        {
          "flavor_text": "Exposure to sun­\nlight adds to its\nstrength. Sunlight\falso makes the bud\non its back grow\nlarger.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "gold",
            "url": "https://pokeapi.co/api/v2/version/4/"
          }
        },
        {
          "flavor_text": "If the bud on its\nback starts to\nsmell sweet, it\fis evidence that\nthe large flower\nwill soon bloom.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "silver",
            "url": "https://pokeapi.co/api/v2/version/5/"
          }
        },
        {
          "flavor_text": "The bulb on its\nback grows as it\nabsorbs nutrients.\fThe bulb gives off\na pleasant aroma\nwhen it blooms.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version/6/"
          }
        },
        {
          "flavor_text": "There is a bud on this POKéMON’s back.\nTo support its weight, IVYSAUR’s legs\nand trunk grow thick and strong.\fIf it starts spending more time lying\nin the sunlight, it’s a sign that the\nbud will bloom into a large flower soon.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "ruby",
            "url": "https://pokeapi.co/api/v2/version/7/"
          }
        },
        {
          "flavor_text": "There is a bud on this POKéMON’s back.\nTo support its weight, IVYSAUR’s legs\nand trunk grow thick and strong.\fIf it starts spending more time lying\nin the sunlight, it’s a sign that the\nbud will bloom into a large flower soon.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sapphire",
            "url": "https://pokeapi.co/api/v2/version/8/"
          }
        },
        {
          "flavor_text": "To support its bulb, IVYSAUR’s legs\ngrow sturdy. If it spends more time lying in\nthe sunlight, the bud will soon bloom into\na large flower.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version/9/"
          }
        },
        {
          "flavor_text": "There is a plant bulb on its back.\nWhen it absorbs nutrients, the bulb is said\nto blossom into a large flower.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "firered",
            "url": "https://pokeapi.co/api/v2/version/10/"
          }
        },
        {
          "flavor_text": "When the bulb on its back grows large, it\nappears to lose the ability to stand on\nits hind legs.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "leafgreen",
            "url": "https://pokeapi.co/api/v2/version/11/"
          }
        },
        {
          "flavor_text": "When the bud on its back starts\nswelling, a sweet aroma wafts to\nindicate the flower’s coming bloom.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "diamond",
            "url": "https://pokeapi.co/api/v2/version/12/"
          }
        },
        {
          "flavor_text": "When the bud on its back starts\nswelling, a sweet aroma wafts to\nindicate the flower’s coming bloom.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "pearl",
            "url": "https://pokeapi.co/api/v2/version/13/"
          }
        },
        {
          "flavor_text": "When the bud on its back starts\nswelling, a sweet aroma wafts to\nindicate the flower’s coming bloom.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version/14/"
          }
        },
        {
          "flavor_text": "Exposure to sunlight adds to its\nstrength. Sunlight also makes the\nbud on its back grow larger.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "heartgold",
            "url": "https://pokeapi.co/api/v2/version/15/"
          }
        },
        {
          "flavor_text": "If the bud on its back starts to\nsmell sweet, it is evidence that\nthe large flower will soon bloom.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "soulsilver",
            "url": "https://pokeapi.co/api/v2/version/16/"
          }
        },
        {
          "flavor_text": "Lorsque le bourgeon sur son dos\néclot, il répand un doux parfum\npour célébrer sa floraison.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "When the bud on its back starts\nswelling, a sweet aroma wafts to\nindicate the flower’s coming bloom.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "Lorsque le bourgeon sur son dos\néclot, il répand un doux parfum\npour célébrer sa floraison.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "When the bud on its back starts\nswelling, a sweet aroma wafts to\nindicate the flower’s coming bloom.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "When the bud on its back starts\nswelling, a sweet aroma wafts to\nindicate the flower’s coming bloom.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black-2",
            "url": "https://pokeapi.co/api/v2/version/21/"
          }
        },
        {
          "flavor_text": "When the bud on its back starts\nswelling, a sweet aroma wafts to\nindicate the flower’s coming bloom.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white-2",
            "url": "https://pokeapi.co/api/v2/version/22/"
          }
        },
        {
          "flavor_text": "つぼみが　せなかに　ついていて\nようぶんを　きゅうしゅうしていくと\nおおきな　はなが　さくという。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "꽃봉오리가 등에 붙어 있으며\n양분을 흡수해가면\n커다란 꽃이 핀다고 한다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Il y a un bulbe sur son dos. On dit que s’il absorbe\nassez de nutriments, ce bulbe se transforme en\nune jolie fleur.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Es trägt eine Knospe auf seinem Rücken. Nimmt es\nNahrung zu sich, soll aus der Knospe eine große\nblühende Blume werden.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Este Pokémon tiene un bulbo en el lomo. Dicen que,\nal absorber nutrientes, el bulbo se transforma en una\nflor grande.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Dopo aver assorbito sufficienti sostanze nutrienti,\nil bulbo sulla schiena sboccia in un magnifico fiore.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "There is a plant bulb on its back.\nWhen it absorbs nutrients, the bulb is said to\nblossom into a large flower.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "つぼみが　背中に　ついていて\n養分を　吸収していくと\n大きな　花が　咲くという。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "せなかの　つぼみが　ふくらみだすと\nあまい　においが　ただよいはじめる。\nたいりんの　はなが　さく　まえぶれ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "등의 봉오리가 부풀어 오르면\n달콤한 냄새가 감돌기 시작한다.\n큰 꽃이 필 조짐이다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Lorsque le bourgeon sur son dos éclot, il répand\nun doux parfum pour célébrer sa floraison.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Sobald die Knospe auf seinem Rücken ein süßes\nAroma abgibt, steht die Blüte kurz bevor.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Cuando el bulbo de su lomo se hincha, desprende un\ndulce aroma para indicar el florecimiento.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Quando il bocciolo che ha sul dorso si gonfia, emana\nun dolce profumo. È indice dell’imminente fioritura.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "When the bud on its back starts swelling, a sweet\naroma wafts to indicate the flower’s coming bloom.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "背中の　つぼみが　ふくらみ出すと\n甘い　においが　漂いはじめる。\n大輪の　花が　咲く　前触れ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "つぼみを　ささえるため　あしこしが　つよくなる。\nひなたで　じっとする　じかんが　ながくなれば\nいよいよ　たいりんの　はなが　さくころだ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "꽃봉오리를 지탱하기 위해 하반신이 강해진다.\n양지에서 가만히 있는 시간이 길어지면\n드디어 커다란 꽃이 필 때다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Un bourgeon a poussé sur le dos de ce Pokémon. Pour en\nsupporter le poids, Herbizarre a dû se muscler les pattes.\nLorsqu’il commence à se prélasser au soleil, ça signifie que\nson bourgeon va éclore, donnant naissance à une fleur.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Bisaknosp hat eine Knospe auf seinem Rücken.\nBeine und Rumpf sind kräftig genug, um sein Gewicht\nzu tragen. Wenn es lange in der Sonne liegt, ist das\nein Anzeichen dafür, dass die Knospe bald blüht.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Este Pokémon lleva un bulbo en el lomo y, para poder con\nsu peso, tiene unas patas y un tronco gruesos y fuertes.\nSi empieza a pasar más tiempo al sol, será porque el bulbo\nestá a punto de hacerse una flor grande.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "C’è un germoglio piantato nella schiena di Ivysaur.\nPer sopportarne il peso, le zampe e il corpo crescono robusti.\nQuando inizia a passare più tempo esposto al sole, significa\nche il germoglio sboccerà presto in un grande fiore.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "There is a bud on this Pokémon’s back. To support its weight,\nIvysaur’s legs and trunk grow thick and strong.\nIf it starts spending more time lying in the sunlight,\nit’s a sign that the bud will bloom into a large flower soon.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "つぼみを　支えるため　足腰が　強くなる。\n日なたで　じっとする　時間が　長くなれば\nいよいよ　大輪の　花が　咲くころだ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "つぼみを　ささえるため　あしこしが　つよくなる。\nひなたで　じっとする　じかんが　ながくなれば\nいよいよ　たいりんの　はなが　さくころだ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "꽃봉오리를 지탱하기 위해 하반신이 강해진다.\n양지에서 가만히 있는 시간이 길어지면\n드디어 커다란 꽃이 필 때다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Un bourgeon a poussé sur le dos de ce Pokémon. Pour en\nsupporter le poids, Herbizarre a dû se muscler les pattes.\nLorsqu’il commence à se prélasser au soleil, ça signifie que\nson bourgeon va éclore, donnant naissance à une fleur.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Bisaknosp hat eine Knospe auf seinem Rücken. Seine Beine\nund sein Stamm sind kräftig genug, um sein Gewicht zu tragen.\nWenn es lange in der Sonne liegt, ist das ein Anzeichen dafür,\ndass die Knospe bald blüht.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Este Pokémon lleva un bulbo en el lomo y, para poder con\nsu peso, tiene unas patas y un tronco gruesos y fuertes.\nSi empieza a pasar más tiempo al sol, será porque el bulbo\nestá a punto de hacerse una flor grande.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "C’è un germoglio piantato nella schiena di Ivysaur.\nPer sopportarne il peso, le zampe e il corpo crescono robusti.\nQuando inizia a passare più tempo esposto al sole, significa\nche il germoglio sboccerà presto in un grande fiore.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "There is a bud on this Pokémon’s back. To support its weight,\nIvysaur’s legs and trunk grow thick and strong.\nIf it starts spending more time lying in the sunlight,\nit’s a sign that the bud will bloom into a large flower soon.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "つぼみを　支えるため　足腰が　強くなる。\n日なたで　じっとする　時間が　長くなれば\nいよいよ　大輪の　花が　咲くころだ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "ようぶんを　とって　おおきくなった\nつぼみから　かおりが　ただよいだすと\nもうすぐ　ハナがひらく　しょうこだ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "양분을 흡수해서 커진 봉오리에서\n향기가 나기 시작하면\n곧 꽃이 핀다는 증거다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "在吸收了養分後，\n變大的花苞開始飄出香氣時，\n就表示快要開花了。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "En emmagasinant de l’énergie, son bulbe grossit.\nUn arôme en émane quand il s’apprête à éclore.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Die Knospe auf seinem Rücken wächst, indem\nsie Nährstoffe absorbiert. Kurz vor der Blüte\nsondert sie einen Duft ab.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Su bulbo crece a medida que absorbe nutrientes.\nDesprende un cierto aroma cuando está a punto\nde florecer.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Il suo bocciolo cresce assorbendo nutrimento e,\nquando è prossimo alla fioritura, emana un\nforte profumo.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "The bud on its back grows by drawing energy. It\ngives off an aroma when it is ready to bloom.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "養分を　摂って　大きくなった\nつぼみから　香りが　漂いだすと\nもうすぐ　ハナが開く　証拠だ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "它的花苞会在吸收养分后\n长大。当花苞发出香味时，\n就预示着它快要开花了。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "ようぶんを　とって　おおきくなった\nつぼみから　かおりが　ただよいだすと\nもうすぐ　ハナがひらく　しょうこだ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "양분을 흡수해서 커진 봉오리에서\n향기가 나기 시작하면\n곧 꽃이 핀다는 증거다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "在吸收了養分後，\n變大的花苞開始飄出香氣時，\n就表示快要開花了。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "En emmagasinant de l’énergie, son bulbe grossit.\nUn arôme en émane quand il s’apprête à éclore.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Die Knospe auf seinem Rücken wächst, indem\nsie Nährstoffe absorbiert. Kurz vor der Blüte\nsondert sie einen Duft ab.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Su bulbo crece a medida que absorbe nutrientes.\nDesprende un cierto aroma cuando está a punto\nde florecer.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Il suo bocciolo cresce assorbendo nutrimento e,\nquando è prossimo alla fioritura, emana un\nforte profumo.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "The bud on its back grows by drawing energy. It\ngives off an aroma when it is ready to bloom.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "養分を　摂って　大きくなった\nつぼみから　香りが　漂いだすと\nもうすぐ　ハナが開く　証拠だ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "它的花苞会在吸收养分后\n长大。当花苞发出香味时，\n就预示着它快要开花了。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "せなかの　つぼみが　おおきく\nそだってくると　２ほんあしで\nたつことが　できなくなるらしい。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "등에 있는 봉오리가 크게\n자라면 두 다리로\n설 수 없게 되는 듯하다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "當背上的花苞長大之後，\n牠似乎就無法再用兩隻腳\n站立起來了。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Son bulbe dorsal est devenu si gros qu’il ne peut\nplus se tenir sur ses pattes postérieures.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Sobald die Knospe auf seinem Rücken groß wird,\nkann Bisaknosp nicht mehr auf zwei Beinen\nstehen.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Cuando le crece bastante el bulbo del lomo,\npierde la capacidad de erguirse sobre las patas\ntraseras.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Il bulbo sulla schiena è cresciuto così tanto\nda impedirgli di alzarsi in piedi sulle zampe\nposteriori.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "When the bulb on its back grows large, it\nappears to lose the ability to stand on its\nhind legs.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "背中の　つぼみが　大きく\n育ってくると　２本脚で\n立つことが　できなくなるらしい。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "当背上的花苞长大之后，\n它似乎就无法再用两只脚\n站立起来了。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "たいようの　ひかりを　あびるほど\nからだに　ちからが　わいて　せなかの\nつぼみが　そだっていく。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "햇빛을 받을수록\n몸에 힘이 솟아나\n등의 꽃봉오리가 자라난다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "沐浴在陽光下越久，\n身體內會湧出越多力量，\n背上的花苞也會漸漸成長。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "La lumière du soleil le rend plus fort et vigoureux.\nLe bulbe sur son dos grossit en conséquence.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Die Sonne macht es stärker. Die Knospe auf\nseinem Rücken wächst unter dem Einfluss von\nSonnenlicht.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "La luz del sol lo fortalece y hace que le crezca el\ncapullo que tiene en el lomo.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "L’esposizione alla luce solare lo rafforza\ne fa crescere il bocciolo che ha sul dorso.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Exposure to sunlight adds to its strength.\nSunlight also makes the bud on its back\ngrow larger.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "太陽の　光を　浴びるほど\n体に　力が　わいて　背中の\nつぼみが　育っていく。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "沐浴在阳光下越久，\n身体内会涌出越多力量，\n背上的花苞也会渐渐成长。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        }
      ],
      "form_descriptions": [],
      "forms_switchable": False,
      "gender_rate": 1,
      "genera": [
        {
          "genus": "たねポケモン",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          }
        },
        {
          "genus": "씨앗포켓몬",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          }
        },
        {
          "genus": "種子寶可夢",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          }
        },
        {
          "genus": "Pokémon Graine",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          }
        },
        {
          "genus": "Samen-Pokémon",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        },
        {
          "genus": "Pokémon Semilla",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          }
        },
        {
          "genus": "Pokémon Seme",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          }
        },
        {
          "genus": "Seed Pokémon",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        },
        {
          "genus": "たねポケモン",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          }
        },
        {
          "genus": "种子宝可梦",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          }
        }
      ],
      "generation": {
        "name": "generation-i",
        "url": "https://pokeapi.co/api/v2/generation/1/"
      },
      "growth_rate": {
        "name": "medium-slow",
        "url": "https://pokeapi.co/api/v2/growth-rate/4/"
      },
      "habitat": {
        "name": "grassland",
        "url": "https://pokeapi.co/api/v2/pokemon-habitat/3/"
      },
      "has_gender_differences": False,
      "hatch_counter": 20,
      "id": 2,
      "is_baby": False,
      "is_legendary": False,
      "is_mythical": False,
      "name": "ivysaur",
      "names": [
        {
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "name": "フシギソウ"
        },
        {
          "language": {
            "name": "roomaji",
            "url": "https://pokeapi.co/api/v2/language/2/"
          },
          "name": "Fushigisou"
        },
        {
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "name": "이상해풀"
        },
        {
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "name": "妙蛙草"
        },
        {
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "name": "Herbizarre"
        },
        {
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "name": "Bisaknosp"
        },
        {
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "name": "Ivysaur"
        },
        {
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "name": "Ivysaur"
        },
        {
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "name": "Ivysaur"
        },
        {
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "name": "フシギソウ"
        },
        {
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "name": "妙蛙草"
        }
      ],
      "order": 2,
      "pal_park_encounters": [
        {
          "area": {
            "name": "field",
            "url": "https://pokeapi.co/api/v2/pal-park-area/2/"
          },
          "base_score": 80,
          "rate": 10
        }
      ],
      "pokedex_numbers": [
        {
          "entry_number": 2,
          "pokedex": {
            "name": "national",
            "url": "https://pokeapi.co/api/v2/pokedex/1/"
          }
        },
        {
          "entry_number": 2,
          "pokedex": {
            "name": "kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/2/"
          }
        },
        {
          "entry_number": 227,
          "pokedex": {
            "name": "original-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/3/"
          }
        },
        {
          "entry_number": 232,
          "pokedex": {
            "name": "updated-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/7/"
          }
        },
        {
          "entry_number": 81,
          "pokedex": {
            "name": "kalos-central",
            "url": "https://pokeapi.co/api/v2/pokedex/12/"
          }
        },
        {
          "entry_number": 2,
          "pokedex": {
            "name": "letsgo-kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/26/"
          }
        },
        {
          "entry_number": 69,
          "pokedex": {
            "name": "isle-of-armor",
            "url": "https://pokeapi.co/api/v2/pokedex/28/"
          }
        },
        {
          "entry_number": 165,
          "pokedex": {
            "name": "blueberry",
            "url": "https://pokeapi.co/api/v2/pokedex/33/"
          }
        }
      ],
      "shape": {
        "name": "quadruped",
        "url": "https://pokeapi.co/api/v2/pokemon-shape/8/"
      },
      "varieties": [
        {
          "is_default": True,
          "pokemon": {
            "name": "ivysaur",
            "url": "https://pokeapi.co/api/v2/pokemon/2/"
          }
        }
      ]
    },
    {
      "base_happiness": 50,
      "capture_rate": 45,
      "color": {
        "name": "green",
        "url": "https://pokeapi.co/api/v2/pokemon-color/5/"
      },
      "egg_groups": [
        {
          "name": "monster",
          "url": "https://pokeapi.co/api/v2/egg-group/1/"
        },
        {
          "name": "plant",
          "url": "https://pokeapi.co/api/v2/egg-group/7/"
        }
      ],
      "evolution_chain": {
        "url": "https://pokeapi.co/api/v2/evolution-chain/1/"
      },
      "evolves_from_species": {
        "name": "ivysaur",
        "url": "https://pokeapi.co/api/v2/pokemon-species/2/"
      },
      "flavor_text_entries": [
        {
          "flavor_text": "The plant blooms\nwhen it is\nabsorbing solar\fenergy. It stays\non the move to\nseek sunlight.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "red",
            "url": "https://pokeapi.co/api/v2/version/1/"
          }
        },
        {
          "flavor_text": "The plant blooms\nwhen it is\nabsorbing solar\fenergy. It stays\non the move to\nseek sunlight.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "blue",
            "url": "https://pokeapi.co/api/v2/version/2/"
          }
        },
        {
          "flavor_text": "The flower on its\nback catches the\nsun's rays.\fThe sunlight is\nthen absorbed and\nused for energy.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version/3/"
          }
        },
        {
          "flavor_text": "By spreading the\nbroad petals of\nits flower and\fcatching the sun's\nrays, it fills its\nbody with power.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "gold",
            "url": "https://pokeapi.co/api/v2/version/4/"
          }
        },
        {
          "flavor_text": "It is able to con­\nvert sunlight into\nenergy. As a\fresult, it is more\npowerful in the\nsummertime.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "silver",
            "url": "https://pokeapi.co/api/v2/version/5/"
          }
        },
        {
          "flavor_text": "As it warms it­\nself and absorbs\nthe sunlight, its\fflower petals\nrelease a pleasant\nfragrance.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version/6/"
          }
        },
        {
          "flavor_text": "There is a large flower on VENUSAUR’s\nback. The flower is said to take on vivid\ncolors if it gets plenty of nutrition\fand sunlight. The flower’s aroma\nsoothes the emotions of people.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "ruby",
            "url": "https://pokeapi.co/api/v2/version/7/"
          }
        },
        {
          "flavor_text": "There is a large flower on VENUSAUR’s\nback. The flower is said to take on vivid\ncolors if it gets plenty of nutrition\fand sunlight. The flower’s aroma\nsoothes the emotions of people.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sapphire",
            "url": "https://pokeapi.co/api/v2/version/8/"
          }
        },
        {
          "flavor_text": "VENUSAUR’s flower is said to take on vivid\ncolors if it gets plenty of nutrition and\nsunlight. The flower’s aroma soothes the\nemotions of people.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version/9/"
          }
        },
        {
          "flavor_text": "A bewitching aroma wafts from its flower.\nThe fragrance becalms those engaged in\na battle.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "firered",
            "url": "https://pokeapi.co/api/v2/version/10/"
          }
        },
        {
          "flavor_text": "Its plant blooms when it is absorbing\nsolar energy. It stays on the move to\nseek sunlight.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "leafgreen",
            "url": "https://pokeapi.co/api/v2/version/11/"
          }
        },
        {
          "flavor_text": "After a rainy day, the flower on\nits back smells stronger. The\nscent attracts other Pokémon.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "diamond",
            "url": "https://pokeapi.co/api/v2/version/12/"
          }
        },
        {
          "flavor_text": "After a rainy day, the flower on\nits back smells stronger. The\nscent attracts other Pokémon.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "pearl",
            "url": "https://pokeapi.co/api/v2/version/13/"
          }
        },
        {
          "flavor_text": "After a rainy day, the flower on\nits back smells stronger. The\nscent attracts other Pokémon.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version/14/"
          }
        },
        {
          "flavor_text": "By spreading the broad petals of\nits flower and catching the sun’s\nrays, it fills its body with power.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "heartgold",
            "url": "https://pokeapi.co/api/v2/version/15/"
          }
        },
        {
          "flavor_text": "It is able to convert sunlight into\nenergy. As a result, it is more\npowerful in the summertime.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "soulsilver",
            "url": "https://pokeapi.co/api/v2/version/16/"
          }
        },
        {
          "flavor_text": "Le parfum de sa fleur se fait plus\npénétrant les lendemains de pluie.\nCela appâte les autres Pokémon.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "After a rainy day, the flower on\nits back smells stronger. The\nscent attracts other Pokémon.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "Le parfum de sa fleur se fait plus\npénétrant les lendemains de pluie.\nCela appâte les autres Pokémon.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "After a rainy day, the flower on\nits back smells stronger. The\nscent attracts other Pokémon.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "After a rainy day, the flower on\nits back smells stronger. The\nscent attracts other Pokémon.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black-2",
            "url": "https://pokeapi.co/api/v2/version/21/"
          }
        },
        {
          "flavor_text": "After a rainy day, the flower on\nits back smells stronger. The\nscent attracts other Pokémon.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white-2",
            "url": "https://pokeapi.co/api/v2/version/22/"
          }
        },
        {
          "flavor_text": "おおきな　はなびらを　ひろげ\nたいようの　ひかりを　あびていると\nからだに　げんきが　みなぎっていく。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "큰 꽃잎을 펼쳐\n햇빛을 받고 있으면\n몸에 힘이 넘쳐흐른다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Ses pétales lui servent à capter la lumière du soleil.\nIl peut ainsi en canaliser l’énergie.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Es spreizt die breiten Blätter seiner Blüte,\num seinen Körper mit Sonnenenergie\nzu durchfluten.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Llena su cuerpo de energía con los rayos solares que\ncaptan los anchos pétalos de su flor.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Si riempie di energia grazie ai grandi petali del fiore,\nche spalanca catturando i raggi solari.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "By spreading the broad petals of its flower\nand catching the sun’s rays, it fills its body\nwith power.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "大きな　花びらを　広げ\n太陽の　光を　浴びていると\n体に　元気が　みなぎっていく。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "あめの　ふった　よくじつは　せなかの\nはなの　かおりが　つよまる。かおりに\nさそわれ　ポケモンが　あつまる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "비가 내린 다음 날은 등의\n꽃향기가 강해진다. 향기에\n이끌려 포켓몬이 모여든다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Le parfum de sa fleur se fait plus pénétrant les\nlendemains de pluie. Cela appâte les autres Pokémon.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Nach einem Regentag riecht die Blume auf seinem\nRücken intensiver. Das Aroma zieht andere\nPokémon an.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Después de un día de lluvia, la flor de su lomo tiene\nun aroma más potente y atrae a otros Pokémon.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Dopo la pioggia, il fiore sul suo dorso emana un\nprofumo più intenso e attira gli altri Pokémon.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "After a rainy day, the flower on its back smells\nstronger. The scent attracts other Pokémon.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "雨の　降った　翌日は\n背中の　花の　香りが　強まる。\n香りに　誘われ　ポケモンが　集まる。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "じゅうぶんな　えいようと　たいようの　ひかりが\nはなの　いろを　あざやかに　すると　いわれる。\nはなの　かおりは　ひとの　こころを　いやす。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "충분한 영양분과 태양의 빛이\n꽃의 색을 선명하게 만든다고 한다.\n꽃의 향기는 사람의 마음을 치유한다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Une belle fleur se trouve sur le dos de Florizarre.\nElle prend une couleur vive lorsqu’elle est bien nourrie et bien\nensoleillée. Le parfum de cette fleur peut apaiser les gens.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Bisaflor hat eine Blume auf seinem Rücken. Wenn sie\nviel Nahrung und Sonne aufnimmt, verfärbt sie sich bunt.\nDer Duft der Blume mildert die Emotionen der Menschen.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Venusaur tiene una flor enorme en el lomo que, según\nparece, adquiere unos colores muy vivos si está bien\nnutrido y le da mucho el sol. El aroma delicado de la flor\ntiene un efecto relajante en el ánimo de las personas.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "C’è un grande fiore sulla schiena di Venusaur. Si dice che\ni colori diventino più vividi con il giusto nutrimento e i\nraggi solari. Il suo profumo calma le reazioni emotive\ndelle persone.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "There is a large flower on Venusaur’s back. The flower is said\nto take on vivid colors if it gets plenty of nutrition and sunlight.\nThe flower’s aroma soothes the emotions of people.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "十分な　栄養と　太陽の　光が\n花の　色を　鮮やかに　すると　いわれる。\n花の　香りは　人の　心を　癒す。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "じゅうぶんな　えいようと　たいようの　ひかりが\nはなの　いろを　あざやかに　すると　いわれる。\nはなの　かおりは　ひとの　こころを　いやす。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "충분한 영양분과 태양의 빛이\n꽃의 색을 선명하게 만든다고 한다.\n꽃의 향기는 사람의 마음을 치유한다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Une belle fleur se trouve sur le dos de Florizarre.\nElle prend une couleur vive lorsqu’elle est bien nourrie et bien\nensoleillée. Le parfum de cette fleur peut apaiser les gens.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Bisaflor hat eine Blume auf seinem Rücken. Wenn sie viel\nNahrung und Sonne aufnimmt, verfärbt sie sich bunt.\nDer Duft der Blume besänftigt die Gemüter der Menschen.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Venusaur tiene una flor enorme en el lomo que, según\nparece, adquiere unos colores muy vivos si está bien\nnutrido y le da mucho el sol. El aroma delicado de la flor\ntiene un efecto relajante en el ánimo de las personas.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "C’è un grande fiore sulla schiena di Venusaur. Si dice che\ni colori diventino più vividi con il giusto nutrimento e i\nraggi solari. Il suo profumo calma le reazioni emotive\ndelle persone.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "There is a large flower on Venusaur’s back. The flower is said\nto take on vivid colors if it gets plenty of nutrition and sunlight.\nThe flower’s aroma soothes the emotions of people.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "十分な　栄養と　太陽の　光が\n花の　色を　鮮やかに　すると　いわれる。\n花の　香りは　人の　心を　癒す。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "せなかに　はえた　おおきな　ハナは\nたいようの　ひかりを　きゅうしゅうし\nエネルギーに　へんかん　できる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "등 위에 활짝 핀 큰 꽃은\n태양 빛을 흡수해서\n에너지로 변환할 수 있다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "長在背上的大花\n能夠吸收太陽光，\n並轉換成能量。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Les pétales de sa fleur dorsale absorbent les\nrayons du soleil pour les convertir en énergie.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Die große Blume auf seinem Rücken absorbiert\nSonnenlicht und kann dieses in Energie\numwandeln.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "La flor que tiene en el lomo puede recoger los\nrayos solares para transformarlos en energía.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Il grande fiore che ha sulla schiena può assorbire\ni raggi solari e trasformarli in energia.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "The flower on its back catches the sun’s rays.\nThe sunlight is then absorbed and\nused for energy.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "背中に　生えた　大きな　ハナは\n太陽の　光を　吸収し\nエネルギーに　変換　できる。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "它背上开出的大花\n能够吸收太阳光\n并将其转换为能量。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "せなかに　はえた　おおきな　ハナは\nたいようの　ひかりを　きゅうしゅうし\nエネルギーに　へんかん　できる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "등 위에 활짝 핀 큰 꽃은\n태양 빛을 흡수해서\n에너지로 변환할 수 있다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "長在背上的大花\n能夠吸收太陽光，\n並轉換成能量。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Les pétales de sa fleur dorsale absorbent les\nrayons du soleil pour les convertir en énergie.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Die große Blume auf seinem Rücken absorbiert\nSonnenlicht und kann dieses in Energie\numwandeln.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "La flor que tiene en el lomo puede recoger los\nrayos solares para transformarlos en energía.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Il grande fiore che ha sulla schiena può assorbire\ni raggi solari e trasformarli in energia.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "The flower on its back catches the sun’s rays.\nThe sunlight is then absorbed and\nused for energy.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "背中に　生えた　大きな　ハナは\n太陽の　光を　吸収し\nエネルギーに　変換　できる。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "它背上开出的大花\n能够吸收太阳光\n并将其转换为能量。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "たいようエネルギーを　えいようにして\nおおきなハナが　ひらく。　ひなたに\nひきよせられるように　いどうする。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "태양에너지를 양분으로\n큰 꽃을 피운다. 양지를 향해\n이끌려가듯이 이동한다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "把太陽的能源當成養分，\n開出碩大的花朵。總是\n朝著有陽光的地方移動。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Sa plante donne une grosse fleur quand\nelle absorbe les rayons du soleil. Il est toujours\nà la recherche des endroits les plus ensoleillés.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Es nutzt Solarenergie als Nahrung und bringt so\nseine große Blume zum Blühen. Es geht dorthin,\nwo die Sonne scheint.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "La planta florece cuando absorbe energía solar,\nlo cual le obliga a buscar siempre la luz del sol.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Il fiore sboccia assorbendo energia solare.\nSi muove continuamente in cerca di luce.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Its plant blooms when it is absorbing solar\nenergy. It stays on the move to seek sunlight.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "太陽エネルギーを　栄養にして\n大きな花が　開く。　日なたに\n引き寄せられるように　移動する。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "把太阳的能源当成养分，\n开出硕大的花朵。总是\n朝着有阳光的地方移动。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "はなから　うっとりする　かおりが\nただよい　たたかうものの　きもちを\nなだめてしまう。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "꽃에서 황홀한 향기가\n퍼져 나와 싸우는 자의\n기분을 달래준다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "花朵散發出的迷人香味，\n能安撫激動的心情，\n甚至消弭鬥爭。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Une douce senteur émane de sa plante.\nCette fragrance calme tous ceux qui sont\nengagés dans un combat.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Die Blume verströmt einen zauberhaften Duft.\nEr beschwichtigt erhitzte Kämpfer.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "La flor que tiene en el lomo libera un delicado\naroma, que tiene un efecto relajante en combate.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Il suo fiore emana una fragranza inebriante\ncapace di placare l’animo di chi è impegnato\nnella lotta.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "A bewitching aroma wafts from its flower.\nThe fragrance becalms those engaged\nin a battle.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "花から　うっとりする　香りが\nただよい　戦うものの　気持ちを\nなだめてしまう。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "花朵散发出的迷人香味\n能安抚激动的心情，\n甚至消弭斗争。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        }
      ],
      "form_descriptions": [],
      "forms_switchable": True,
      "gender_rate": 1,
      "genera": [
        {
          "genus": "たねポケモン",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          }
        },
        {
          "genus": "씨앗포켓몬",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          }
        },
        {
          "genus": "種子寶可夢",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          }
        },
        {
          "genus": "Pokémon Graine",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          }
        },
        {
          "genus": "Samen-Pokémon",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        },
        {
          "genus": "Pokémon Semilla",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          }
        },
        {
          "genus": "Pokémon Seme",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          }
        },
        {
          "genus": "Seed Pokémon",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        },
        {
          "genus": "たねポケモン",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          }
        },
        {
          "genus": "种子宝可梦",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          }
        }
      ],
      "generation": {
        "name": "generation-i",
        "url": "https://pokeapi.co/api/v2/generation/1/"
      },
      "growth_rate": {
        "name": "medium-slow",
        "url": "https://pokeapi.co/api/v2/growth-rate/4/"
      },
      "habitat": {
        "name": "grassland",
        "url": "https://pokeapi.co/api/v2/pokemon-habitat/3/"
      },
      "has_gender_differences": True,
      "hatch_counter": 20,
      "id": 3,
      "is_baby": False,
      "is_legendary": False,
      "is_mythical": False,
      "name": "venusaur",
      "names": [
        {
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "name": "フシギバナ"
        },
        {
          "language": {
            "name": "roomaji",
            "url": "https://pokeapi.co/api/v2/language/2/"
          },
          "name": "Fushigibana"
        },
        {
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "name": "이상해꽃"
        },
        {
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "name": "妙蛙花"
        },
        {
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "name": "Florizarre"
        },
        {
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "name": "Bisaflor"
        },
        {
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "name": "Venusaur"
        },
        {
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "name": "Venusaur"
        },
        {
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "name": "Venusaur"
        },
        {
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "name": "フシギバナ"
        },
        {
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "name": "妙蛙花"
        }
      ],
      "order": 3,
      "pal_park_encounters": [
        {
          "area": {
            "name": "field",
            "url": "https://pokeapi.co/api/v2/pal-park-area/2/"
          },
          "base_score": 90,
          "rate": 3
        }
      ],
      "pokedex_numbers": [
        {
          "entry_number": 3,
          "pokedex": {
            "name": "national",
            "url": "https://pokeapi.co/api/v2/pokedex/1/"
          }
        },
        {
          "entry_number": 3,
          "pokedex": {
            "name": "kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/2/"
          }
        },
        {
          "entry_number": 228,
          "pokedex": {
            "name": "original-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/3/"
          }
        },
        {
          "entry_number": 233,
          "pokedex": {
            "name": "updated-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/7/"
          }
        },
        {
          "entry_number": 82,
          "pokedex": {
            "name": "kalos-central",
            "url": "https://pokeapi.co/api/v2/pokedex/12/"
          }
        },
        {
          "entry_number": 3,
          "pokedex": {
            "name": "letsgo-kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/26/"
          }
        },
        {
          "entry_number": 70,
          "pokedex": {
            "name": "isle-of-armor",
            "url": "https://pokeapi.co/api/v2/pokedex/28/"
          }
        },
        {
          "entry_number": 166,
          "pokedex": {
            "name": "blueberry",
            "url": "https://pokeapi.co/api/v2/pokedex/33/"
          }
        }
      ],
      "shape": {
        "name": "quadruped",
        "url": "https://pokeapi.co/api/v2/pokemon-shape/8/"
      },
      "varieties": [
        {
          "is_default": True,
          "pokemon": {
            "name": "venusaur",
            "url": "https://pokeapi.co/api/v2/pokemon/3/"
          }
        },
        {
          "is_default": False,
          "pokemon": {
            "name": "venusaur-mega",
            "url": "https://pokeapi.co/api/v2/pokemon/10033/"
          }
        },
        {
          "is_default": False,
          "pokemon": {
            "name": "venusaur-gmax",
            "url": "https://pokeapi.co/api/v2/pokemon/10195/"
          }
        }
      ]
    },
    {
      "base_happiness": 50,
      "capture_rate": 45,
      "color": {
        "name": "red",
        "url": "https://pokeapi.co/api/v2/pokemon-color/8/"
      },
      "egg_groups": [
        {
          "name": "monster",
          "url": "https://pokeapi.co/api/v2/egg-group/1/"
        },
        {
          "name": "dragon",
          "url": "https://pokeapi.co/api/v2/egg-group/14/"
        }
      ],
      "evolution_chain": {
        "url": "https://pokeapi.co/api/v2/evolution-chain/2/"
      },
      "evolves_from_species": None,
      "flavor_text_entries": [
        {
          "flavor_text": "Obviously prefers\nhot places. When\nit rains, steam\fis said to spout\nfrom the tip of\nits tail.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "red",
            "url": "https://pokeapi.co/api/v2/version/1/"
          }
        },
        {
          "flavor_text": "Obviously prefers\nhot places. When\nit rains, steam\fis said to spout\nfrom the tip of\nits tail.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "blue",
            "url": "https://pokeapi.co/api/v2/version/2/"
          }
        },
        {
          "flavor_text": "The flame at the\ntip of its tail\nmakes a sound as\fit burns. You can\nonly hear it in\nquiet places.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version/3/"
          }
        },
        {
          "flavor_text": "The flame on its\ntail shows the\nstrength of its\flife force. If it\nis weak, the flame\nalso burns weakly.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "gold",
            "url": "https://pokeapi.co/api/v2/version/4/"
          }
        },
        {
          "flavor_text": "The flame on its\ntail indicates\nCHARMANDER's life\fforce. If it is\nhealthy, the flame\nburns brightly.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "silver",
            "url": "https://pokeapi.co/api/v2/version/5/"
          }
        },
        {
          "flavor_text": "If it's healthy,\nthe flame on the\ntip of its tail\fwill burn vigor­\nously, even if it\ngets a bit wet.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version/6/"
          }
        },
        {
          "flavor_text": "The flame that burns at the tip of its\ntail is an indication of its emotions.\nThe flame wavers when CHARMANDER is\fenjoying itself. If the POKéMON becomes\nenraged, the flame burns fiercely.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "ruby",
            "url": "https://pokeapi.co/api/v2/version/7/"
          }
        },
        {
          "flavor_text": "The flame that burns at the tip of its\ntail is an indication of its emotions.\nThe flame wavers when CHARMANDER is\fenjoying itself. If the POKéMON becomes\nenraged, the flame burns fiercely.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sapphire",
            "url": "https://pokeapi.co/api/v2/version/8/"
          }
        },
        {
          "flavor_text": "The flame that burns at the tip of its\ntail is an indication of its emotions.\nThe flame wavers when CHARMANDER is\nhappy, and blazes when it is enraged.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version/9/"
          }
        },
        {
          "flavor_text": "From the time it is born, a flame burns\nat the tip of its tail. Its life would end\nif the flame were to go out.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "firered",
            "url": "https://pokeapi.co/api/v2/version/10/"
          }
        },
        {
          "flavor_text": "It has a preference for hot things.\nWhen it rains, steam is said to spout from\nthe tip of its tail.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "leafgreen",
            "url": "https://pokeapi.co/api/v2/version/11/"
          }
        },
        {
          "flavor_text": "The fire on the tip of its tail is a\nmeasure of its life. If healthy,\nits tail burns intensely.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "diamond",
            "url": "https://pokeapi.co/api/v2/version/12/"
          }
        },
        {
          "flavor_text": "The fire on the tip of its tail is a\nmeasure of its life. If healthy,\nits tail burns intensely.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "pearl",
            "url": "https://pokeapi.co/api/v2/version/13/"
          }
        },
        {
          "flavor_text": "The fire on the tip of its tail is a\nmeasure of its life. If healthy,\nits tail burns intensely.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version/14/"
          }
        },
        {
          "flavor_text": "The flame on its tail shows the\nstrength of its life force. If it is weak,\nthe flame also burns weakly.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "heartgold",
            "url": "https://pokeapi.co/api/v2/version/15/"
          }
        },
        {
          "flavor_text": "The flame on its tail indicates\nCHARMANDER’s life force. If it is\nhealthy, the flame burns brightly.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "soulsilver",
            "url": "https://pokeapi.co/api/v2/version/16/"
          }
        },
        {
          "flavor_text": "La flamme de sa queue symbolise sa\nvitalité. Elle est intense quand il\nest en bonne santé.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "The fire on the tip of its tail is a\nmeasure of its life. If healthy,\nits tail burns intensely.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "La flamme de sa queue symbolise sa\nvitalité. Elle est intense quand il\nest en bonne santé.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "The fire on the tip of its tail is a\nmeasure of its life. If healthy,\nits tail burns intensely.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "The fire on the tip of its tail is a\nmeasure of its life. If healthy,\nits tail burns intensely.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black-2",
            "url": "https://pokeapi.co/api/v2/version/21/"
          }
        },
        {
          "flavor_text": "The fire on the tip of its tail is a\nmeasure of its life. If healthy,\nits tail burns intensely.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white-2",
            "url": "https://pokeapi.co/api/v2/version/22/"
          }
        },
        {
          "flavor_text": "しっぽの　ほのおは　ヒトカゲの\nせいめいりょくの　あかし。\nげんきだと　さかんに　もえさかる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "꼬리의 불꽃은 파이리의\n생명력의 상징이다.\n건강할 때 왕성하게 불타오른다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "La flamme sur sa queue représente l’énergie vitale\nde Salamèche. Quand il est vigoureux, elle brûle plus\nfort.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Die Flamme auf seiner Schweifspitze zeigt die\nLebensenergie an. Ist es gesund, leuchtet sie hell.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "La llama de su cola indica la fuerza vital de\nCharmander. Será brillante si está sano.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "La fiamma che Charmander ha sulla coda indica la\nsua forza vitale. Se è in forma, la fiamma è vivace.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "The flame on its tail indicates Charmander’s life\nforce. If it is healthy, the flame burns brightly.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "尻尾の　炎は\nヒトカゲの　生命力の　証。\n元気だと　さかんに　燃えさかる。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "うまれたときから　しっぽに　ほのおが\nともっている。ほのおが　きえたとき\nその　いのちは　おわって　しまう。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "태어날 때부터 꼬리의 불꽃이\n타오르고 있다. 불꽃이 꺼지면\n그 생명이 다하고 만다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Depuis sa naissance, une petite flamme brûle au bout\nde sa queue. Si cette flamme s’éteint, la vie de ce\nPokémon s’éteindra elle aussi.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Von Geburt an brennt die Flamme auf seiner\nSchwanzspitze. Sobald sie erlischt, erlischt auch\nsein Lebenslicht.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Este Pokémon nace con una llama en la punta de la\ncola. Si la llama se apagara, el Pokémon se debilitaría.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Dalla nascita una fiamma gli arde sulla punta della\ncoda. Se si spegnesse, per lui sarebbe la fine.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "From the time it is born, a flame burns at the tip of\nits tail. Its life would end if the flame were to\ngo out.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "生まれたときから　尻尾に　炎が\n点っている。炎が　消えたとき\nその　命は　終わってしまう。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "しっぽの　ほのおは　きぶんを　ひょうげん。\nたのしい　ときには　ゆらゆら　ほのおが　ゆれて\nおこった　ときには　めらめら　さかんに　もえる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "꼬리의 불꽃은 기분을 표현한다.\n즐거울 때는 흔들흔들 불꽃이 흔들리고\n화가 났을 때는 활활 맹렬히 불타오른다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "La flamme qui brûle au bout de sa queue indique l’humeur\nde ce Pokémon. Elle vacille lorsque Salamèche est content.\nEn revanche, lorsqu’il s’énerve, la flamme prend\nde l’importance et brûle plus ardemment.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Die Flamme auf seiner Schweifspitze zeigt seine\nGefühlslage an. Sie flackert, wenn Glumanda\nzufrieden ist. Wenn dieses Pokémon wütend wird,\nlodert die Flamme gewaltig.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "La llama que tiene en la punta de la cola arde según sus\nsentimientos. Llamea levemente cuando está alegre y arde\nvigorosamente cuando está enfadado.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "La fiamma sulla punta della coda indica il suo stato emotivo.\nSe la fiamma ondeggia significa che Charmander si sta\ndivertendo. Quando il Pokémon si infuria, la fiamma arde\nviolentemente.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "The flame that burns at the tip of its tail is an indication\nof its emotions. The flame wavers when Charmander\nis enjoying itself. If the Pokémon becomes enraged,\nthe flame burns fiercely.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "尻尾の　炎は　気分を　表現。\n楽しい　ときには　ゆらゆら　炎が　ゆれて\n怒った　ときには　めらめら　盛んに　燃える。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "しっぽの　ほのおは　きぶんを　ひょうげん。\nたのしい　ときには　ゆらゆら　ほのおが　ゆれて\nおこった　ときには　めらめら　さかんに　もえる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "꼬리의 불꽃은 기분을 표현한다.\n즐거울 때는 흔들흔들 불꽃이 흔들리고\n화가 났을 때는 활활 맹렬히 불타오른다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "La flamme qui brûle au bout de sa queue indique l’humeur\nde ce Pokémon. Elle vacille lorsque Salamèche est content.\nEn revanche, lorsqu’il s’énerve, la flamme prend\nde l’importance et brûle plus ardemment.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Die Flamme auf seiner Schweifspitze zeigt seine\nGefühlslage an. Sie flackert, wenn Glumanda\nzufrieden ist. Wenn dieses Pokémon wütend wird,\nlodert die Flamme sehr stark.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "La llama que tiene en la punta de la cola arde según sus\nsentimientos. Llamea levemente cuando está alegre y arde\nvigorosamente cuando está enfadado.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "La fiamma sulla punta della coda indica il suo stato emotivo.\nSe la fiamma ondeggia significa che Charmander si sta\ndivertendo. Quando il Pokémon si infuria, la fiamma arde\nviolentemente.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "The flame that burns at the tip of its tail is an indication\nof its emotions. The flame wavers when Charmander\nis enjoying itself. If the Pokémon becomes enraged,\nthe flame burns fiercely.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "尻尾の　炎は　気分を　表現。\n楽しい　ときには　ゆらゆら　炎が　ゆれて\n怒った　ときには　めらめら　盛んに　燃える。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "しずかな　ところに　つれていくと\nシッポが　もえてる　ちいさな　おとが\nきこえてくるよ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "조용한 곳에 데려가면\n꼬리가 타고 있는\n작은 소리가 들린다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "要是把牠帶到安靜的地方，\n就能聽見牠的尾巴燃燒時\n發出的微小聲音。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "La flammèche au bout de sa queue émet\nun crépitement audible seulement dans\nles endroits calmes.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "An sehr stillen Orten kann man seine brennende\nSchwanzspitze ganz leise lodern hören.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "En lugares silenciosos se puede oír el débil\nchisporroteo de la llama que le arde en la\npunta de la cola.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Nel silenzio più assoluto si può udire la fiamma\nin cima alla sua coda scoppiettare bruciando.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "The flame at the tip of its tail makes a sound as\nit burns. You can only hear it in quiet places.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "静かな　ところに　連れていくと\nシッポが　燃えてる　小さな　音が\n聞こえてくるよ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "要是把它带到安静的地方，\n就能听到它的尾巴燃烧时\n发出的微小的声音。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "しずかな　ところに　つれていくと\nシッポが　もえてる　ちいさな　おとが\nきこえてくるよ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "조용한 곳에 데려가면\n꼬리가 타고 있는\n작은 소리가 들린다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "要是把牠帶到安靜的地方，\n就能聽見牠的尾巴燃燒時\n發出的微小聲音。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "La flammèche au bout de sa queue émet\nun crépitement audible seulement dans\nles endroits calmes.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "An sehr stillen Orten kann man seine brennende\nSchwanzspitze ganz leise lodern hören.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "En lugares silenciosos se puede oír el débil\nchisporroteo de la llama que le arde en la\npunta de la cola.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Nel silenzio più assoluto si può udire la fiamma\nin cima alla sua coda scoppiettare bruciando.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "The flame at the tip of its tail makes a sound as\nit burns. You can only hear it in quiet places.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "静かな　ところに　連れていくと\nシッポが　燃えてる　小さな　音が\n聞こえてくるよ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "要是把它带到安静的地方，\n就能听到它的尾巴燃烧时\n发出的微小的声音。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "あついものを　このむ　せいかく。\nあめにぬれると　しっぽの　さきから\nけむりが　でるという。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "뜨거운 것을 좋아하는 성격이다.\n비에 젖으면 꼬리 끝에서\n연기가 난다고 한다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "天生喜歡熱熱的東西。\n據說當牠被雨淋濕的時候，\n尾巴的末端會冒出煙來。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Il préfère ce qui est chaud.\nEn cas de pluie, de la vapeur se forme autour\nde sa queue.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Dieses Pokémon bevorzugt heiße Dinge.\nBei Regen soll seine Schwanzspitze dampfen.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Prefiere las cosas calientes. Dicen que cuando\nllueve le sale vapor de la punta de la cola.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Ama le cose calde. Si dice che quando piove\ngli esca vapore dalla punta della coda.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "It has a preference for hot things. When it rains,\nsteam is said to spout from the tip of its tail.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "熱いものを　好む　性格。\n雨に濡れると　しっぽの　先から\n煙が　出るという。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "天生喜欢热热的东西。\n据说当它被雨淋湿的时候，\n尾巴的末端会冒出烟来。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "うまれたときから　しっぽに　ほのおが\nともっている。　ほのおが　きえたとき\nその　いのちは　おわって　しまう。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "태어날 때부터 꼬리에 불꽃이\n타오르고 있다. 불꽃이 꺼지면\n생명도 다하고 만다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "從出生時開始尾巴上\n就有火焰在燃燒。\n火焰熄滅時，生命也會結束。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Depuis sa naissance, une petite flamme brûle\nau bout de sa queue. Si cette flamme s’éteint,\nla vie de ce Pokémon s’éteindra elle aussi.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Von Geburt an brennt die Flamme auf seiner\nSchwanzspitze. Sobald sie verglimmt, erlischt\nauch sein Lebenslicht.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Este Pokémon nace con una llama en la punta de\nla cola. Si se le apagara, fallecería.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Una fiamma gli arde sulla punta della coda\nfin dalla nascita. Se si spegnesse, per lui\nsarebbe la fine.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "From the time it is born, a flame burns at the tip\nof its tail. Its life would end if the flame were to\ngo out.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "生まれたときから　しっぽに　炎が\nともっている。　炎が　消えたとき\nその　命は　終わって　しまう。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "生下来的时候，\n尾巴上就有火焰在燃烧。\n火焰熄灭时，它的生命也会结束。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        }
      ],
      "form_descriptions": [],
      "forms_switchable": False,
      "gender_rate": 1,
      "genera": [
        {
          "genus": "とかげポケモン",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          }
        },
        {
          "genus": "도롱뇽포켓몬",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          }
        },
        {
          "genus": "蜥蜴寶可夢",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          }
        },
        {
          "genus": "Pokémon Lézard",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          }
        },
        {
          "genus": "Echsen-Pokémon",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        },
        {
          "genus": "Pokémon Lagartija",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          }
        },
        {
          "genus": "Pokémon Lucertola",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          }
        },
        {
          "genus": "Lizard Pokémon",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        },
        {
          "genus": "とかげポケモン",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          }
        },
        {
          "genus": "蜥蜴宝可梦",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          }
        }
      ],
      "generation": {
        "name": "generation-i",
        "url": "https://pokeapi.co/api/v2/generation/1/"
      },
      "growth_rate": {
        "name": "medium-slow",
        "url": "https://pokeapi.co/api/v2/growth-rate/4/"
      },
      "habitat": {
        "name": "mountain",
        "url": "https://pokeapi.co/api/v2/pokemon-habitat/4/"
      },
      "has_gender_differences": False,
      "hatch_counter": 20,
      "id": 4,
      "is_baby": False,
      "is_legendary": False,
      "is_mythical": False,
      "name": "charmander",
      "names": [
        {
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "name": "ヒトカゲ"
        },
        {
          "language": {
            "name": "roomaji",
            "url": "https://pokeapi.co/api/v2/language/2/"
          },
          "name": "Hitokage"
        },
        {
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "name": "파이리"
        },
        {
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "name": "小火龍"
        },
        {
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "name": "Salamèche"
        },
        {
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "name": "Glumanda"
        },
        {
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "name": "Charmander"
        },
        {
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "name": "Charmander"
        },
        {
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "name": "Charmander"
        },
        {
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "name": "ヒトカゲ"
        },
        {
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "name": "小火龙"
        }
      ],
      "order": 4,
      "pal_park_encounters": [
        {
          "area": {
            "name": "field",
            "url": "https://pokeapi.co/api/v2/pal-park-area/2/"
          },
          "base_score": 50,
          "rate": 30
        }
      ],
      "pokedex_numbers": [
        {
          "entry_number": 4,
          "pokedex": {
            "name": "national",
            "url": "https://pokeapi.co/api/v2/pokedex/1/"
          }
        },
        {
          "entry_number": 4,
          "pokedex": {
            "name": "kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/2/"
          }
        },
        {
          "entry_number": 229,
          "pokedex": {
            "name": "original-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/3/"
          }
        },
        {
          "entry_number": 234,
          "pokedex": {
            "name": "updated-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/7/"
          }
        },
        {
          "entry_number": 109,
          "pokedex": {
            "name": "conquest-gallery",
            "url": "https://pokeapi.co/api/v2/pokedex/11/"
          }
        },
        {
          "entry_number": 83,
          "pokedex": {
            "name": "kalos-central",
            "url": "https://pokeapi.co/api/v2/pokedex/12/"
          }
        },
        {
          "entry_number": 4,
          "pokedex": {
            "name": "letsgo-kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/26/"
          }
        },
        {
          "entry_number": 378,
          "pokedex": {
            "name": "galar",
            "url": "https://pokeapi.co/api/v2/pokedex/27/"
          }
        },
        {
          "entry_number": 167,
          "pokedex": {
            "name": "blueberry",
            "url": "https://pokeapi.co/api/v2/pokedex/33/"
          }
        }
      ],
      "shape": {
        "name": "upright",
        "url": "https://pokeapi.co/api/v2/pokemon-shape/6/"
      },
      "varieties": [
        {
          "is_default": True,
          "pokemon": {
            "name": "charmander",
            "url": "https://pokeapi.co/api/v2/pokemon/4/"
          }
        }
      ]
    },
    {
      "base_happiness": 50,
      "capture_rate": 45,
      "color": {
        "name": "red",
        "url": "https://pokeapi.co/api/v2/pokemon-color/8/"
      },
      "egg_groups": [
        {
          "name": "monster",
          "url": "https://pokeapi.co/api/v2/egg-group/1/"
        },
        {
          "name": "dragon",
          "url": "https://pokeapi.co/api/v2/egg-group/14/"
        }
      ],
      "evolution_chain": {
        "url": "https://pokeapi.co/api/v2/evolution-chain/2/"
      },
      "evolves_from_species": {
        "name": "charmander",
        "url": "https://pokeapi.co/api/v2/pokemon-species/4/"
      },
      "flavor_text_entries": [
        {
          "flavor_text": "When it swings\nits burning tail,\nit elevates the\ftemperature to\nunbearably high\nlevels.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "red",
            "url": "https://pokeapi.co/api/v2/version/1/"
          }
        },
        {
          "flavor_text": "When it swings\nits burning tail,\nit elevates the\ftemperature to\nunbearably high\nlevels.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "blue",
            "url": "https://pokeapi.co/api/v2/version/2/"
          }
        },
        {
          "flavor_text": "Tough fights could\nexcite this\nPOKéMON. When\fexcited, it may\nblow out bluish-\nwhite flames.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version/3/"
          }
        },
        {
          "flavor_text": "It is very hot­\nheaded by nature,\nso it constantly\fseeks opponents.\nIt calms down only\nwhen it wins.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "gold",
            "url": "https://pokeapi.co/api/v2/version/4/"
          }
        },
        {
          "flavor_text": "It has a barbaric\nnature. In battle,\nit whips its\ffiery tail around\nand slashes away\nwith sharp claws.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "silver",
            "url": "https://pokeapi.co/api/v2/version/5/"
          }
        },
        {
          "flavor_text": "If it becomes\nagitated during\nbattle, it spouts\fintense flames,\nincinerating its\nsurroundings.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version/6/"
          }
        },
        {
          "flavor_text": "CHARMELEON mercilessly destroys its\nfoes using its sharp claws.\nIf it encounters a strong foe, it turns\faggressive. In this excited state, the\nflame at the tip of its tail flares with a\nbluish white color.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "ruby",
            "url": "https://pokeapi.co/api/v2/version/7/"
          }
        },
        {
          "flavor_text": "CHARMELEON mercilessly destroys its\nfoes using its sharp claws.\nIf it encounters a strong foe, it turns\faggressive. In this excited state, the\nflame at the tip of its tail flares with a\nbluish white color.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sapphire",
            "url": "https://pokeapi.co/api/v2/version/8/"
          }
        },
        {
          "flavor_text": "Without pity, its sharp claws destroy foes.\nIf it encounters a strong enemy, it\nbecomes agitated, and the flame on its\ntail flares with a bluish white color.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version/9/"
          }
        },
        {
          "flavor_text": "It lashes about with its tail to knock\ndown its foe. It then tears up the fallen\nopponent with sharp claws.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "firered",
            "url": "https://pokeapi.co/api/v2/version/10/"
          }
        },
        {
          "flavor_text": "When it swings its burning tail, it\nelevates the air temperature to \nunbearably high levels.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "leafgreen",
            "url": "https://pokeapi.co/api/v2/version/11/"
          }
        },
        {
          "flavor_text": "In the rocky mountains where\nCHARMELEON live, their fiery\ntails shine at night like stars.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "diamond",
            "url": "https://pokeapi.co/api/v2/version/12/"
          }
        },
        {
          "flavor_text": "In the rocky mountains where\nCHARMELEON live, their fiery\ntails shine at night like stars.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "pearl",
            "url": "https://pokeapi.co/api/v2/version/13/"
          }
        },
        {
          "flavor_text": "In the rocky mountains where\nCHARMELEON live, their fiery\ntails shine at night like stars.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version/14/"
          }
        },
        {
          "flavor_text": "It is very hotheaded by nature,\nso it constantly seeks opponents.\nIt calms down only when it wins.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "heartgold",
            "url": "https://pokeapi.co/api/v2/version/15/"
          }
        },
        {
          "flavor_text": "It has a barbaric nature. In battle,\nit whips its fiery tail around\nand slashes away with sharp claws.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "soulsilver",
            "url": "https://pokeapi.co/api/v2/version/16/"
          }
        },
        {
          "flavor_text": "La nuit, la queue ardente du Reptincel\nbrille comme une étoile dans son\nrepaire montagneux.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "In the rocky mountains where\nCharmeleon live, their fiery\ntails shine at night like stars.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "La nuit, la queue ardente du Reptincel\nbrille comme une étoile dans son\nrepaire montagneux.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "In the rocky mountains where\nCharmeleon live, their fiery\ntails shine at night like stars.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "In the rocky mountains where\nCharmeleon live, their fiery\ntails shine at night like stars.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black-2",
            "url": "https://pokeapi.co/api/v2/version/21/"
          }
        },
        {
          "flavor_text": "In the rocky mountains where\nCharmeleon live, their fiery\ntails shine at night like stars.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white-2",
            "url": "https://pokeapi.co/api/v2/version/22/"
          }
        },
        {
          "flavor_text": "しっぽを　ふりまわして　あいてを\nなぎたおし　するどい　ツメで\nズタズタに　ひきさいてしまう。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "꼬리를 휘둘러 상대를\n쓰러트리고 날카로운 발톱으로\n갈기갈기 찢어버린다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Il se sert de sa queue pour faire tomber ses\nadversaires. Une fois qu’ils sont au sol, il les lacère\nde ses griffes acérées.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Es schlägt im Kampf mit seinem Schwanz nach\nseinen Gegnern. Anschließend zerfetzt es\ndie Gegner mit seinen scharfen Klauen.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Suele usar la cola para derribar a su rival. Cuando lo\ntira, se vale de sus afiladas garras para acabar con él.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Fa cadere a terra il nemico colpendolo con la coda,\nper poi finirlo con gli artigli affilati.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "It lashes about with its tail to knock down its foe.\nIt then tears up the fallen opponent with\nsharp claws.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "尻尾を　振り回して\n相手を　なぎ倒し　鋭い　ツメで\nズタズタに　ひきさいてしまう。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "もえる　しっぽを　ふりまわすと\nまわりの　おんどが　どんどん\nあがって　あいてを　くるしめる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "불타는 꼬리를 휘두르면\n주위의 온도가 점점\n올라가 상대를 괴롭게 한다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "En agitant sa queue, il peut élever la température à\nun niveau incroyable.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Wenn Glutexo mit seinem Schwanz schwingt,\nsteigt die Temperatur ins Unermessliche.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Cuando balancea la ardiente cola, eleva la temperatura\na niveles muy altos.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Quando agita la sua coda infuocata porta la\ntemperatura a livelli insostenibili.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "When it swings its burning tail, it elevates the air\ntemperature to unbearably high levels.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "燃える　尻尾を　振り回すと\nまわりの　温度が　どんどん　上がって\n相手を　苦しめる。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "するどい　ツメで　ようしゃなく　たたきのめす。\nきょうてきと　むかいあうと　きぶんが　たかぶり\nしっぽの　ほのおが　あおじろく　もえあがる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "날카로운 발톱으로 봐주지 않고 때려눕힌다.\n강한 적을 만나면 기분이 고양되며\n꼬리의 불꽃이 푸르스름하게 불타오른다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Reptincel lacère ses ennemis sans pitié grâce à ses griffes\nacérées. S’il rencontre un ennemi puissant, il devient agressif\net la flamme au bout de sa queue s’embrase et prend\nune couleur bleu clair.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Gnadenlos besiegt Glutexo seine Gegner mit seinen\nscharfen Klauen. Wenn es auf starke Gegner trifft,\nwird es wütend und die Flamme auf seiner Schweifspitze\nflackert in einem bläulichen Ton.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Charmeleon no tiene reparo en acabar con su rival usando\nlas afiladas garras que tiene. Si su enemigo es fuerte, se\nvuelve agresivo, y la llama que tiene en el extremo de la cola\nempieza a arder con mayor intensidad tornándose azulada.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Charmeleon distrugge il nemico senza pietà con i suoi\nartigli affilati. Quando incontra un avversario molto forte\ndiventa aggressivo. In questo stato di grande agitazione\nla fiamma della coda diventa di colore bianco bluastro.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Charmeleon mercilessly destroys its foes using its sharp claws.\nIf it encounters a strong foe, it turns aggressive.\nIn this excited state, the flame at the tip of its tail flares with a\nbluish white color.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "鋭い　ツメで　ようしゃなく　たたきのめす。\n強敵と　向かい合うと　気分が　たかぶり\n尻尾の　炎が　青白く　燃えあがる。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "するどい　ツメで　ようしゃなく　たたきのめす。\nきょうてきと　むかいあうと　きぶんが　たかぶり\nしっぽの　ほのおが　あおじろく　もえあがる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "날카로운 발톱으로 봐주지 않고 때려눕힌다.\n강한 적을 만나면 기분이 고양되며\n꼬리의 불꽃이 푸르스름하게 불타오른다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Reptincel lacère ses ennemis sans pitié grâce à ses griffes\nacérées. S’il rencontre un ennemi puissant, il devient agressif\net la flamme au bout de sa queue s’embrase et prend\nune couleur bleu clair.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Glutexo attackiert seine Feinde mit aller Gewalt und unter\nEinsatz seiner scharfen Krallen. Trifft es auf starke Gegner,\nwird es wütend und die Flamme auf seiner Schweifspitze\nflackert in einem bläulichen Ton.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Charmeleon no tiene reparo en acabar con su rival usando\nlas afiladas garras que tiene. Si su enemigo es fuerte, se\nvuelve agresivo, y la llama que tiene en el extremo de la cola\nempieza a arder con mayor intensidad tornándose azulada.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Charmeleon distrugge il nemico senza pietà con i suoi\nartigli affilati. Quando incontra un avversario molto forte\ndiventa aggressivo. In questo stato di grande agitazione\nla fiamma della coda diventa di colore bianco bluastro.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Charmeleon mercilessly destroys its foes using its sharp\nclaws. If it encounters a strong foe, it turns aggressive.\nIn this excited state, the flame at the tip of its tail flares with\na bluish white color.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "鋭い　ツメで　ようしゃなく　たたきのめす。\n強敵と　向かい合うと　気分が　たかぶり\n尻尾の　炎が　青白く　燃えあがる。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "きょうてきと　たたかいつづけ\nエキサイトすると　あおじろい\nほのおを　はきだすことがある。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "강한 적과 싸움을 거듭하다\n흥분하면 푸르스름한\n불꽃을 뿜어낼 때가 있다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "在與強敵戰鬥的過程中，\n如果情緒變得興奮起來，\n有時會噴出藍白色的火焰。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Exalté quand il affronte des adversaires\npuissants, ce Pokémon en vient parfois\nà cracher des flammes bleutées.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Kämpft es länger gegen starke Gegner, so gerät\nes in Aufregung und spuckt manchmal gleißend\nhelle, bläuliche Flammen.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Librar combates intensos lo entusiasma tanto\nque en ocasiones lanza llamas de tono blanco\nazulado.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Si infervora durante le lotte più dure e talvolta\nsputa fiamme bluastre.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Tough fights could excite this Pokémon. When\nexcited, it may breathe out bluish-white flames.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "強敵と　戦いつづけ\nエキサイトすると　青白い\n炎を　吐き出すことがある。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "在与强敌战斗的过程中，\n如果情绪变得兴奋起来，\n有时会喷出青白色的烈火。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "きょうてきと　たたかいつづけ\nエキサイトすると　あおじろい\nほのおを　はきだすことがある。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "강한 적과 싸움을 거듭하다\n흥분하면 푸르스름한\n불꽃을 뿜어낼 때가 있다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "在與強敵戰鬥的過程中，\n如果情緒變得興奮起來，\n有時會噴出藍白色的火焰。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Exalté quand il affronte des adversaires\npuissants, ce Pokémon en vient parfois\nà cracher des flammes bleutées.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Kämpft es länger gegen starke Gegner, so gerät\nes in Aufregung und spuckt manchmal gleißend\nhelle, bläuliche Flammen.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Librar combates intensos lo entusiasma tanto\nque en ocasiones lanza llamas de tono blanco\nazulado.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Si infervora durante le lotte più dure e talvolta\nsputa fiamme bluastre.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Tough fights could excite this Pokémon. When\nexcited, it may breathe out bluish-white flames.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "強敵と　戦いつづけ\nエキサイトすると　青白い\n炎を　吐き出すことがある。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "在与强敌战斗的过程中，\n如果情绪变得兴奋起来，\n有时会喷出青白色的烈火。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "もえる　しっぽを　ふりまわし\nするどい　ツメで　あいてを\nきりさく　あらあらしい　せいかく。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "불타는 꼬리를 휘두르며\n날카로운 발톱으로 상대를\n베어 가르는 몹시 거친 성격이다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "揮動燃燒著火焰的尾巴，\n用鋒利的爪子撕裂對手。\n性情十分粗暴。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Il est très brutal. En combat, il se sert de\nses griffes acérées et de sa queue enflammée\npour mettre en pièces ses adversaires.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Es ist brutal veranlagt. Im Kampf schlägt es mit\nseinem brennenden Schweif um sich und schlitzt\nGegner mit seinen scharfen Klauen auf.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Este Pokémon de naturaleza agresiva ataca en\ncombate con su cola llameante y hace trizas al\nrival con sus afiladas garras.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Ha un’indole feroce. Usa la coda fiammeggiante\ncome una frusta e lacera l’avversario con gli\nartigli affilati.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "It has a barbaric nature. In battle, it whips its\nfiery tail around and slashes away with sharp claws.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "燃える　しっぽを　振りまわし\nするどい　ツメで　相手を\n切り裂く　荒々しい　性格。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "挥动燃烧着火焰的尾巴，\n用锋利的爪子撕裂对手。\n性格十分粗暴。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "たたかいで　きもちが　たかぶると\nしゃくねつの　ほのおを　ふきながら\nあたりを　もやしてまわる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "싸움으로 기분이 고조되면\n작열하는 불꽃을 뿜으며\n주변을 태워버린다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "如果牠在戰鬥中亢奮起來，\n就會噴出灼熱的火焰，\n把周圍的東西燒得一乾二淨。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "S’il s’excite pendant un combat, il crache\nde grandes flammes, brûlant tout ce qui\nse trouve aux alentours.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Steigert es sich in einen Kampf hinein, spuckt es\nFlammen, die alles in seiner Umgebung\nniederbrennen.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Si se exalta en combate, expulsa intensas\nllamaradas que incineran todo a su alrededor.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Se s’infervora nella lotta, sputa potenti fiamme\nche inceneriscono l’area circostante.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "If it becomes agitated during battle, it spouts\nintense flames, incinerating its surroundings.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "戦いで　気持ちが　たかぶると\n灼熱の　炎を　吹きながら\nあたりを　燃やしてまわる。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "如果它在战斗中亢奋起来，\n就会喷出灼热的火焰，\n把周围的东西烧得一干二净。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        }
      ],
      "form_descriptions": [],
      "forms_switchable": False,
      "gender_rate": 1,
      "genera": [
        {
          "genus": "かえんポケモン",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          }
        },
        {
          "genus": "화염포켓몬",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          }
        },
        {
          "genus": "火焰寶可夢",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          }
        },
        {
          "genus": "Pokémon Flamme",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          }
        },
        {
          "genus": "Flammen-Pokémon",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        },
        {
          "genus": "Pokémon Llama",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          }
        },
        {
          "genus": "Pokémon Fiamma",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          }
        },
        {
          "genus": "Flame Pokémon",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        },
        {
          "genus": "かえんポケモン",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          }
        },
        {
          "genus": "火焰宝可梦",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          }
        }
      ],
      "generation": {
        "name": "generation-i",
        "url": "https://pokeapi.co/api/v2/generation/1/"
      },
      "growth_rate": {
        "name": "medium-slow",
        "url": "https://pokeapi.co/api/v2/growth-rate/4/"
      },
      "habitat": {
        "name": "mountain",
        "url": "https://pokeapi.co/api/v2/pokemon-habitat/4/"
      },
      "has_gender_differences": False,
      "hatch_counter": 20,
      "id": 5,
      "is_baby": False,
      "is_legendary": False,
      "is_mythical": False,
      "name": "charmeleon",
      "names": [
        {
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "name": "リザード"
        },
        {
          "language": {
            "name": "roomaji",
            "url": "https://pokeapi.co/api/v2/language/2/"
          },
          "name": "Lizardo"
        },
        {
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "name": "리자드"
        },
        {
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "name": "火恐龍"
        },
        {
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "name": "Reptincel"
        },
        {
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "name": "Glutexo"
        },
        {
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "name": "Charmeleon"
        },
        {
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "name": "Charmeleon"
        },
        {
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "name": "Charmeleon"
        },
        {
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "name": "リザード"
        },
        {
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "name": "火恐龙"
        }
      ],
      "order": 5,
      "pal_park_encounters": [
        {
          "area": {
            "name": "field",
            "url": "https://pokeapi.co/api/v2/pal-park-area/2/"
          },
          "base_score": 80,
          "rate": 10
        }
      ],
      "pokedex_numbers": [
        {
          "entry_number": 5,
          "pokedex": {
            "name": "national",
            "url": "https://pokeapi.co/api/v2/pokedex/1/"
          }
        },
        {
          "entry_number": 5,
          "pokedex": {
            "name": "kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/2/"
          }
        },
        {
          "entry_number": 230,
          "pokedex": {
            "name": "original-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/3/"
          }
        },
        {
          "entry_number": 235,
          "pokedex": {
            "name": "updated-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/7/"
          }
        },
        {
          "entry_number": 110,
          "pokedex": {
            "name": "conquest-gallery",
            "url": "https://pokeapi.co/api/v2/pokedex/11/"
          }
        },
        {
          "entry_number": 84,
          "pokedex": {
            "name": "kalos-central",
            "url": "https://pokeapi.co/api/v2/pokedex/12/"
          }
        },
        {
          "entry_number": 5,
          "pokedex": {
            "name": "letsgo-kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/26/"
          }
        },
        {
          "entry_number": 379,
          "pokedex": {
            "name": "galar",
            "url": "https://pokeapi.co/api/v2/pokedex/27/"
          }
        },
        {
          "entry_number": 168,
          "pokedex": {
            "name": "blueberry",
            "url": "https://pokeapi.co/api/v2/pokedex/33/"
          }
        }
      ],
      "shape": {
        "name": "upright",
        "url": "https://pokeapi.co/api/v2/pokemon-shape/6/"
      },
      "varieties": [
        {
          "is_default": True,
          "pokemon": {
            "name": "charmeleon",
            "url": "https://pokeapi.co/api/v2/pokemon/5/"
          }
        }
      ]
    },
    {
      "base_happiness": 50,
      "capture_rate": 45,
      "color": {
        "name": "red",
        "url": "https://pokeapi.co/api/v2/pokemon-color/8/"
      },
      "egg_groups": [
        {
          "name": "monster",
          "url": "https://pokeapi.co/api/v2/egg-group/1/"
        },
        {
          "name": "dragon",
          "url": "https://pokeapi.co/api/v2/egg-group/14/"
        }
      ],
      "evolution_chain": {
        "url": "https://pokeapi.co/api/v2/evolution-chain/2/"
      },
      "evolves_from_species": {
        "name": "charmeleon",
        "url": "https://pokeapi.co/api/v2/pokemon-species/5/"
      },
      "flavor_text_entries": [
        {
          "flavor_text": "Spits fire that\nis hot enough to\nmelt boulders.\fKnown to cause\nforest fires\nunintentionally.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "red",
            "url": "https://pokeapi.co/api/v2/version/1/"
          }
        },
        {
          "flavor_text": "Spits fire that\nis hot enough to\nmelt boulders.\fKnown to cause\nforest fires\nunintentionally.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "blue",
            "url": "https://pokeapi.co/api/v2/version/2/"
          }
        },
        {
          "flavor_text": "When expelling a\nblast of super\nhot fire, the red\fflame at the tip\nof its tail burns\nmore intensely.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version/3/"
          }
        },
        {
          "flavor_text": "If CHARIZARD be­\ncomes furious, the\nflame at the tip\fof its tail flares\nup in a whitish-\nblue color.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "gold",
            "url": "https://pokeapi.co/api/v2/version/4/"
          }
        },
        {
          "flavor_text": "Breathing intense,\nhot flames, it can\nmelt almost any­\fthing. Its breath\ninflicts terrible\npain on enemies.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "silver",
            "url": "https://pokeapi.co/api/v2/version/5/"
          }
        },
        {
          "flavor_text": "It uses its wings\nto fly high. The\ntemperature of its\ffire increases as\nit gains exper­\nience in battle.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version/6/"
          }
        },
        {
          "flavor_text": "CHARIZARD flies around the sky in\nsearch of powerful opponents.\nIt breathes fire of such great heat\fthat it melts anything. However, it\nnever turns its fiery breath on any\nopponent weaker than itself.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "ruby",
            "url": "https://pokeapi.co/api/v2/version/7/"
          }
        },
        {
          "flavor_text": "CHARIZARD flies around the sky in\nsearch of powerful opponents.\nIt breathes fire of such great heat\fthat it melts anything. However, it\nnever turns its fiery breath on any\nopponent weaker than itself.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sapphire",
            "url": "https://pokeapi.co/api/v2/version/8/"
          }
        },
        {
          "flavor_text": "A CHARIZARD flies about in search of\nstrong opponents. It breathes intense\nflames that can melt any material. However,\nit will never torch a weaker foe.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version/9/"
          }
        },
        {
          "flavor_text": "Its wings can carry this POKéMON close to\nan altitude of 4,600 feet. It blows out\nfire at very high temperatures.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "firered",
            "url": "https://pokeapi.co/api/v2/version/10/"
          }
        },
        {
          "flavor_text": "It spits fire that is hot enough to melt\nboulders. It may cause forest fires by\nblowing flames.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "leafgreen",
            "url": "https://pokeapi.co/api/v2/version/11/"
          }
        },
        {
          "flavor_text": "It is said that CHARIZARD’s fire\nburns hotter if it has\nexperienced harsh battles.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "diamond",
            "url": "https://pokeapi.co/api/v2/version/12/"
          }
        },
        {
          "flavor_text": "It is said that CHARIZARD’s fire\nburns hotter if it has\nexperienced harsh battles.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "pearl",
            "url": "https://pokeapi.co/api/v2/version/13/"
          }
        },
        {
          "flavor_text": "It is said that CHARIZARD’s fire\nburns hotter if it has\nexperienced harsh battles.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version/14/"
          }
        },
        {
          "flavor_text": "If CHARIZARD becomes furious,\nthe flame at the tip of its tail flares\nup in a light blue shade.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "heartgold",
            "url": "https://pokeapi.co/api/v2/version/15/"
          }
        },
        {
          "flavor_text": "Breathing intense, hot flames, it can\nmelt almost anything. Its breath\ninflicts terrible pain on enemies.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "soulsilver",
            "url": "https://pokeapi.co/api/v2/version/16/"
          }
        },
        {
          "flavor_text": "On raconte que la flamme du\nDracaufeu s’intensifie après\nun combat difficile.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "It is said that Charizard’s fire\nburns hotter if it has\nexperienced harsh battles.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "On raconte que la flamme du\nDracaufeu s’intensifie après\nun combat difficile.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "It is said that Charizard’s fire\nburns hotter if it has\nexperienced harsh battles.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "It is said that Charizard’s fire\nburns hotter if it has\nexperienced harsh battles.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black-2",
            "url": "https://pokeapi.co/api/v2/version/21/"
          }
        },
        {
          "flavor_text": "It is said that Charizard’s fire\nburns hotter if it has\nexperienced harsh battles.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white-2",
            "url": "https://pokeapi.co/api/v2/version/22/"
          }
        },
        {
          "flavor_text": "くちから　しゃくねつの　ほのおを\nはきだすとき　しっぽの　さきは\nより　あかく　はげしく　もえあがる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "입에서 작렬하는 불꽃을\n토해낼 때 꼬리의 끝이\n더욱 붉고 격렬하게 타오른다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Quand il crache son souffle brûlant, la flamme au bout\nde sa queue s’embrase.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Wenn dieses Pokémon einen Strahl glühenden\nFeuers speit, leuchtet seine Schwanzspitze auf.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Cuando lanza una descarga de fuego supercaliente, la\nroja llama de su cola brilla más intensamente.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Quando emette le sue lingue di fuoco, la fiamma\nrossa sulla punta della coda brucia più intensamente.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "When expelling a blast of superhot fire,\nthe red flame at the tip of its tail burns\nmore intensely.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "口から　灼熱の　炎を　吐き出すとき\n尻尾の　先は\nより　赤く　激しく　燃え上がる。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "ちじょう　１４００メートル　まで\nハネを　つかって　とぶことができる。\nこうねつの　ほのおを　はく。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "지상 1400m까지\n날개를 사용해 날 수 있다.\n고열의 불꽃을 내뿜는다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Ses ailes peuvent le faire voler à plus de 1 400 m\nd’altitude. Ce Pokémon crache du feu à des\ntempératures très élevées.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Dieses Pokémon kann mit seinen Flügeln\neine Höhe von bis zu 1 400 m erreichen.\nEs spuckt sehr heißes Feuer.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Con las alas que tiene puede alcanzar una altura de\ncasi 1400 m. Suele escupir fuego por la boca.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Grazie alle possenti ali può volare fino a 1400 m\nd’altezza. Sputa fuoco a una temperatura\nimpressionante.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Its wings can carry this Pokémon close to an\naltitude of 4,600 feet. It blows out fire at very\nhigh temperatures.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "地上　１４００メートルまで\n羽を　使って　飛ぶことができる。\n高熱の　炎を　吐く。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "つよい　あいてを　もとめて　そらを　とびまわる。\nなんでも　とかして　しまう　こうねつの　ほのおを\nじぶんより　よわいものに　むけることは　しない。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "강한 상대를 찾아 하늘을 날아다닌다.\n무엇이든 다 녹여버리는 고열의 불꽃을\n자신보다 약한 자에게 들이대지 않는다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Dracaufeu parcourt les cieux pour trouver des adversaires\nà sa mesure. Il crache de puissantes flammes capables de\nfaire fondre n’importe quoi. Mais il ne dirige jamais son souffle\ndestructeur vers un ennemi plus faible.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Glurak fliegt durch die Lüfte, um starke Gegner aufzuspüren.\nSein heißer Feueratem bringt alles zum Schmelzen. Aber es\nrichtet seinen Feueratem nie auf schwächere Gegner.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Charizard se dedica a volar por los cielos en busca de\noponentes fuertes. Echa fuego por la boca y es capaz de\nderretir cualquier cosa. No obstante, si su rival es más débil\nque él, no usará este ataque.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Charizard solca i cieli in cerca di nemici molto forti.\nRiesce a emettere fiammate di un calore tale da fondere\nogni cosa. Tuttavia, non rivolge mai le sue micidiali lingue\ndi fuoco contro avversari più deboli di lui.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Charizard flies around the sky in search of powerful opponents.\nIt breathes fire of such great heat that it melts anything.\nHowever, it never turns its fiery breath on any opponent\nweaker than itself.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "強い　相手を　求めて　空を　飛び回る。\nなんでも　溶かして　しまう　高熱の　炎を\n自分より　弱いものに　向けることは　しない。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "つよい　あいてを　もとめて　そらを　とびまわる。\nなんでも　とかして　しまう　こうねつの　ほのおを\nじぶんより　よわいものに　むけることは　しない。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "강한 상대를 찾아 하늘을 날아다닌다.\n무엇이든 다 녹여버리는 고열의 불꽃을\n자신보다 약한 자에게 들이대지 않는다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Dracaufeu parcourt les cieux pour trouver des adversaires\nà sa mesure. Il crache de puissantes flammes capables de\nfaire fondre n’importe quoi. Mais il ne dirige jamais son souffle\ndestructeur vers un ennemi plus faible.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Glurak fliegt durch die Lüfte, um starke Gegner aufzuspüren.\nSein heißer Feueratem bringt alles zum Schmelzen. Aber es\nrichtet seinen Feueratem nie gegen schwächere Gegner.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Charizard se dedica a volar por los cielos en busca de\noponentes fuertes. Echa fuego por la boca y es capaz de\nderretir cualquier cosa. No obstante, si su rival es más débil\nque él, no usará este ataque.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Charizard solca i cieli in cerca di nemici molto forti.\nRiesce a emettere fiammate di un calore tale da fondere\nogni cosa. Tuttavia, non rivolge mai le sue micidiali lingue\ndi fuoco contro avversari più deboli di lui.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Charizard flies around the sky in search of powerful opponents.\nIt breathes fire of such great heat that it melts anything.\nHowever, it never turns its fiery breath on any opponent\nweaker than itself.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "強い　相手を　求めて　空を　飛び回る。\nなんでも　溶かして　しまう　高熱の　炎を\n自分より　弱いものに　向けることは　しない。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "くちから　しゃくねつの　ほのおを\nはきだすとき　シッポのさきは\nより　あかく　はげしく　もえあがる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "입에서 작렬하는 불꽃을\n토해낼 때 꼬리의 끝이\n더욱 붉고 격렬하게 타오른다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "從口中噴出熾熱的火焰時，\n尾巴尖端的紅色火焰\n會燃燒得更加激烈。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Quand il crache son souffle brûlant, la flamme\nau bout de sa queue s’embrase.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Wenn es einen Strahl glühenden Feuers speit,\nlodert die rote Flamme an seiner Schwanzspitze\nnoch intensiver.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Cuando exhala fuego abrasador, la llama de la\npunta de la cola se aviva y adquiere un intenso\ncolor rojo.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Quando emette lingue di fuoco roventi\ndalla bocca, la fiamma rossa sulla punta\ndella coda brucia più intensamente.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "When this Pokémon expels a blast of superhot\nfire, the red flame at the tip of its tail burns\nmore intensely.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "口から　灼熱の　炎を\n吐き出すとき　シッポの先は\nより　赤く　激しく　燃えあがる。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "从口中喷出灼热的火焰时，\n尾巴尖端的红色火焰\n会燃烧得更加猛烈。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "くちから　しゃくねつの　ほのおを\nはきだすとき　シッポのさきは\nより　あかく　はげしく　もえあがる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "입에서 작렬하는 불꽃을\n토해낼 때 꼬리의 끝이\n더욱 붉고 격렬하게 타오른다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "從口中噴出熾熱的火焰時，\n尾巴尖端的紅色火焰\n會燃燒得更加激烈。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Quand il crache son souffle brûlant, la flamme\nau bout de sa queue s’embrase.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Wenn es einen Strahl glühenden Feuers speit,\nlodert die rote Flamme an seiner Schwanzspitze\nnoch intensiver.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Cuando exhala fuego abrasador, la llama de la\npunta de la cola se aviva y adquiere un intenso\ncolor rojo.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Quando emette lingue di fuoco roventi\ndalla bocca, la fiamma rossa sulla punta\ndella coda brucia più intensamente.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "When this Pokémon expels a blast of superhot\nfire, the red flame at the tip of its tail burns\nmore intensely.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "口から　灼熱の　炎を\n吐き出すとき　シッポの先は\nより　赤く　激しく　燃えあがる。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "从口中喷出灼热的火焰时，\n尾巴尖端的红色火焰\n会燃烧得更加猛烈。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "がんせきも　やけるような\nしゃくねつの　ほのおを　はいて\nやまかじを　おこすことが　ある。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "암석도 태워버릴 정도로\n작열하는 화염을 뿜어\n산불을 일으킬 때가 있다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "會噴出彷彿連岩石\n都能燒焦的灼熱火焰。\n有時會引發森林火災。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Son souffle brûlant peut faire fondre la roche.\nIl est parfois la cause d’incendies de forêt.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Dieses Pokémon kann mit seinem Feueratem\nFelsen schmelzen. Es verursacht ab und zu\nWaldbrände.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Escupe un fuego tan caliente que funde las rocas.\nCausa incendios forestales sin querer.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Sputa fiamme incandescenti in grado di fondere\nle rocce. A volte causa incendi boschivi.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "It spits fire that is hot enough to melt boulders.\nIt may cause forest fires by blowing flames.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "岩石も　焼けるような\n灼熱の　炎を　吐いて\n山火事を　起こすことが　ある。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "能够喷出猛烈的火焰，\n仿佛连岩石都能烤焦。\n有时会引发森林火灾。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "ちじょう　１４００メートル　まで\nハネを　つかって　とぶことができる。\nこうねつの　ほのおを　はく。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "지상 1400m까지\n날개를 사용해 날 수 있다.\n고열의 불꽃을 내뿜는다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "能用翅膀飛到距離地面\n１４００公尺的高度。\n會吐出高溫的火焰。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Ses ailes lui permettent de voler à plus de\n1 400 m d’altitude. Ce Pokémon crache du feu\nà des températures très élevées.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Dieses Pokémon kann mit seinen Flügeln eine\nHöhe von bis zu 1 400 m erreichen. Es spuckt\nsehr heißes Feuer.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Sus potentes alas le permiten volar a una altura\nde 1400 m. Escupe llamaradas que llegan a\nalcanzar temperaturas elevadísimas.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Grazie alle possenti ali può volare fino a\n1.400 m d’altezza. Le fiamme che sputa\npossono raggiungere temperature altissime.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Its wings can carry this Pokémon close to an\naltitude of 4,600 feet. It blows out fire at very\nhigh temperatures.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "地上　１４００メートル　まで\n羽を　使って　飛ぶことができる。\n高熱の　炎を　吐く。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "能用翅膀飞到距地面\n１４００米的高度。\n会吐出高温火焰。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        }
      ],
      "form_descriptions": [],
      "forms_switchable": True,
      "gender_rate": 1,
      "genera": [
        {
          "genus": "かえんポケモン",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          }
        },
        {
          "genus": "화염포켓몬",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          }
        },
        {
          "genus": "火焰寶可夢",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          }
        },
        {
          "genus": "Pokémon Flamme",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          }
        },
        {
          "genus": "Flammen-Pokémon",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        },
        {
          "genus": "Pokémon Llama",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          }
        },
        {
          "genus": "Pokémon Fiamma",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          }
        },
        {
          "genus": "Flame Pokémon",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        },
        {
          "genus": "かえんポケモン",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          }
        },
        {
          "genus": "火焰宝可梦",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          }
        }
      ],
      "generation": {
        "name": "generation-i",
        "url": "https://pokeapi.co/api/v2/generation/1/"
      },
      "growth_rate": {
        "name": "medium-slow",
        "url": "https://pokeapi.co/api/v2/growth-rate/4/"
      },
      "habitat": {
        "name": "mountain",
        "url": "https://pokeapi.co/api/v2/pokemon-habitat/4/"
      },
      "has_gender_differences": False,
      "hatch_counter": 20,
      "id": 6,
      "is_baby": False,
      "is_legendary": False,
      "is_mythical": False,
      "name": "charizard",
      "names": [
        {
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "name": "リザードン"
        },
        {
          "language": {
            "name": "roomaji",
            "url": "https://pokeapi.co/api/v2/language/2/"
          },
          "name": "Lizardon"
        },
        {
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "name": "리자몽"
        },
        {
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "name": "噴火龍"
        },
        {
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "name": "Dracaufeu"
        },
        {
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "name": "Glurak"
        },
        {
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "name": "Charizard"
        },
        {
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "name": "Charizard"
        },
        {
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "name": "Charizard"
        },
        {
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "name": "リザードン"
        },
        {
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "name": "喷火龙"
        }
      ],
      "order": 6,
      "pal_park_encounters": [
        {
          "area": {
            "name": "field",
            "url": "https://pokeapi.co/api/v2/pal-park-area/2/"
          },
          "base_score": 90,
          "rate": 3
        }
      ],
      "pokedex_numbers": [
        {
          "entry_number": 6,
          "pokedex": {
            "name": "national",
            "url": "https://pokeapi.co/api/v2/pokedex/1/"
          }
        },
        {
          "entry_number": 6,
          "pokedex": {
            "name": "kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/2/"
          }
        },
        {
          "entry_number": 231,
          "pokedex": {
            "name": "original-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/3/"
          }
        },
        {
          "entry_number": 236,
          "pokedex": {
            "name": "updated-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/7/"
          }
        },
        {
          "entry_number": 111,
          "pokedex": {
            "name": "conquest-gallery",
            "url": "https://pokeapi.co/api/v2/pokedex/11/"
          }
        },
        {
          "entry_number": 85,
          "pokedex": {
            "name": "kalos-central",
            "url": "https://pokeapi.co/api/v2/pokedex/12/"
          }
        },
        {
          "entry_number": 6,
          "pokedex": {
            "name": "letsgo-kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/26/"
          }
        },
        {
          "entry_number": 380,
          "pokedex": {
            "name": "galar",
            "url": "https://pokeapi.co/api/v2/pokedex/27/"
          }
        },
        {
          "entry_number": 169,
          "pokedex": {
            "name": "blueberry",
            "url": "https://pokeapi.co/api/v2/pokedex/33/"
          }
        }
      ],
      "shape": {
        "name": "upright",
        "url": "https://pokeapi.co/api/v2/pokemon-shape/6/"
      },
      "varieties": [
        {
          "is_default": True,
          "pokemon": {
            "name": "charizard",
            "url": "https://pokeapi.co/api/v2/pokemon/6/"
          }
        },
        {
          "is_default": False,
          "pokemon": {
            "name": "charizard-mega-x",
            "url": "https://pokeapi.co/api/v2/pokemon/10034/"
          }
        },
        {
          "is_default": False,
          "pokemon": {
            "name": "charizard-mega-y",
            "url": "https://pokeapi.co/api/v2/pokemon/10035/"
          }
        },
        {
          "is_default": False,
          "pokemon": {
            "name": "charizard-gmax",
            "url": "https://pokeapi.co/api/v2/pokemon/10196/"
          }
        }
      ]
    },
    {
      "base_happiness": 50,
      "capture_rate": 45,
      "color": {
        "name": "blue",
        "url": "https://pokeapi.co/api/v2/pokemon-color/2/"
      },
      "egg_groups": [
        {
          "name": "monster",
          "url": "https://pokeapi.co/api/v2/egg-group/1/"
        },
        {
          "name": "water1",
          "url": "https://pokeapi.co/api/v2/egg-group/2/"
        }
      ],
      "evolution_chain": {
        "url": "https://pokeapi.co/api/v2/evolution-chain/3/"
      },
      "evolves_from_species": None,
      "flavor_text_entries": [
        {
          "flavor_text": "After birth, its\nback swells and\nhardens into a\fshell. Powerfully\nsprays foam from\nits mouth.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "red",
            "url": "https://pokeapi.co/api/v2/version/1/"
          }
        },
        {
          "flavor_text": "After birth, its\nback swells and\nhardens into a\fshell. Powerfully\nsprays foam from\nits mouth.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "blue",
            "url": "https://pokeapi.co/api/v2/version/2/"
          }
        },
        {
          "flavor_text": "Shoots water at\nprey while in the\nwater.\fWithdraws into\nits shell when in\ndanger.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version/3/"
          }
        },
        {
          "flavor_text": "The shell is soft\nwhen it is born.\nIt soon becomes so\fresilient, prod­\nding fingers will\nbounce off it.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "gold",
            "url": "https://pokeapi.co/api/v2/version/4/"
          }
        },
        {
          "flavor_text": "The shell, which\nhardens soon after\nit is born, is\fresilient. If you\npoke it, it will\nbounce back out.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "silver",
            "url": "https://pokeapi.co/api/v2/version/5/"
          }
        },
        {
          "flavor_text": "When it feels\nthreatened, it\ndraws its legs\finside its shell\nand sprays water\nfrom its mouth.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version/6/"
          }
        },
        {
          "flavor_text": "SQUIRTLE’s shell is not merely used\nfor protection.\nThe shell’s rounded shape and the\fgrooves on its surface help minimize\nresistance in water, enabling this\nPOKéMON to swim at high speeds.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "ruby",
            "url": "https://pokeapi.co/api/v2/version/7/"
          }
        },
        {
          "flavor_text": "SQUIRTLE’s shell is not merely used\nfor protection.\nThe shell’s rounded shape and the\fgrooves on its surface help minimize\nresistance in water, enabling this\nPOKéMON to swim at high speeds.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sapphire",
            "url": "https://pokeapi.co/api/v2/version/8/"
          }
        },
        {
          "flavor_text": "Its shell is not just for protection.\nIts rounded shape and the grooves on its\nsurface minimize resistance in water,\nenabling SQUIRTLE to swim at high speeds.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version/9/"
          }
        },
        {
          "flavor_text": "When it retracts its long neck into its\nshell, it squirts out water with vigorous\nforce.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "firered",
            "url": "https://pokeapi.co/api/v2/version/10/"
          }
        },
        {
          "flavor_text": "After birth, its back swells and hardens\ninto a shell. It powerfully sprays foam \nfrom its mouth.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "leafgreen",
            "url": "https://pokeapi.co/api/v2/version/11/"
          }
        },
        {
          "flavor_text": "It shelters itself in its shell,\nthen strikes back with spouts of\nwater at every opportunity.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "diamond",
            "url": "https://pokeapi.co/api/v2/version/12/"
          }
        },
        {
          "flavor_text": "It shelters itself in its shell,\nthen strikes back with spouts of\nwater at every opportunity.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "pearl",
            "url": "https://pokeapi.co/api/v2/version/13/"
          }
        },
        {
          "flavor_text": "It shelters itself in its shell,\nthen strikes back with spouts of\nwater at every opportunity.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version/14/"
          }
        },
        {
          "flavor_text": "The shell is soft when it is born.\nIt soon becomes so resilient,\nprodding fingers will bounce off it.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "heartgold",
            "url": "https://pokeapi.co/api/v2/version/15/"
          }
        },
        {
          "flavor_text": "The shell, which hardens soon after\nit is born, is resilient. If you\npoke it, it will bounce back out.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "soulsilver",
            "url": "https://pokeapi.co/api/v2/version/16/"
          }
        },
        {
          "flavor_text": "Il se réfugie dans sa carapace\net réplique en éclaboussant\nl’ennemi à la première occasion.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "It shelters itself in its shell,\nthen strikes back with spouts of\nwater at every opportunity.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "Il se réfugie dans sa carapace\net réplique en éclaboussant\nl’ennemi à la première occasion.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "It shelters itself in its shell,\nthen strikes back with spouts of\nwater at every opportunity.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "It shelters itself in its shell\nthen strikes back with spouts of\nwater at every opportunity.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black-2",
            "url": "https://pokeapi.co/api/v2/version/21/"
          }
        },
        {
          "flavor_text": "It shelters itself in its shell\nthen strikes back with spouts of\nwater at every opportunity.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white-2",
            "url": "https://pokeapi.co/api/v2/version/22/"
          }
        },
        {
          "flavor_text": "こうらに　とじこもり　みを　まもる。\nあいての　すきを　みのがさず\nみずを　ふきだして　はんげきする。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "등껍질에 숨어 몸을 보호한다.\n상대의 빈틈을 놓치지 않고\n물을 뿜어내어 반격한다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Il se réfugie dans sa carapace et réplique en\néclaboussant l’ennemi à la première occasion.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Es zieht sich in seinen Panzer zurück und greift\ndann mit Wasserstrahlen seine Gegner an.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Se protege con su caparazón y luego contraataca\nlanzando agua a presión cuando tiene oportunidad.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Si ritira nel suo guscio e, alla prima occasione,\ncontrattacca colpendo il nemico con spruzzi d’acqua.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "It shelters itself in its shell, then strikes back\nwith spouts of water at every opportunity.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "甲羅に　閉じこもり　身を　守る。\n相手の　すきを　見逃さず\n水を　噴き出して　反撃する。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "すいめんから　みずを　ふんしゃして\nエサをとる。あぶなくなると　こうらに\nてあしを　ひっこめて　みをまもる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "수면에서 물을 분사하여\n먹이를 잡는다. 위험해지면 등껍질에\n손발을 감추고 몸을 지킨다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Caché sous l’eau, il crache un jet d’eau sur sa proie\net se cache à l’intérieur de sa carapace.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Dieses Pokémon jagt mit einem Wasserstrahl.\nBei Gefahr zieht es sich in seinen Panzer zurück.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Lanza agua a su presa desde el agua. Se esconde en\nsu concha cuando se siente en peligro.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Attacca i nemici con potenti getti d’acqua. Se si\nsente in pericolo si ritira dentro la sua corazza.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Shoots water at prey while in the water. Withdraws\ninto its shell when in danger.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "水面から　水を　噴射して\nエサを　取る。危なくなると　甲羅に\n手足を　ひっこめて　身を　守る。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "こうらの　やくめは　みを　まもる　だけではない。\nまるい　かたちと　ひょうめんの　みぞが　みずの\nていこうを　へらすので　はやく　およげるのだ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "등껍질의 역할은 몸을 지키는 것뿐만이 아니다.\n둥그런 모양과 표면의 홈이 물의\n저항을 줄여서 빠르게 헤엄칠 수 있다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "La carapace de Carapuce ne sert pas qu’à le protéger.\nLa forme ronde de sa carapace et ses rainures lui permettent\nd’améliorer son hydrodynamisme.\nCe Pokémon nage extrêmement vite.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Schiggys Panzer dient nicht nur zum Schutz. Die runde Form\nund die Furchen auf der Oberfläche verringern den Widerstand\nim Wasser, sodass dieses Pokémon sehr schnell schwimmen\nkann.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "El caparazón de Squirtle no le sirve de protección únicamente.\nSu forma redondeada y las hendiduras que tiene le ayudan\na deslizarse en el agua y le permiten nadar a gran velocidad.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "La corazza di Squirtle non serve soltanto da protezione.\nLa particolare forma arrotondata e le scanalature\nsuperficiali lo aiutano a minimizzare l’attrito dell’acqua\nper nuotare ad alta velocità.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Squirtle’s shell is not merely used for protection.\nThe shell’s rounded shape and the grooves on its surface\nhelp minimize resistance in water, enabling this Pokémon\nto swim at high speeds.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "甲羅の　役目は　身を　守る　だけではない。\n丸い　形と　表面の　溝が　水の\n抵抗を　減らすので　早く　泳げるのだ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "こうらの　やくめは　みを　まもる　だけではない。\nまるい　かたちと　ひょうめんの　みぞが　みずの\nていこうを　へらすので　はやく　およげるのだ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "등껍질의 역할은 몸을 지키는 것뿐만이 아니다.\n둥그런 모양과 표면의 홈이 물의\n저항을 줄여서 빠르게 헤엄칠 수 있다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "La carapace de Carapuce ne sert pas qu’à le protéger.\nLa forme ronde de sa carapace et ses rainures lui permettent\nd’améliorer son hydrodynamisme.\nCe Pokémon nage extrêmement vite.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Schiggys Panzer dient nicht nur zum Schutz. Die runde Form\nund die Furchen auf der Oberfläche verringern den Widerstand\nim Wasser, sodass dieses Pokémon sehr schnell schwimmen\nkann.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "El caparazón de Squirtle no le sirve de protección únicamente.\nSu forma redondeada y las hendiduras que tiene le ayudan\na deslizarse en el agua y le permiten nadar a gran velocidad.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "La corazza di Squirtle non serve soltanto da protezione.\nLa particolare forma arrotondata e le scanalature\nsuperficiali lo aiutano a minimizzare l’attrito dell’acqua\nper nuotare ad alta velocità.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Squirtle’s shell is not merely used for protection.\nThe shell’s rounded shape and the grooves on its\nsurface help minimize resistance in water,\nenabling this Pokémon to swim at high speeds.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "甲羅の　役目は　身を　守る　だけではない。\n丸い　形と　表面の　溝が　水の\n抵抗を　減らすので　早く　泳げるのだ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "すいめんから　みずを　ふんしゃして\nエサをとる。あぶなくなると　こうらに\nてあしを　ひっこめて　みをまもる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "수면에서 물을 분사하여\n먹이를 잡는다. 위험해지면 등껍질에\n손발을 감추고 몸을 지킨다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "會從水面噴水來擊落獵物。\n當遇到危險時，會把手腳\n縮進甲殼裡保護自己。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Caché sous les flots, il crache un jet d’eau sur\nsa proie et se réfugie à l’intérieur de sa carapace\nen cas de danger.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Es greift seine Beute aus dem Wasser heraus mit\neinem Wasserstrahl an. Bei Gefahr zieht es sich\nin seinen Panzer zurück.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Escupe chorros de agua mientras flota para\ncapturar a sus presas. Se esconde en su\ncaparazón cuando se siente en peligro.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Se ne sta tra i flutti e attacca le prede con\npotenti getti d’acqua. Se si sente in pericolo\nsi ritira dentro la corazza.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Shoots water at prey while in the water.\nWithdraws into its shell when in danger.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "水面から　水を　噴射して\nエサをとる。危なくなると　こうらに\n手足を　引っこめて　身を守る。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "通过从水面喷水来捕食。\n在危急时刻会将四肢\n缩入龟壳里保护自己。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "すいめんから　みずを　ふんしゃして\nエサをとる。あぶなくなると　こうらに\nてあしを　ひっこめて　みをまもる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "수면에서 물을 분사하여\n먹이를 잡는다. 위험해지면 등껍질에\n손발을 감추고 몸을 지킨다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "會從水面噴水來擊落獵物。\n當遇到危險時，會把手腳\n縮進甲殼裡保護自己。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Caché sous les flots, il crache un jet d’eau sur\nsa proie et se réfugie à l’intérieur de sa carapace\nen cas de danger.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Es greift seine Beute aus dem Wasser heraus mit\neinem Wasserstrahl an. Bei Gefahr zieht es sich\nin seinen Panzer zurück.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Escupe chorros de agua mientras flota para\ncapturar a sus presas. Se esconde en su\ncaparazón cuando se siente en peligro.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Se ne sta tra i flutti e attacca le prede con\npotenti getti d’acqua. Se si sente in pericolo\nsi ritira dentro la corazza.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Shoots water at prey while in the water.\nWithdraws into its shell when in danger.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "水面から　水を　噴射して\nエサをとる。危なくなると　こうらに\n手足を　引っこめて　身を守る。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "通过从水面喷水来捕食。\n在危急时刻会将四肢\n缩入龟壳里保护自己。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "ながい　くびを　こうらのなかに\nひっこめるとき　いきおいよく\nみずでっぽうを　はっしゃする。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "기다란 목을 등껍질 속에\n감춘 다음 기세 좋게\n물대포를 발사한다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "當牠把長長的脖子縮回\n殼裡時，會順勢發射\n力道強勁的水槍。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Quand il rentre son cou dans sa carapace,\nil peut projeter de l’eau à haute pression.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Zieht es seinen langen Hals in seinen Panzer\nzurück, verspritzt es Wasser mit unbändiger Kraft.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Cuando retrae su largo cuello en el caparazón,\ndispara agua a una presión increíble.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Quando ritrae il lungo collo dentro la corazza\nsputa un vigoroso getto d’acqua.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "When it retracts its long neck into its shell, it\nsquirts out water with vigorous force.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "長い　首を　甲羅のなかに\n引っこめるとき　勢いよく\n水鉄砲を　発射する。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "当它把长长的脖子缩回\n壳里时，会顺势发射出\n力道强劲的水枪。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "あぶなくなると　こうらに　てあしを\nひっこめて　みを　まもりながら\nくちから　みずを　ふきだしてくる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "위험해지면 등껍질에 손발을\n감추고 몸을 지키면서\n입에서 물을 내뿜는다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "當牠遇到危險的時候，\n會將四肢收回甲殼裡保護自己，\n同時從嘴裡噴出水來。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "S’il se sent menacé, il rétracte ses pattes dans\nsa carapace pour se protéger et crache de l’eau.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Fühlt es sich bedroht, verkriecht es sich in seinen\nPanzer und spuckt Wasser aus seinem Maul.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Cuando se siente en peligro, se esconde en su\ncaparazón y escupe chorros de agua por la boca.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Se si sente minacciato, ritira le zampe nel guscio\ne inizia a spruzzare acqua dalla bocca.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "When it feels threatened, it draws its limbs inside\nits shell and sprays water from its mouth.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "危なくなると　甲羅に　手足を\n引っこめて　身を　守りながら\n口から　水を　吹き出している。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "当它遇到危险的时候，\n会将四肢收回龟壳里保护自己，\n同时从嘴里喷出水来。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        }
      ],
      "form_descriptions": [],
      "forms_switchable": False,
      "gender_rate": 1,
      "genera": [
        {
          "genus": "かめのこポケモン",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          }
        },
        {
          "genus": "꼬마거북포켓몬",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          }
        },
        {
          "genus": "小龜寶可夢",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          }
        },
        {
          "genus": "Pokémon Minitortue",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          }
        },
        {
          "genus": "Minikröten-Pokémon",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        },
        {
          "genus": "Pokémon Tortuguita",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          }
        },
        {
          "genus": "Pokémon Tartaghina",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          }
        },
        {
          "genus": "Tiny Turtle Pokémon",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        },
        {
          "genus": "かめのこポケモン",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          }
        },
        {
          "genus": "小龟宝可梦",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          }
        }
      ],
      "generation": {
        "name": "generation-i",
        "url": "https://pokeapi.co/api/v2/generation/1/"
      },
      "growth_rate": {
        "name": "medium-slow",
        "url": "https://pokeapi.co/api/v2/growth-rate/4/"
      },
      "habitat": {
        "name": "waters-edge",
        "url": "https://pokeapi.co/api/v2/pokemon-habitat/9/"
      },
      "has_gender_differences": False,
      "hatch_counter": 20,
      "id": 7,
      "is_baby": False,
      "is_legendary": False,
      "is_mythical": False,
      "name": "squirtle",
      "names": [
        {
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "name": "ゼニガメ"
        },
        {
          "language": {
            "name": "roomaji",
            "url": "https://pokeapi.co/api/v2/language/2/"
          },
          "name": "Zenigame"
        },
        {
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "name": "꼬부기"
        },
        {
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "name": "傑尼龜"
        },
        {
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "name": "Carapuce"
        },
        {
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "name": "Schiggy"
        },
        {
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "name": "Squirtle"
        },
        {
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "name": "Squirtle"
        },
        {
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "name": "Squirtle"
        },
        {
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "name": "ゼニガメ"
        },
        {
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "name": "杰尼龟"
        }
      ],
      "order": 7,
      "pal_park_encounters": [
        {
          "area": {
            "name": "pond",
            "url": "https://pokeapi.co/api/v2/pal-park-area/4/"
          },
          "base_score": 50,
          "rate": 30
        }
      ],
      "pokedex_numbers": [
        {
          "entry_number": 7,
          "pokedex": {
            "name": "national",
            "url": "https://pokeapi.co/api/v2/pokedex/1/"
          }
        },
        {
          "entry_number": 7,
          "pokedex": {
            "name": "kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/2/"
          }
        },
        {
          "entry_number": 232,
          "pokedex": {
            "name": "original-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/3/"
          }
        },
        {
          "entry_number": 237,
          "pokedex": {
            "name": "updated-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/7/"
          }
        },
        {
          "entry_number": 86,
          "pokedex": {
            "name": "kalos-central",
            "url": "https://pokeapi.co/api/v2/pokedex/12/"
          }
        },
        {
          "entry_number": 7,
          "pokedex": {
            "name": "letsgo-kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/26/"
          }
        },
        {
          "entry_number": 71,
          "pokedex": {
            "name": "isle-of-armor",
            "url": "https://pokeapi.co/api/v2/pokedex/28/"
          }
        },
        {
          "entry_number": 170,
          "pokedex": {
            "name": "blueberry",
            "url": "https://pokeapi.co/api/v2/pokedex/33/"
          }
        }
      ],
      "shape": {
        "name": "upright",
        "url": "https://pokeapi.co/api/v2/pokemon-shape/6/"
      },
      "varieties": [
        {
          "is_default": True,
          "pokemon": {
            "name": "squirtle",
            "url": "https://pokeapi.co/api/v2/pokemon/7/"
          }
        }
      ]
    },
    {
      "base_happiness": 50,
      "capture_rate": 45,
      "color": {
        "name": "blue",
        "url": "https://pokeapi.co/api/v2/pokemon-color/2/"
      },
      "egg_groups": [
        {
          "name": "monster",
          "url": "https://pokeapi.co/api/v2/egg-group/1/"
        },
        {
          "name": "water1",
          "url": "https://pokeapi.co/api/v2/egg-group/2/"
        }
      ],
      "evolution_chain": {
        "url": "https://pokeapi.co/api/v2/evolution-chain/3/"
      },
      "evolves_from_species": {
        "name": "squirtle",
        "url": "https://pokeapi.co/api/v2/pokemon-species/7/"
      },
      "flavor_text_entries": [
        {
          "flavor_text": "Often hides in\nwater to stalk\nunwary prey. For\fswimming fast, it\nmoves its ears to\nmaintain balance.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "red",
            "url": "https://pokeapi.co/api/v2/version/1/"
          }
        },
        {
          "flavor_text": "Often hides in\nwater to stalk\nunwary prey. For\fswimming fast, it\nmoves its ears to\nmaintain balance.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "blue",
            "url": "https://pokeapi.co/api/v2/version/2/"
          }
        },
        {
          "flavor_text": "When tapped, this\nPOKéMON will pull\nin its head, but\fits tail will\nstill stick out a\nlittle bit.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version/3/"
          }
        },
        {
          "flavor_text": "It is recognized\nas a symbol of\nlongevity. If its\fshell has algae on\nit, that WARTORTLE\nis very old.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "gold",
            "url": "https://pokeapi.co/api/v2/version/4/"
          }
        },
        {
          "flavor_text": "It cleverly con­\ntrols its furry\nears and tail to\fmaintain its\nbalance while\nswimming.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "silver",
            "url": "https://pokeapi.co/api/v2/version/5/"
          }
        },
        {
          "flavor_text": "Its long, furry\ntail is a symbol\nof longevity,\fmaking it quite\npopular among\nolder people.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version/6/"
          }
        },
        {
          "flavor_text": "Its tail is large and covered with a rich,\nthick fur. The tail becomes increasingly\ndeeper in color as WARTORTLE ages.\fThe scratches on its shell are evidence\nof this POKéMON’s toughness as a\nbattler.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "ruby",
            "url": "https://pokeapi.co/api/v2/version/7/"
          }
        },
        {
          "flavor_text": "Its tail is large and covered with a rich,\nthick fur. The tail becomes increasingly\ndeeper in color as WARTORTLE ages.\fThe scratches on its shell are evidence\nof this POKéMON’s toughness as a\nbattler.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sapphire",
            "url": "https://pokeapi.co/api/v2/version/8/"
          }
        },
        {
          "flavor_text": "Its large tail is covered with rich, thick\nfur that deepens in color with age.\nThe scratches on its shell are evidence\nof this POKéMON’s toughness in battle.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version/9/"
          }
        },
        {
          "flavor_text": "This POKéMON is very popular as a pet.\nIts fur-covered tail is a symbol of its\nlongevity.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "firered",
            "url": "https://pokeapi.co/api/v2/version/10/"
          }
        },
        {
          "flavor_text": "It often hides in water to stalk unwary\nprey. For fast swimming, it moves its\nears to maintain balance.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "leafgreen",
            "url": "https://pokeapi.co/api/v2/version/11/"
          }
        },
        {
          "flavor_text": "It is said to live 10,000 years.\nIts furry tail is popular as a\nsymbol of longevity.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "diamond",
            "url": "https://pokeapi.co/api/v2/version/12/"
          }
        },
        {
          "flavor_text": "It is said to live 10,000 years.\nIts furry tail is popular as a\nsymbol of longevity.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "pearl",
            "url": "https://pokeapi.co/api/v2/version/13/"
          }
        },
        {
          "flavor_text": "It is said to live 10,000 years.\nIts furry tail is popular as a\nsymbol of longevity.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version/14/"
          }
        },
        {
          "flavor_text": "It is a well-established symbol of\nlongevity. If its shell has algae on it,\nthat WARTORTLE is very old.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "heartgold",
            "url": "https://pokeapi.co/api/v2/version/15/"
          }
        },
        {
          "flavor_text": "It cleverly controls its furry\nears and tail to maintain its\nbalance while swimming.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "soulsilver",
            "url": "https://pokeapi.co/api/v2/version/16/"
          }
        },
        {
          "flavor_text": "On prétend qu’il vit 10 000 ans.\nSa queue duveteuse est un\nsymbole de longévité populaire.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "It is said to live 10,000 years.\nIts furry tail is popular as a\nsymbol of longevity.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "On prétend qu’il vit 10 000 ans.\nSa queue duveteuse est un\nsymbole de longévité populaire.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "It is said to live 10,000 years.\nIts furry tail is popular as a\nsymbol of longevity.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "It is said to live 10,000 years.\nIts furry tail is popular as a\nsymbol of longevity.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black-2",
            "url": "https://pokeapi.co/api/v2/version/21/"
          }
        },
        {
          "flavor_text": "It is said to live 10,000 years.\nIts furry tail is popular as a\nsymbol of longevity.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white-2",
            "url": "https://pokeapi.co/api/v2/version/22/"
          }
        },
        {
          "flavor_text": "ポカンと　あたまを　たたかれるとき\nこうらに　ひっこんで　よける。でも\nちょっとだけ　しっぽが　でているよ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "딱 하고 머리를 맞을 때\n등껍질로 숨어서 피한다. 하지만\n꼬리가 살짝 삐져나와 있다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Attaqué, il cache sa tête dans sa carapace, mais\nson corps trop gros ne peut y tenir en entier.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Bei Gefahr zieht dieses Pokémon seinen Kopf ein.\nDie Schwanzspitze ragt jedoch aus dem Panzer\nheraus.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Si es golpeado, esconderá su cabeza. Aun así, su cola\npuede seguir golpeando.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Quando si sente minacciato ritira la testa nella\ncorazza, mentre la coda sporge sempre un po’.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "When tapped, this Pokémon will pull in its head,\nbut its tail will still stick out a little bit.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "ポカンと　頭を　たたかれるとき\n甲羅に　引っこんで　避ける。でも\nちょっとだけ　尻尾が　出ているよ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "いちまんねんの　じゅみょうを　もつと\nいわれている。ふさふさの　しっぽは\nながいきの　シンボルとして　にんき。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "만 년의 수명을 가지고 있다고들\n말한다. 치렁치렁한 꼬리는\n장수의 상징으로서 인기가 있다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "On prétend qu’il vit 10 000 ans. Sa queue duveteuse\nest un symbole de longévité populaire.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Man sagt, es werde 10 000 Jahre alt. Sein buschiger\nSchweif ist ein Symbol für langes Leben.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Se dice que vive 10 000 años. Su peluda cola es un\nsímbolo de longevidad.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Pare che viva 10.000 anni. Ha la coda ricoperta da\nuna folta pelliccia, indice di longevità.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "It is said to live 10,000 years. Its furry tail is\npopular as a symbol of longevity.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "１万年の　寿命を　持つと\n言われている。ふさふさの　尻尾は\n長生きの　シンボルとして　人気。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "ふさふさの　けで　おおわれた　おおきな　しっぽは\nながいき　するほど　ふかい　いろあいに　かわる。\nこうらの　キズは　つわものの　あかし。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "푹신한 털로 덮인 큰 꼬리는\n오래 살수록 깊은 색으로 변한다.\n등껍질의 상처는 강자임을 증명한다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Carabaffe a une large queue recouverte d’une épaisse\nfourrure. Elle devient de plus en plus foncée avec l’âge.\nLes éraflures sur la carapace de ce Pokémon témoignent\nde son expérience au combat.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Schillok hat einen langen, buschigen Schweif, dessen Farbe\nintensiver wird, wenn es altert. Die Kratzer auf seinem Panzer\nzeugen von seiner Kampfkraft.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Tiene una cola larga y cubierta de un pelo abundante y\ngrueso que se torna más oscuro a medida que crece.\nLos arañazos que tiene en el caparazón dan fe de lo buen\nguerrero que es.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "La grande coda di Wartortle è coperta da una folta\npelliccia, che diventa sempre più scura con l’avanzare\ndell’età. I graffi sulla corazza indicano la potenza di questo\nPokémon come lottatore.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Its tail is large and covered with a rich, thick fur. The tail\nbecomes increasingly deeper in color as Wartortle ages.\nThe scratches on its shell are evidence of this Pokémon’s\ntoughness as a battler.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "ふさふさの　毛で　覆われた　大きな　尻尾は\n長生き　するほど　深い　色合いに　変わる。\n甲羅の　キズは　強者の　証。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "ふさふさの　けで　おおわれた　おおきな　しっぽは\nながいき　するほど　ふかい　いろあいに　かわる。\nこうらの　キズは　つわものの　あかし。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "푹신한 털로 덮인 큰 꼬리는\n오래 살수록 깊은 색으로 변한다.\n등껍질의 상처는 강자임을 증명한다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Carabaffe a une large queue recouverte d’une épaisse\nfourrure. Elle devient de plus en plus foncée avec l’âge.\nLes éraflures sur la carapace de ce Pokémon témoignent\nde son expérience au combat.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Schillok hat einen langen, buschigen Schweif, dessen Farbe\nintensiver wird, wenn es altert. Die Kratzer auf seinem Panzer\nzeugen von seiner Kampfkraft.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Tiene una cola larga y cubierta de un pelo abundante y\ngrueso que se torna más oscuro a medida que crece.\nLos arañazos que tiene en el caparazón dan fe de lo buen\nguerrero que es.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "La grande coda di Wartortle è coperta da una folta\npelliccia, che diventa sempre più scura con l’avanzare\ndell’età. I graffi sulla corazza indicano la potenza di questo\nPokémon come lottatore.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Its tail is large and covered with a rich, thick fur. The tail\nbecomes increasingly deeper in color as Wartortle ages.\nThe scratches on its shell are evidence of this Pokémon’s\ntoughness as a battler.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "ふさふさの　毛で　覆われた　大きな　尻尾は\n長生き　するほど　深い　色合いに　変わる。\n甲羅の　キズは　強者の　証。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "ポカンと　あたまを　たたかれるとき\nこうらに　ひっこんで　よける。でも\nちょっとだけ　シッポが　でているよ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "딱 하고 머리를 맞을 때\n등껍질로 숨어서 피한다. 하지만\n꼬리가 살짝 삐져나와 있다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "如果有人打牠的頭，\n牠會縮進殼裡來躲避，\n但會留下一小截尾巴在外面。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Quand on lui tapote la tête, il se cache dans\nsa carapace, mais son corps ne peut pas y tenir\nen entier.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Wenn es einen Schlag auf den Kopf bekommt,\nzieht es sich in seinen Panzer zurück. Seine\nSchwanzspitze ragt jedoch ein wenig heraus.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Si alguien le golpea la cabeza, se protege\nescondiéndose en su caparazón, aunque parte\nde la cola queda al descubierto.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Quando viene colpito sulla testa si ritira nella\ncorazza. La coda, però, sporge sempre un po’.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "When tapped on its head, this Pokémon will pull\nit in, but its tail will still stick out a little bit.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "ポカンと　頭を　たたかれるとき\nこうらに　引っこんで　よける。でも\nちょっとだけ　シッポが　出ているよ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "如果拍打它的头部，它会\n把头缩进壳里，但尾巴\n还是会露出来一点点。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "ポカンと　あたまを　たたかれるとき\nこうらに　ひっこんで　よける。でも\nちょっとだけ　シッポが　でているよ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "딱 하고 머리를 맞을 때\n등껍질로 숨어서 피한다. 하지만\n꼬리가 살짝 삐져나와 있다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "如果有人打牠的頭，\n牠會縮進殼裡來躲避，\n但會留下一小截尾巴在外面。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Quand on lui tapote la tête, il se cache dans\nsa carapace, mais son corps ne peut pas y tenir\nen entier.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Wenn es einen Schlag auf den Kopf bekommt,\nzieht es sich in seinen Panzer zurück. Seine\nSchwanzspitze ragt jedoch ein wenig heraus.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Si alguien le golpea la cabeza, se protege\nescondiéndose en su caparazón, aunque parte\nde la cola queda al descubierto.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Quando viene colpito sulla testa si ritira nella\ncorazza. La coda, però, sporge sempre un po’.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "When tapped on its head, this Pokémon will pull\nit in, but its tail will still stick out a little bit.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "ポカンと　頭を　たたかれるとき\nこうらに　引っこんで　よける。でも\nちょっとだけ　シッポが　出ているよ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "如果拍打它的头部，它会\n把头缩进壳里，但尾巴\n还是会露出来一点点。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "ながいきの　シンボルと　されている。\nこうらに　コケが　ついているのは\nとくに　ながいきの　カメールだ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "장수의 상징으로 여겨진다.\n등껍질에 이끼가 붙어 있는 것은\n특히 장수한 어니부기다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "被視為長壽的象徵。\n如果卡咪龜的殼上長著苔蘚，\n那就代表牠已經活了非常久。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Il est considéré comme un symbole de longévité.\nOn reconnaît les spécimens les plus âgés\nà la mousse qui pousse sur leur carapace.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Es gilt als Symbol für Langlebigkeit. Sehr alte\nExemplare erkennt man daran, dass ihr Panzer\nmit Algen übersät ist.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Se lo considera un símbolo de longevidad. Los\nejemplares más ancianos tienen musgo sobre el\ncaparazón.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "È considerato un simbolo di longevità.\nSe c’è del muschio sul suo guscio, significa\nche è molto anziano.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "It is recognized as a symbol of longevity. If its\nshell has algae on it, that Wartortle is very old.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "長生きの　シンボルと　されている。\n甲羅に　苔が　ついているのは\nとくに　長生きの　カメールだ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "被视为长寿的象征。\n如果卡咪龟的壳上长着苔藓，\n代表它已经活了非常久了。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "ふさふさの　みみと　しっぽを\nたくみに　あやつって　すいちゅうでの\nバランスを　たもつ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "탐스러운 귀와 꼬리를\n능숙하게 다뤄서 수중에서의\n밸런스를 유지한다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "會靈巧地擺動自己\n毛茸茸的耳朵和尾巴，\n藉此在水中保持平衡。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Il se sert habilement de sa queue et de ses\noreilles touffues pour garder son équilibre\nsous l’eau.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Es balanciert geschickt mit seinen buschigen\nOhren und dem Schweif, während es im Wasser\nschwimmt.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Utiliza hábilmente sus peludas orejas y la cola\npara mantener el equilibrio al nadar.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Controlla abilmente le orecchie e la coda\ncoperte di pelo, mantenendo l’assetto\nmentre nuota.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "It cleverly controls its furry ears and tail to\nmaintain its balance while swimming.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "ふさふさの　耳と　しっぽを\nたくみに　操って　水中での\nバランスを　たもつ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "会灵巧地摆动自己\n毛茸茸的耳朵和尾巴，\n借此在水中保持平衡。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        }
      ],
      "form_descriptions": [],
      "forms_switchable": False,
      "gender_rate": 1,
      "genera": [
        {
          "genus": "かめポケモン",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          }
        },
        {
          "genus": "거북포켓몬",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          }
        },
        {
          "genus": "龜寶可夢",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          }
        },
        {
          "genus": "Pokémon Tortue",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          }
        },
        {
          "genus": "Kröten-Pokémon",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        },
        {
          "genus": "Pokémon Tortuga",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          }
        },
        {
          "genus": "Pokémon Tartaruga",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          }
        },
        {
          "genus": "Turtle Pokémon",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        },
        {
          "genus": "かめポケモン",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          }
        },
        {
          "genus": "龟宝可梦",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          }
        }
      ],
      "generation": {
        "name": "generation-i",
        "url": "https://pokeapi.co/api/v2/generation/1/"
      },
      "growth_rate": {
        "name": "medium-slow",
        "url": "https://pokeapi.co/api/v2/growth-rate/4/"
      },
      "habitat": {
        "name": "waters-edge",
        "url": "https://pokeapi.co/api/v2/pokemon-habitat/9/"
      },
      "has_gender_differences": False,
      "hatch_counter": 20,
      "id": 8,
      "is_baby": False,
      "is_legendary": False,
      "is_mythical": False,
      "name": "wartortle",
      "names": [
        {
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "name": "カメール"
        },
        {
          "language": {
            "name": "roomaji",
            "url": "https://pokeapi.co/api/v2/language/2/"
          },
          "name": "Kameil"
        },
        {
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "name": "어니부기"
        },
        {
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "name": "卡咪龜"
        },
        {
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "name": "Carabaffe"
        },
        {
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "name": "Schillok"
        },
        {
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "name": "Wartortle"
        },
        {
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "name": "Wartortle"
        },
        {
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "name": "Wartortle"
        },
        {
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "name": "カメール"
        },
        {
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "name": "卡咪龟"
        }
      ],
      "order": 8,
      "pal_park_encounters": [
        {
          "area": {
            "name": "pond",
            "url": "https://pokeapi.co/api/v2/pal-park-area/4/"
          },
          "base_score": 80,
          "rate": 10
        }
      ],
      "pokedex_numbers": [
        {
          "entry_number": 8,
          "pokedex": {
            "name": "national",
            "url": "https://pokeapi.co/api/v2/pokedex/1/"
          }
        },
        {
          "entry_number": 8,
          "pokedex": {
            "name": "kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/2/"
          }
        },
        {
          "entry_number": 233,
          "pokedex": {
            "name": "original-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/3/"
          }
        },
        {
          "entry_number": 238,
          "pokedex": {
            "name": "updated-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/7/"
          }
        },
        {
          "entry_number": 87,
          "pokedex": {
            "name": "kalos-central",
            "url": "https://pokeapi.co/api/v2/pokedex/12/"
          }
        },
        {
          "entry_number": 8,
          "pokedex": {
            "name": "letsgo-kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/26/"
          }
        },
        {
          "entry_number": 72,
          "pokedex": {
            "name": "isle-of-armor",
            "url": "https://pokeapi.co/api/v2/pokedex/28/"
          }
        },
        {
          "entry_number": 171,
          "pokedex": {
            "name": "blueberry",
            "url": "https://pokeapi.co/api/v2/pokedex/33/"
          }
        }
      ],
      "shape": {
        "name": "upright",
        "url": "https://pokeapi.co/api/v2/pokemon-shape/6/"
      },
      "varieties": [
        {
          "is_default": True,
          "pokemon": {
            "name": "wartortle",
            "url": "https://pokeapi.co/api/v2/pokemon/8/"
          }
        }
      ]
    },
    {
      "base_happiness": 50,
      "capture_rate": 45,
      "color": {
        "name": "blue",
        "url": "https://pokeapi.co/api/v2/pokemon-color/2/"
      },
      "egg_groups": [
        {
          "name": "monster",
          "url": "https://pokeapi.co/api/v2/egg-group/1/"
        },
        {
          "name": "water1",
          "url": "https://pokeapi.co/api/v2/egg-group/2/"
        }
      ],
      "evolution_chain": {
        "url": "https://pokeapi.co/api/v2/evolution-chain/3/"
      },
      "evolves_from_species": {
        "name": "wartortle",
        "url": "https://pokeapi.co/api/v2/pokemon-species/8/"
      },
      "flavor_text_entries": [
        {
          "flavor_text": "A brutal POKéMON\nwith pressurized\nwater jets on its\fshell. They are\nused for high\nspeed tackles.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "red",
            "url": "https://pokeapi.co/api/v2/version/1/"
          }
        },
        {
          "flavor_text": "A brutal POKéMON\nwith pressurized\nwater jets on its\fshell. They are\nused for high\nspeed tackles.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "blue",
            "url": "https://pokeapi.co/api/v2/version/2/"
          }
        },
        {
          "flavor_text": "Once it takes aim\nat its enemy, it\nblasts out water\fwith even more\nforce than a fire\nhose.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version/3/"
          }
        },
        {
          "flavor_text": "It deliberately\nmakes itself heavy\nso it can with­\fstand the recoil\nof the water jets\nit fires.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "gold",
            "url": "https://pokeapi.co/api/v2/version/4/"
          }
        },
        {
          "flavor_text": "The rocket cannons\non its shell fire\njets of water\fcapable of punch­\ning holes through\nthick steel.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "silver",
            "url": "https://pokeapi.co/api/v2/version/5/"
          }
        },
        {
          "flavor_text": "It firmly plants\nits feet on the\nground before\fshooting water\nfrom the jets on\nits back.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version/6/"
          }
        },
        {
          "flavor_text": "BLASTOISE has water spouts that\nprotrude from its shell. The water\nspouts are very accurate.\fThey can shoot bullets of water with\nenough accuracy to strike empty cans\nfrom a distance of over 160 feet.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "ruby",
            "url": "https://pokeapi.co/api/v2/version/7/"
          }
        },
        {
          "flavor_text": "BLASTOISE has water spouts that\nprotrude from its shell. The water\nspouts are very accurate.\fThey can shoot bullets of water with\nenough accuracy to strike empty cans\nfrom a distance of over 160 feet.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sapphire",
            "url": "https://pokeapi.co/api/v2/version/8/"
          }
        },
        {
          "flavor_text": "The waterspouts that protrude from its\nshell are highly accurate. Their bullets of\nwater can precisely nail tin cans from\na distance of over 160 feet.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version/9/"
          }
        },
        {
          "flavor_text": "It crushes its foe under its heavy body\nto cause fainting. In a pinch, it will\nwithdraw inside its shell.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "firered",
            "url": "https://pokeapi.co/api/v2/version/10/"
          }
        },
        {
          "flavor_text": "The pressurized water jets on this brutal\nPOKéMON’s shell are used for high-\nspeed tackles.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "leafgreen",
            "url": "https://pokeapi.co/api/v2/version/11/"
          }
        },
        {
          "flavor_text": "The jets of water it spouts from\nthe rocket cannons on its shell\ncan punch through thick steel.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "diamond",
            "url": "https://pokeapi.co/api/v2/version/12/"
          }
        },
        {
          "flavor_text": "The jets of water it spouts from\nthe rocket cannons on its shell\ncan punch through thick steel.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "pearl",
            "url": "https://pokeapi.co/api/v2/version/13/"
          }
        },
        {
          "flavor_text": "The jets of water it spouts from\nthe rocket cannons on its shell\ncan punch through thick steel.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version/14/"
          }
        },
        {
          "flavor_text": "It deliberately makes itself heavy\nso it can withstand the recoil\nof the water jets it fires.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "heartgold",
            "url": "https://pokeapi.co/api/v2/version/15/"
          }
        },
        {
          "flavor_text": "The rocket cannons on its shell fire\njets of water capable of punching\nholes through thick steel.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "soulsilver",
            "url": "https://pokeapi.co/api/v2/version/16/"
          }
        },
        {
          "flavor_text": "Les trombes d’eau projetées par\nles canons de sa carapace peuvent\npercer le métal le plus résistant.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "The jets of water it spouts from\nthe rocket cannons on its shell\ncan punch through thick steel.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "Les trombes d’eau projetées par\nles canons de sa carapace peuvent\npercer le métal le plus résistant.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "The jets of water it spouts from\nthe rocket cannons on its shell\ncan punch through thick steel.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "The jets of water it spouts from\nthe rocket cannons on its shell\ncan punch through thick steel.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black-2",
            "url": "https://pokeapi.co/api/v2/version/21/"
          }
        },
        {
          "flavor_text": "The jets of water it spouts from\nthe rocket cannons on its shell\ncan punch through thick steel.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white-2",
            "url": "https://pokeapi.co/api/v2/version/22/"
          }
        },
        {
          "flavor_text": "からだが　おもたく　のしかかって\nあいてを　きぜつさせる。\nピンチの　ときは　カラに　かくれる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "무거운 몸으로 상대를\n덮쳐서 기절시킨다.\n위기에 처하면 등껍질에 숨는다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Il écrase ses adversaires de tout son poids pour leur\nfaire perdre connaissance. Il rentre dans sa carapace\ns’il se sent en danger.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Es begräbt seine Gegner mit seinem enormen\nKörpergewicht. Wenn es in einer aussichtslosen\nLage steckt, zieht es sich in seinen Panzer zurück.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Para acabar con su enemigo, lo aplasta con el peso de\nsu cuerpo. En momentos de apuro, se esconde en el\ncaparazón.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Mette KO gli avversari schiacciandoli sotto il corpo\npossente. Se è in difficoltà, può ritrarsi nella corazza.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "It crushes its foe under its heavy body to cause\nfainting. In a pinch, it will withdraw inside its shell.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "体が　重たく　のしかかって\n相手を　気絶させる。\nピンチのときは　殻に　隠れる。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "こうらに　ふんしゃこうが　あって\nロケットのような　いきおいで\nつっこんでくる　すごい　やつだ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "등껍질에 분사구가 있어\n로켓 같은 기세로\n덤벼드는 굉장한 녀석이다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Ce Pokémon brutal est armé de canons hydrauliques.\nSes puissants jets d’eau sont dévastateurs.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Ein mächtiges und schnelles Pokémon, das auf\ndem Rücken zwei Hochdruckwasserwerfer trägt.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Es un Pokémon imponente. Tiene reactores de agua\nen el caparazón, que le sirven para atacar con fuerza.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Pokémon brutale che lancia getti d’acqua ad alta\npressione dalla corazza, usati per attacchi rapidi.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "The pressurized water jets on this brutal Pokémon’s\nshell are used for high-speed tackles.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "甲羅に　噴射口が　あって\nロケットのような　勢いで\n突っこんでくる　すごい　やつだ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "こうらの　ふんしゃこうの　ねらいは　せいかく。\nみずの　だんがんを　５０メートル　はなれた\nあきかんに　めいちゅうさせる　ことが　できるぞ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "등껍질의 분사구로 하는 조준은 정확하다.\n물 탄환으로 50m 떨어진\n빈 캔을 명중시킬 수 있다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Tortank dispose de canons à eau émergeant de sa carapace.\nIls sont très précis et peuvent envoyer des balles d’eau\ncapables de faire mouche sur une cible située à plus de 50 m.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Turtok besitzt Wasserdüsen, die aus seinem\nPanzer herausragen. Diese sind sehr präzise.\nEs kann Wassergeschosse so genau verschießen,\ndass es damit aus fast 50 m leere Dosen trifft.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Blastoise lanza chorros de agua con gran precisión por los\ntubos que le salen del caparazón que tiene en la espalda.\nPuede disparar chorros de agua con tanta puntería que no\nfallaría al tirar contra una lata pequeña a 50 m.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Blastoise è dotato di cannoni ad acqua che fuoriescono dalla\ncorazza. I getti emessi sono così precisi da riuscire a colpire\nun bersaglio a una distanza di 50 m.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Blastoise has water spouts that protrude from its shell.\nThe water spouts are very accurate. They can shoot bullets of\nwater with enough accuracy to strike empty cans from a\ndistance of over 160 feet.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "甲羅の　噴射口の　ねらいは　正確。\n水の　弾丸を　５０メートル　離れた\n空き缶に　命中させる　ことが　できるぞ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "こうらの　ふんしゃこうの　ねらいは　せいかく。\nみずの　だんがんを　５０メートル　はなれた\nあきかんに　めいちゅうさせる　ことが　できるぞ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "등껍질의 분사구로 하는 조준은 정확하다.\n물 탄환으로 50m 떨어진\n빈 캔을 명중시킬 수 있다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Tortank dispose de canons à eau émergeant de sa carapace.\nIls sont très précis et peuvent envoyer des balles d’eau\ncapables de faire mouche sur une cible située à plus de 50 m.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Turtok besitzt Wasserdüsen, die aus seinem\nPanzer herausragen. Diese sind sehr präzise.\nEs kann Wassergeschosse so genau verschießen,\ndass es damit aus fast 50 m leere Dosen trifft.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Blastoise lanza chorros de agua con gran precisión por los\ntubos que le salen del caparazón que tiene en la espalda.\nPuede disparar chorros de agua con tanta puntería que no\nfallaría al tirar contra una lata pequeña a 50 m.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Blastoise è dotato di cannoni ad acqua che fuoriescono dalla\ncorazza. I getti emessi sono così precisi da riuscire a colpire\nun bersaglio a una distanza di 50 m.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Blastoise has water spouts that protrude from its shell.\nThe water spouts are very accurate.\nThey can shoot bullets of water with enough accuracy\nto strike empty cans from a distance of over 160 feet.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "甲羅の　噴射口の　ねらいは　正確。\n水の　弾丸を　５０メートル　離れた\n空き缶に　命中させる　ことが　できるぞ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "あいてに　ねらいを　さだめると\nしょうぼうしゃの　ホースより\nつよい　いきおいで　みずを　だす。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "상대를 겨냥한 다음\n소방차의 호스보다\n강한 기세로 물을 뿜는다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "在鎖定了目標之後，\n會用比消防車的水龍\n更強的力道來射出水柱。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Une fois sa cible dans sa ligne de mire,\nil projette des jets d’eau plus puissants\nqu’une lance à incendie.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Nachdem es einen Gegner anvisiert hat, greift\nes mit einem Wasserstrahl an, dessen Druck\nhöher ist als der eines Feuerwehrschlauchs.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Tras fijar el blanco, ataca disparando un chorro\nde agua a una presión mayor que la manguera\nde un bombero.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Dopo aver preso la mira colpisce il nemico con\ngetti d’acqua più potenti di quelli di un idrante.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Once it takes aim at its enemy, it blasts out\nwater with even more force than a fire hose.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "相手に　狙いを　定めると\n消防車の　ホースより\n強い　勢いで　水を　出す。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "一旦锁定了目标，\n它会以超越了消防\n水枪的力道来喷水。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "あいてに　ねらいを　さだめると\nしょうぼうしゃの　ホースより\nつよい　いきおいで　みずを　だす。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "상대를 겨냥한 다음\n소방차의 호스보다\n강한 기세로 물을 뿜는다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "在鎖定了目標之後，\n會用比消防車的水龍\n更強的力道來射出水柱。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Une fois sa cible dans sa ligne de mire,\nil projette des jets d’eau plus puissants\nqu’une lance à incendie.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Nachdem es einen Gegner anvisiert hat, greift\nes mit einem Wasserstrahl an, dessen Druck\nhöher ist als der eines Feuerwehrschlauchs.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Tras fijar el blanco, ataca disparando un chorro\nde agua a una presión mayor que la manguera\nde un bombero.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Dopo aver preso la mira colpisce il nemico con\ngetti d’acqua più potenti di quelli di un idrante.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Once it takes aim at its enemy, it blasts out\nwater with even more force than a fire hose.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "相手に　狙いを　定めると\n消防車の　ホースより\n強い　勢いで　水を　出す。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "一旦锁定了目标，\n它会以超越了消防\n水枪的力道来喷水。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "からだが　おもたく　のしかかって\nあいてを　きぜつさせる。\nピンチの　ときは　カラに　かくれる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "무거운 몸으로 상대를\n덮쳐서 기절시킨다.\n위기에 처하면 등껍질에 숨는다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "會用重量驚人的身體\n壓住對手使其昏厥。\n遇到危險時會躲進殼裡。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Il écrase ses adversaires de tout son poids\npour leur faire perdre connaissance.\nIl rentre dans sa carapace s’il se sent en danger.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Es begräbt seine Gegner mit seinem enormen\nKörpergewicht. Wenn es in einer aussichtslosen\nLage steckt, zieht es sich in seinen Panzer zurück.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Para acabar con su enemigo, lo aplasta con el\npeso de su cuerpo. En momentos de apuro, se\nesconde en el caparazón.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Mette KO gli avversari schiacciandoli sotto\nil corpo possente. Se è in difficoltà, può ritrarsi\nnella corazza.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "It crushes its foe under its heavy body to cause\nfainting. In a pinch, it will withdraw inside its shell.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "体が　重たく　のしかかって\n相手を　気絶させる。\nピンチの　ときは　殻に　隠れる。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "身体很重，压住对手后\n就能让对手昏厥。\n遇到危险时会躲进壳里。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "こうらの　ロケットほう　から\nふきだした　ジェットすいりゅうは\nぶあつい　てっぱんも　つらぬく。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "등껍질의 로켓포에서\n뿜어져 나오는 제트 수류는\n두꺼운 철판도 뚫는다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "從甲殼上的大炮裡\n放出的噴射水流\n足以貫穿厚實的鐵板。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Les canons sur sa carapace tirent des jets d’eau\ncapables de percer même de l’acier trempé.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Die Wassersalven, die es mit den Wasserdüsen\nin seinem Panzer abfeuert, durchdringen sogar\ndicke Stahlwände.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Dispara chorros de agua a través de los cañones\nde su caparazón, capaces de agujerear incluso el\nacero.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "I cannoni sul suo guscio sparano getti d’acqua\ncapaci di bucare l’acciaio.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "The rocket cannons on its shell fire jets of water\ncapable of punching holes through thick steel.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "甲羅の　ロケット砲　から\n噴き出した　ジェット水流は\nぶ厚い　鉄板も　つらぬく。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "从龟壳上的大炮里\n放出的喷射水流\n足以贯穿厚实的铁板。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        }
      ],
      "form_descriptions": [],
      "forms_switchable": True,
      "gender_rate": 1,
      "genera": [
        {
          "genus": "こうらポケモン",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          }
        },
        {
          "genus": "껍질포켓몬",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          }
        },
        {
          "genus": "甲殼寶可夢",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          }
        },
        {
          "genus": "Pokémon Carapace",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          }
        },
        {
          "genus": "Panzertier-Pokémon",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        },
        {
          "genus": "Pokémon Armazón",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          }
        },
        {
          "genus": "Pokémon Crostaceo",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          }
        },
        {
          "genus": "Shellfish Pokémon",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        },
        {
          "genus": "こうらポケモン",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          }
        },
        {
          "genus": "甲壳宝可梦",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          }
        }
      ],
      "generation": {
        "name": "generation-i",
        "url": "https://pokeapi.co/api/v2/generation/1/"
      },
      "growth_rate": {
        "name": "medium-slow",
        "url": "https://pokeapi.co/api/v2/growth-rate/4/"
      },
      "habitat": {
        "name": "waters-edge",
        "url": "https://pokeapi.co/api/v2/pokemon-habitat/9/"
      },
      "has_gender_differences": False,
      "hatch_counter": 20,
      "id": 9,
      "is_baby": False,
      "is_legendary": False,
      "is_mythical": False,
      "name": "blastoise",
      "names": [
        {
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "name": "カメックス"
        },
        {
          "language": {
            "name": "roomaji",
            "url": "https://pokeapi.co/api/v2/language/2/"
          },
          "name": "Kamex"
        },
        {
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "name": "거북왕"
        },
        {
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "name": "水箭龜"
        },
        {
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "name": "Tortank"
        },
        {
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "name": "Turtok"
        },
        {
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "name": "Blastoise"
        },
        {
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "name": "Blastoise"
        },
        {
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "name": "Blastoise"
        },
        {
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "name": "カメックス"
        },
        {
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "name": "水箭龟"
        }
      ],
      "order": 9,
      "pal_park_encounters": [
        {
          "area": {
            "name": "pond",
            "url": "https://pokeapi.co/api/v2/pal-park-area/4/"
          },
          "base_score": 90,
          "rate": 3
        }
      ],
      "pokedex_numbers": [
        {
          "entry_number": 9,
          "pokedex": {
            "name": "national",
            "url": "https://pokeapi.co/api/v2/pokedex/1/"
          }
        },
        {
          "entry_number": 9,
          "pokedex": {
            "name": "kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/2/"
          }
        },
        {
          "entry_number": 234,
          "pokedex": {
            "name": "original-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/3/"
          }
        },
        {
          "entry_number": 239,
          "pokedex": {
            "name": "updated-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/7/"
          }
        },
        {
          "entry_number": 88,
          "pokedex": {
            "name": "kalos-central",
            "url": "https://pokeapi.co/api/v2/pokedex/12/"
          }
        },
        {
          "entry_number": 9,
          "pokedex": {
            "name": "letsgo-kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/26/"
          }
        },
        {
          "entry_number": 73,
          "pokedex": {
            "name": "isle-of-armor",
            "url": "https://pokeapi.co/api/v2/pokedex/28/"
          }
        },
        {
          "entry_number": 172,
          "pokedex": {
            "name": "blueberry",
            "url": "https://pokeapi.co/api/v2/pokedex/33/"
          }
        }
      ],
      "shape": {
        "name": "upright",
        "url": "https://pokeapi.co/api/v2/pokemon-shape/6/"
      },
      "varieties": [
        {
          "is_default": True,
          "pokemon": {
            "name": "blastoise",
            "url": "https://pokeapi.co/api/v2/pokemon/9/"
          }
        },
        {
          "is_default": False,
          "pokemon": {
            "name": "blastoise-mega",
            "url": "https://pokeapi.co/api/v2/pokemon/10036/"
          }
        },
        {
          "is_default": False,
          "pokemon": {
            "name": "blastoise-gmax",
            "url": "https://pokeapi.co/api/v2/pokemon/10197/"
          }
        }
      ]
    },
    {
      "base_happiness": 50,
      "capture_rate": 255,
      "color": {
        "name": "green",
        "url": "https://pokeapi.co/api/v2/pokemon-color/5/"
      },
      "egg_groups": [
        {
          "name": "bug",
          "url": "https://pokeapi.co/api/v2/egg-group/3/"
        }
      ],
      "evolution_chain": {
        "url": "https://pokeapi.co/api/v2/evolution-chain/4/"
      },
      "evolves_from_species": None,
      "flavor_text_entries": [
        {
          "flavor_text": "如果碰到牠頭上的觸角，\n牠就會分泌強烈的臭味\n來保護自己。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Its short feet are tipped with suction\npads that enable it to tirelessly climb\nslopes and walls.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "leafgreen",
            "url": "https://pokeapi.co/api/v2/version/11/"
          }
        },
        {
          "flavor_text": "Its short feet\nare tipped with\nsuction pads that\fenable it to\ntirelessly climb\nslopes and walls.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "red",
            "url": "https://pokeapi.co/api/v2/version/1/"
          }
        },
        {
          "flavor_text": "Its short feet\nare tipped with\nsuction pads that\fenable it to\ntirelessly climb\nslopes and walls.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "blue",
            "url": "https://pokeapi.co/api/v2/version/2/"
          }
        },
        {
          "flavor_text": "If you touch the\nfeeler on top of\nits head, it will\frelease a horrible\nstink to protect\nitself.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version/3/"
          }
        },
        {
          "flavor_text": "For protection, it\nreleases a horri­\nble stench from\fthe antenna on its\nhead to drive away\nenemies.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "gold",
            "url": "https://pokeapi.co/api/v2/version/4/"
          }
        },
        {
          "flavor_text": "Its feet have\nsuction cups\ndesigned to stick\fto any surface. It\ntenaciously climbs\ntrees to forage.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "silver",
            "url": "https://pokeapi.co/api/v2/version/5/"
          }
        },
        {
          "flavor_text": "It crawls into\nfoliage where it\ncamouflages itself\famong leaves that\nare the same color\nas its body.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version/6/"
          }
        },
        {
          "flavor_text": "CATERPIE has a voracious appetite.\nIt can devour leaves bigger than its\nbody right before your eyes.\fFrom its antenna, this POKéMON releases\na terrifically strong odor.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "ruby",
            "url": "https://pokeapi.co/api/v2/version/7/"
          }
        },
        {
          "flavor_text": "CATERPIE has a voracious appetite.\nIt can devour leaves bigger than its\nbody right before your eyes.\fFrom its antenna, this POKéMON releases\na terrifically strong odor.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sapphire",
            "url": "https://pokeapi.co/api/v2/version/8/"
          }
        },
        {
          "flavor_text": "Its voracious appetite compels it to\ndevour leaves bigger than itself without\nhesitation. It releases a terribly strong\nodor from its antennae.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version/9/"
          }
        },
        {
          "flavor_text": "It is covered with a green skin. When it\ngrows, it sheds the skin, covers itself\nwith silk, and becomes a cocoon.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "firered",
            "url": "https://pokeapi.co/api/v2/version/10/"
          }
        },
        {
          "flavor_text": "It releases a stench from its red\nantenna to repel enemies. It\ngrows by molting repeatedly.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "diamond",
            "url": "https://pokeapi.co/api/v2/version/12/"
          }
        },
        {
          "flavor_text": "It releases a stench from its red\nantenna to repel enemies. It\ngrows by molting repeatedly.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "pearl",
            "url": "https://pokeapi.co/api/v2/version/13/"
          }
        },
        {
          "flavor_text": "It releases a stench from its red\nantenna to repel enemies. It\ngrows by molting repeatedly.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version/14/"
          }
        },
        {
          "flavor_text": "For protection, it releases a horrible\nstench from the antennae on its\nhead to drive away enemies.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "heartgold",
            "url": "https://pokeapi.co/api/v2/version/15/"
          }
        },
        {
          "flavor_text": "Its feet have suction cups\ndesigned to stick to any surface. It\ntenaciously climbs trees to forage.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "soulsilver",
            "url": "https://pokeapi.co/api/v2/version/16/"
          }
        },
        {
          "flavor_text": "Ses antennes rouges libèrent une\npuanteur qui repousse l’ennemi.\nIl grandit par mues régulières.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "It releases a stench from its red\nantenna to repel enemies. It\ngrows by molting repeatedly.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "Ses antennes rouges libèrent une\npuanteur qui repousse l’ennemi.\nIl grandit par mues régulières.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "It releases a stench from its red\nantenna to repel enemies. It\ngrows by molting repeatedly.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "It releases a stench from its red\nantenna to repel enemies. It\ngrows by molting repeatedly.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black-2",
            "url": "https://pokeapi.co/api/v2/version/21/"
          }
        },
        {
          "flavor_text": "It releases a stench from its red\nantenna to repel enemies. It\ngrows by molting repeatedly.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white-2",
            "url": "https://pokeapi.co/api/v2/version/22/"
          }
        },
        {
          "flavor_text": "あたまの　しょっかく　から\nきょうれつな　においを　だして\nてきを　おいはらい　みをまもる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "머리의 더듬이로부터\n강렬한 냄새를 내어\n적을 물리치고 몸을 보호한다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Pour se protéger, il émet un gaz puant par ses\nantennes, qui fait fuir ses ennemis audacieux.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Als Schutz vor Feinden sondert es einen übel\nriechenden Gestank mit seinen Antennen ab.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Para protegerse despide un hedor horrible de sus\nantenas, con el que repele a sus enemigos.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Per proteggersi emette un puzzo terribile\ndall’antenna sul capo, tenendo lontani i nemici.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "For protection, it releases a horrible stench from\nthe antennae on its head to drive away enemies.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "頭の　触覚から\n強烈な　においを　出して\n敵を　追い払い　身を守る。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "あしの　さきは　どんなところにも\nすいつく　きゅうばん。ひっしに\nきのぼりをして　はっぱを　たべる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "발끝에는 어디든지\n달라붙는 빨판이 있다. 필사적으로\n나무 타기를 해서 나뭇잎을 먹는다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Ses pattes ont des ventouses lui permettant de\ngrimper sur toute surface, notamment les arbres.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Die Saugnäpfe an den Beinen haften auf jedem\nUntergrund. Es sucht hartnäckig in Bäumen\nnach Futter.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Sus patas tienen ventosas con las que se adhiere a\ncualquier sitio. Escala árboles buscando forraje.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Le sue zampe hanno ventose che possono aderire\na ogni superficie. Sale sugli alberi cercando cibo.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Its feet have suction cups designed to stick to any\nsurface. It tenaciously climbs trees to forage.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "足の　先は　どんなところにも\n吸いつく　吸盤。必死に\n木登りをして　葉っぱを　食べる。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "からだ　よりも　おおきな　はっぱを　みるみる\nたべつくして　しまうほどの　しょくよくを　もつ。\nしょっかくから　きょうれつな　においを　だすぞ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "몸보다 커다란 잎사귀를 순식간에\n먹어치울 정도의 식욕을 지녔다.\n더듬이로 강렬한 냄새를 피운다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Chenipan a un appétit d’ogre. Il peut engloutir des feuilles\nplus grosses que lui. Les antennes de ce Pokémon dégagent\nune odeur particulièrement entêtante.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Raupy ist sehr gefräßig, es kann Blätter verschlingen,\ndie größer sind als es selbst. Seine Antennen sondern\neinen übel riechenden Gestank ab.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Caterpie tiene un apetito voraz. Es capaz de devorar hojas\nque superen su tamaño en un abrir y cerrar de ojos.\nAtención a la antena que tiene: libera un hedor realmente\nfuerte.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Caterpie mangia voracemente. È in grado di divorare foglie\npiù grandi del suo stesso corpo in pochi istanti.\nQuesto Pokémon emette un odore terrificante dalle antenne.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Caterpie has a voracious appetite. It can devour leaves bigger\nthan its body right before your eyes. From its antenna, this\nPokémon releases a terrifically strong odor.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "体　よりも　大きな　葉っぱを　みるみる\n食べつくして　しまうほどの　食欲を　もつ。\n触角から　強烈な　臭いを　出すぞ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "からだ　よりも　おおきな　はっぱを　みるみる\nたべつくして　しまうほどの　しょくよくを　もつ。\nしょっかくから　きょうれつな　においを　だすぞ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "몸보다 커다란 잎사귀를 순식간에\n먹어치울 정도의 식욕을 지녔다.\n더듬이로 강렬한 냄새를 피운다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Chenipan a un appétit d’ogre. Il peut engloutir des feuilles\nplus grosses que lui. Les antennes de ce Pokémon dégagent\nune odeur particulièrement entêtante.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Raupy ist sehr gefräßig. Es kann Blätter verschlingen,\ndie seine eigene Größe um ein Vielfaches übersteigen.\nSeine Antennen sondern einen übel riechenden Gestank ab.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Caterpie tiene un apetito voraz. Es capaz de devorar hojas\nque superen su tamaño en un abrir y cerrar de ojos.\nAtención a la antena que tiene: libera un hedor realmente\nfuerte.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Caterpie mangia voracemente. È in grado di divorare foglie\npiù grandi del suo stesso corpo in pochi istanti.\nQuesto Pokémon emette un odore terrificante dalle antenne.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Caterpie has a voracious appetite. It can devour leaves\nbigger than its body right before your eyes. From its antenna,\nthis Pokémon releases a terrifically strong odor.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "体　よりも　大きな　葉っぱを　みるみる\n食べつくして　しまうほどの　食欲を　もつ。\n触角から　強烈な　臭いを　出すぞ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "とりポケモンに　おそわれると　ツノから\nにおいを　だして　ていこう　するが\nえじきに　なることも　おおい。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "새포켓몬에게 습격당하면 뿔에서\n냄새를 뿜어 저항하지만\n먹이가 되는 일도 많다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "被鳥寶可夢襲擊時，\n會從觸角釋放出臭氣抵抗，\n但還是經常淪為獵物。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "Lorsqu’il est attaqué par un Pokémon Vol,\nil utilise ses antennes pour dégager une odeur\nnauséabonde, mais cela le sauve rarement.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "Es versucht, angreifende Vogel-Pokémon mit\ndem Gestank aus seinen Antennen in die Flucht\nzu schlagen. Das gelingt ihm aber nicht immer.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "A menudo resulta presa de Pokémon pájaro,\nfrente a los que su única defensa es el hedor\nrepulsivo que libera por su antena.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "Tenta di difendersi dai Pokémon alati\nemettendo un forte fetore dalle antenne,\nma cade spesso vittima dei loro attacchi.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "When attacked by bird Pokémon, it resists by\nreleasing a terrifically strong odor from its\nantennae, but it often becomes their prey.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "とりポケモンに　襲われると　ツノから\n臭いを　だして　抵抗　するが\n餌食に　なることも　多い。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "被鸟宝可梦袭击时\n会从触角中释放出臭气抵抗，\n但也经常会成为鸟食。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "つかまえやすく　せいちょうも　はやい。\nしんまいトレーナーの　パートナーに\nおススメの　ポケモンの　いっぴき。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "잡기 쉽고 성장도 빠르다.\n새내기 트레이너의 파트너로\n추천하는 포켓몬 중 한 마리.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "易於捕捉，成長速度亦快。\n是推薦給新手訓練家\n作為同伴的寶可夢之一。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "Un Pokémon facile à attraper et qui croît\nrapidement. C’est l’un des partenaires\nprivilégiés des Dresseurs débutants.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "Es eignet sich bestens für frischgebackene\nTrainer, da es sich leicht fangen lässt und\nsich sehr schnell entwickelt.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "Se desarrolla rápidamente y es fácil de atrapar.\nEs el compañero ideal para Entrenadores menos\nexperimentados.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "È facile da catturare e cresce in fretta.\nÈ uno dei Pokémon più indicati per gli Allenatori\nin erba.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "It’s easy to catch, and it grows quickly, making\nit one of the top recommendations for novice\nPokémon Trainers.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "捕まえやすく　成長も　早い。\n新米トレーナーの　パートナーに\nおススメの　ポケモンの　一匹。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "易于捕捉，成长也快。\n是推荐给新手训练家\n作为同伴的宝可梦之一。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "はやく　せいちょう　したいのか\nしょくよくおうせいで　１にちに\n１００まいの　はっぱを　くらう。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "빨리 성장하고 싶어서인지\n식욕이 왕성하여 하루에\n100장의 잎사귀를 먹는다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "或許是為了讓自己快點成長，\n牠的食慾非常旺盛，\n每天要吃掉１００片樹葉。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "C’est peut-être parce qu’il a envie de grandir\nle plus vite possible qu’il est si vorace.\nIl engloutit une centaine de feuilles par jour.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "Das nimmersatte Raupy verschlingt 100 Blätter\nam Tag. Vermutlich strebt es so ein schnelleres\nWachstum an.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "Muestra un apetito voraz, debido quizás a sus\nganas de acelerar su desarrollo. Puede llegar a\ndevorar un centenar de hojas al día.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "Mangia 100 foglie al giorno. La sua voracità\npotrebbe essere dovuta al desiderio di crescere\nin fretta.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "Perhaps because it would like to grow up\nquickly, it has a voracious appetite, eating\na hundred leaves a day.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "早く　成長　したいのか\n食欲旺盛で　１日に\n１００枚の　葉っぱを　食らう。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "或许是想要尽快长大，\n它的食欲非常旺盛，\n每天能吃掉１００片叶子。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "からだは　やわらかく　ちからもない。\nしぜんかいでは　つねに　エサとして\nねらわれ　つづける　うんめい。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "몸은 부드럽고 힘도 없다.\n자연계에서는 항상 먹이로\n노려지게 될 운명이다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "身體柔軟，又沒什麼力氣。\n在自然界，牠的命運就是\n不斷被當成獵物來捕食。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "Son corps est mou et sans force.\nLa nature semble l’avoir destiné à servir\nde proie aux autres Pokémon.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "Sein weicher und schwacher Körper ist ein\nallseits beliebtes Futter. Es muss sich daher\nstets vor Angreifern in Acht nehmen.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "Su cuerpo es blando y carente de fuerza. Parece\nque la naturaleza lo hubiera destinado a servir\nde sustento a otros Pokémon.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "Il suo corpo è molle e privo di forza.\nMolto spesso il suo destino in natura è\ndi cadere preda di altri Pokémon.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "Its body is soft and weak. In nature, its\nperpetual fate is to be seen by others as food.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "身体は　柔らかく　力もない。\n自然界では　常に　エサとして\n狙われ　続ける　運命。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "身体软绵绵的，也没什么力气。\n在自然界，它的命运就是作为\n猎物而被不断捕食。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "あたまの　さきにある　しょっかくに\nふれると　きょうれつな　においを\nだして　みを　まもろうとする。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "머리끝에 있는 더듬이를\n건드리면 강렬한 냄새를 내서\n몸을 보호하려 한다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "如果碰到牠頭上的觸角，\n牠就會分泌強烈的臭味\n來保護自己。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Quand on touche l’appendice sur son front,\nil sécrète une odeur nauséabonde pour se\nprotéger.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Berührt man die Fühler auf seinem Kopf,\nso versucht es sich zu schützen, indem es\neinen penetranten Geruch absondert.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Cuando le tocan la antena roja que tiene en la\nfrente, se defiende desprendiendo un hedor\nnauseabundo.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Se gli si toccano le antenne che ha sulla testa,\nsi difende emettendo un odore insopportabile.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "If you touch the feeler on top of its head, it will\nrelease a horrible stink to protect itself.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "頭の　先にある　触角に\nふれると　強烈な　においを\n出して　身を　守ろうとする。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "如果你碰到了它头上的\n触角，它就会分泌出\n难闻的气味来保护自己。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "あたまの　さきにある　しょっかくに\nふれると　きょうれつな　においを\nだして　みを　まもろうとする。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "머리끝에 있는 더듬이를\n건드리면 강렬한 냄새를 내서\n몸을 보호하려 한다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Quand on touche l’appendice sur son front,\nil sécrète une odeur nauséabonde pour se\nprotéger.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Berührt man die Fühler auf seinem Kopf,\nso versucht es sich zu schützen, indem es\neinen penetranten Geruch absondert.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Cuando le tocan la antena roja que tiene en la\nfrente, se defiende desprendiendo un hedor\nnauseabundo.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Se gli si toccano le antenne che ha sulla testa,\nsi difende emettendo un odore insopportabile.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "If you touch the feeler on top of its head, it will\nrelease a horrible stink to protect itself.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "頭の　先にある　触角に\nふれると　強烈な　においを\n出して　身を　守ろうとする。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "如果你碰到了它头上的\n触角，它就会分泌出\n难闻的气味来保护自己。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "あたまの　しょっかくから\nきょうれつな　においを　だして\nてきを　おいはらい　みをまもる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "머리의 더듬이로부터\n강렬한 냄새를 내어\n적을 물리치고 몸을 보호한다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "會從頭部的觸角釋放出\n強烈的氣味來趕走敵人，\n藉此保護自己。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Pour se protéger, il émet par ses antennes\nune odeur nauséabonde qui fait fuir ses ennemis.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Als Schutz vor Feinden sondert es einen übel\nriechenden Gestank mit seinen Antennen ab.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Para protegerse, despide un hedor horrible por\nlas antenas con el que repele a sus enemigos.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Per proteggersi emette un puzzo terribile dalle\nantenne sul capo, con cui tiene lontani i nemici.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "For protection, it releases a horrible stench from\nthe antenna on its head to drive away enemies.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "頭の　触角から\n強烈な　においを　だして\n敵を　追いはらい　身を守る。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "会从头部的触角中\n释放出强烈的臭气，\n以此来赶走敌人保护自己。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "あしは　みじかいが　きゅうばんに\nなっているので　さかでも　かべでも\nくたびれることなく　すすんでいく。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "다리는 짧지만 빨판으로\n되어 있어 비탈길이나 벽에서도\n지치지 않고 나아간다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "別看牠的腳很短，\n因為是吸盤，所以無論是\n斜坡還是牆壁都能輕鬆前進。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Ses petites pattes munies de ventouses\nlui permettent de monter les pentes\net de grimper aux murs sans se fatiguer.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Es hat Saugnäpfe an den Beinchen, mit denen es\nmühelos Steigungen und Mauern erklimmen kann.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Sus cortas patas están recubiertas de ventosas\nque le permiten subir incansable por muros y\ncuestas.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Le ventose sulle sue corte zampe gli permettono\ndi affrontare ogni salita e di scalare senza fatica\nqualsiasi muro.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Its short feet are tipped with suction pads that\nenable it to tirelessly climb slopes and walls.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "脚は　短いが　吸盤に\nなっているので　坂でも　壁でも\nくたびれることなく　進んでいく。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "别看它的脚很短，\n因为是吸盘，所以无论是\n斜坡还是墙壁都能轻松前进。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        }
      ],
      "form_descriptions": [],
      "forms_switchable": False,
      "gender_rate": 4,
      "genera": [
        {
          "genus": "いもむしポケモン",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          }
        },
        {
          "genus": "애벌레포켓몬",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          }
        },
        {
          "genus": "蟲寶寶寶可夢",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          }
        },
        {
          "genus": "Pokémon Ver",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          }
        },
        {
          "genus": "Wurm-Pokémon",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        },
        {
          "genus": "Pokémon Gusano",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          }
        },
        {
          "genus": "Pokémon Baco",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          }
        },
        {
          "genus": "Worm Pokémon",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        },
        {
          "genus": "いもむしポケモン",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          }
        },
        {
          "genus": "虫宝宝宝可梦",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          }
        }
      ],
      "generation": {
        "name": "generation-i",
        "url": "https://pokeapi.co/api/v2/generation/1/"
      },
      "growth_rate": {
        "name": "medium",
        "url": "https://pokeapi.co/api/v2/growth-rate/2/"
      },
      "habitat": {
        "name": "forest",
        "url": "https://pokeapi.co/api/v2/pokemon-habitat/2/"
      },
      "has_gender_differences": False,
      "hatch_counter": 15,
      "id": 10,
      "is_baby": False,
      "is_legendary": False,
      "is_mythical": False,
      "name": "caterpie",
      "names": [
        {
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "name": "キャタピー"
        },
        {
          "language": {
            "name": "roomaji",
            "url": "https://pokeapi.co/api/v2/language/2/"
          },
          "name": "Caterpie"
        },
        {
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "name": "캐터피"
        },
        {
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "name": "綠毛蟲"
        },
        {
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "name": "Chenipan"
        },
        {
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "name": "Raupy"
        },
        {
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "name": "Caterpie"
        },
        {
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "name": "Caterpie"
        },
        {
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "name": "Caterpie"
        },
        {
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "name": "キャタピー"
        },
        {
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "name": "绿毛虫"
        }
      ],
      "order": 10,
      "pal_park_encounters": [
        {
          "area": {
            "name": "forest",
            "url": "https://pokeapi.co/api/v2/pal-park-area/1/"
          },
          "base_score": 30,
          "rate": 50
        }
      ],
      "pokedex_numbers": [
        {
          "entry_number": 10,
          "pokedex": {
            "name": "national",
            "url": "https://pokeapi.co/api/v2/pokedex/1/"
          }
        },
        {
          "entry_number": 10,
          "pokedex": {
            "name": "kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/2/"
          }
        },
        {
          "entry_number": 24,
          "pokedex": {
            "name": "original-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/3/"
          }
        },
        {
          "entry_number": 24,
          "pokedex": {
            "name": "updated-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/7/"
          }
        },
        {
          "entry_number": 23,
          "pokedex": {
            "name": "kalos-central",
            "url": "https://pokeapi.co/api/v2/pokedex/12/"
          }
        },
        {
          "entry_number": 17,
          "pokedex": {
            "name": "original-alola",
            "url": "https://pokeapi.co/api/v2/pokedex/16/"
          }
        },
        {
          "entry_number": 17,
          "pokedex": {
            "name": "original-melemele",
            "url": "https://pokeapi.co/api/v2/pokedex/17/"
          }
        },
        {
          "entry_number": 8,
          "pokedex": {
            "name": "original-akala",
            "url": "https://pokeapi.co/api/v2/pokedex/18/"
          }
        },
        {
          "entry_number": 17,
          "pokedex": {
            "name": "updated-alola",
            "url": "https://pokeapi.co/api/v2/pokedex/21/"
          }
        },
        {
          "entry_number": 17,
          "pokedex": {
            "name": "updated-melemele",
            "url": "https://pokeapi.co/api/v2/pokedex/22/"
          }
        },
        {
          "entry_number": 8,
          "pokedex": {
            "name": "updated-akala",
            "url": "https://pokeapi.co/api/v2/pokedex/23/"
          }
        },
        {
          "entry_number": 10,
          "pokedex": {
            "name": "letsgo-kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/26/"
          }
        },
        {
          "entry_number": 13,
          "pokedex": {
            "name": "galar",
            "url": "https://pokeapi.co/api/v2/pokedex/27/"
          }
        }
      ],
      "shape": {
        "name": "armor",
        "url": "https://pokeapi.co/api/v2/pokemon-shape/14/"
      },
      "varieties": [
        {
          "is_default": True,
          "pokemon": {
            "name": "caterpie",
            "url": "https://pokeapi.co/api/v2/pokemon/10/"
          }
        }
      ]
    },
    {
      "base_happiness": 50,
      "capture_rate": 120,
      "color": {
        "name": "green",
        "url": "https://pokeapi.co/api/v2/pokemon-color/5/"
      },
      "egg_groups": [
        {
          "name": "bug",
          "url": "https://pokeapi.co/api/v2/egg-group/3/"
        }
      ],
      "evolution_chain": {
        "url": "https://pokeapi.co/api/v2/evolution-chain/4/"
      },
      "evolves_from_species": {
        "name": "caterpie",
        "url": "https://pokeapi.co/api/v2/pokemon-species/10/"
      },
      "flavor_text_entries": [
        {
          "flavor_text": "This POKéMON is\nvulnerable to\nattack while its\fshell is soft,\nexposing its weak\nand tender body.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "red",
            "url": "https://pokeapi.co/api/v2/version/1/"
          }
        },
        {
          "flavor_text": "This POKéMON is\nvulnerable to\nattack while its\fshell is soft,\nexposing its weak\nand tender body.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "blue",
            "url": "https://pokeapi.co/api/v2/version/2/"
          }
        },
        {
          "flavor_text": "Hardens its shell\nto protect itself.\nHowever, a large\fimpact may cause\nit to pop out of\nits shell.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version/3/"
          }
        },
        {
          "flavor_text": "Inside the shell,\nit is soft and\nweak as it pre­\fpares to evolve.\nIt stays motion­\nless in the shell.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "gold",
            "url": "https://pokeapi.co/api/v2/version/4/"
          }
        },
        {
          "flavor_text": "It prepares for\nevolution by har­\ndening its shell\fas much as possi­\nble to protect its\nsoft body.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "silver",
            "url": "https://pokeapi.co/api/v2/version/5/"
          }
        },
        {
          "flavor_text": "This is its pre-\nevolved form. At\nthis stage, it can\fonly harden, so it\nremains motionless\nto avoid attack.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version/6/"
          }
        },
        {
          "flavor_text": "The shell covering this POKéMON’s body\nis as hard as an iron slab.\nMETAPOD does not move very much.\fIt stays still because it is preparing\nits soft innards for evolution inside\nthe hard shell.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "ruby",
            "url": "https://pokeapi.co/api/v2/version/7/"
          }
        },
        {
          "flavor_text": "The shell covering this POKéMON’s body\nis as hard as an iron slab.\nMETAPOD does not move very much.\fIt stays still because it is preparing\nits soft innards for evolution inside\nthe hard shell.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sapphire",
            "url": "https://pokeapi.co/api/v2/version/8/"
          }
        },
        {
          "flavor_text": "Its shell is as hard as an iron slab.\nA METAPOD does not move very much\nbecause it is preparing its soft innards\nfor evolution inside the shell.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version/9/"
          }
        },
        {
          "flavor_text": "Even though it is encased in a sturdy\nshell, the body inside is tender.\nIt can’t withstand a harsh attack.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "firered",
            "url": "https://pokeapi.co/api/v2/version/10/"
          }
        },
        {
          "flavor_text": "This POKéMON is vulnerable to attack\nwhile its shell is soft, exposing its weak\nand tender body.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "leafgreen",
            "url": "https://pokeapi.co/api/v2/version/11/"
          }
        },
        {
          "flavor_text": "A steel-hard shell protects its\ntender body. It quietly endures\nhardships while awaiting evolution.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "diamond",
            "url": "https://pokeapi.co/api/v2/version/12/"
          }
        },
        {
          "flavor_text": "A steel-hard shell protects its\ntender body. It quietly endures\nhardships while awaiting evolution.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "pearl",
            "url": "https://pokeapi.co/api/v2/version/13/"
          }
        },
        {
          "flavor_text": "A steel-hard shell protects its\ntender body. It quietly endures\nhardships while awaiting evolution.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version/14/"
          }
        },
        {
          "flavor_text": "Inside the shell, it is soft and\nweak as it prepares to evolve.\nIt stays motionless in the shell.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "heartgold",
            "url": "https://pokeapi.co/api/v2/version/15/"
          }
        },
        {
          "flavor_text": "It prepares for evolution by hardening\nits shell as much as possible\nto protect its soft body.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "soulsilver",
            "url": "https://pokeapi.co/api/v2/version/16/"
          }
        },
        {
          "flavor_text": "Son corps frêle est protégé par sa\ncarapace d’acier. Il encaisse les\ncoups durs en attendant d’évoluer.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "A steel-hard shell protects its\ntender body. It quietly endures\nhardships while awaiting evolution.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "Son corps frêle est protégé par sa\ncarapace d’acier. Il encaisse les\ncoups durs en attendant d’évoluer.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "A steel-hard shell protects its\ntender body. It quietly endures\nhardships while awaiting evolution.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "A steel-hard shell protects its\ntender body. It quietly endures\nhardships while awaiting evolution.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black-2",
            "url": "https://pokeapi.co/api/v2/version/21/"
          }
        },
        {
          "flavor_text": "A steel-hard shell protects its\ntender body. It quietly endures\nhardships while awaiting evolution.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white-2",
            "url": "https://pokeapi.co/api/v2/version/22/"
          }
        },
        {
          "flavor_text": "こうてつのように　かたい　カラで\nやわらかい　なかみを　まもっている。\nしんかするまで　じっと　たえている。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "강철같이 단단한 껍질로\n부드러운 몸을 보호하고 있다.\n진화할 때까지 가만히 참고 있다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Son corps frêle est protégé par sa carapace d’acier.\nIl encaisse les coups durs en attendant d’évoluer.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Der stahlharte Panzer schützt seinen zarten Körper.\nEs wartet geduldig auf seine Entwicklung.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Su frágil cuerpo está recubierto de una coraza dura\ncomo el acero. Permanece quieto en su desarrollo.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Ha una corazza dura come l’acciaio che protegge\nil suo fragile corpo. Attende immobile di evolversi.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "A steel-hard shell protects its tender body.\nIt quietly endures hardships while\nawaiting evolution.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "鋼鉄のように　硬い　殻で\nやわらかい　中身を　守っている。\n進化するまで　じっと　耐えている。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "カラが　かたくなるまえに\nつよい　しょうげきを　うけると\nなかみが　でてしまうので　ちゅうい。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "껍질이 단단해지기 전에\n강한 충격을 받으면\n속이 나와버리니 주의.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Il est vulnérable aux attaques tant que sa carapace\nest molle, car il expose son corps tendre et mou.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Während der Panzer dieses Pokémon sehr weich ist,\nbietet er keinen großen Schutz vor Attacken.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Este Pokémon es vulnerable al ataque cuando su\ncoraza es blanda y no lo protege del todo.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Quando la sua corazza è morbida, il corpo fragile di\nquesto Pokémon è più vulnerabile agli attacchi.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "This Pokémon is vulnerable to attack while its shell\nis soft, exposing its weak and tender body.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "殻が　硬くなる前に\n強い　衝撃を　受けると\n中身が　出てしまうので　注意。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "からだの　カラは　てっぱんの　ように　かたい。\nあまり　うごかないのは　カラのなかで　やわらかい\nなかみが　しんかの　じゅんびを　しているからだ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "몸의 껍질은 철판처럼 단단하다.\n움직임이 적은 것은 껍질 안에서 부드러운\n몸이 진화 준비를 하고 있어서다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "La carapace protégeant ce Pokémon est dure comme du\nmétal. Chrysacier ne bouge pas beaucoup. Il reste immobile\npour préparer les organes à l’intérieur de sa carapace en vue\nd’une évolution future.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Der Panzer dieses Pokémon ist hart wie Stahl. Safcon bewegt\nsich kaum, da es das weiche Innere unter seiner harten Schale\nauf seine Entwicklung vorbereitet.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "La capa que recubre el cuerpo de este Pokémon es tan dura\ncomo una plancha de hierro. Metapod apenas se mueve.\nPermanece inmóvil para que las vísceras evolucionen dentro\nde la coraza que le rodea.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "La corazza di questo Pokémon è dura come una lastra\ndi ferro. Metapod non si muove molto. Sta immobile per\npreparare il morbido interno della dura corazza all’evoluzione.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "The shell covering this Pokémon’s body is as hard as an\niron slab. Metapod does not move very much. It stays still\nbecause it is preparing its soft innards for evolution inside\nthe hard shell.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "体の　カラは　鉄板の　ように　硬い。\nあまり　動かないのは　カラの中で　柔らかい\n中身が　進化の　準備を　しているからだ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "からだの　カラは　てっぱんの　ように　かたい。\nあまり　うごかないのは　カラのなかで　やわらかい\nなかみが　しんかの　じゅんびを　しているからだ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "몸의 껍질은 철판처럼 단단하다.\n움직임이 적은 것은 껍질 안에서 부드러운\n몸이 진화 준비를 하고 있어서다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "La carapace protégeant ce Pokémon est dure comme du\nmétal. Chrysacier ne bouge pas beaucoup. Il reste immobile\npour préparer les organes à l’intérieur de sa carapace en vue\nd’une évolution future.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Der Panzer dieses Pokémon ist hart wie Stahl. Safcon bewegt\nsich kaum, da es das weiche Innere unter seiner harten Schale\nauf seine Entwicklung vorbereitet.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "La capa que recubre el cuerpo de este Pokémon es tan dura\ncomo una plancha de hierro. Metapod apenas se mueve.\nPermanece inmóvil para que las vísceras evolucionen dentro\nde la coraza que le rodea.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "La corazza di questo Pokémon è dura come una lastra\ndi ferro. Metapod non si muove molto. Sta immobile per\npreparare il morbido interno della dura corazza all’evoluzione.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "The shell covering this Pokémon’s body is as hard as an\niron slab. Metapod does not move very much.\nIt stays still because it is preparing its soft innards for\nevolution inside the hard shell.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "体の　カラは　鉄板の　ように　硬い。\nあまり　動かないのは　カラの中で　柔らかい\n中身が　進化の　準備を　しているからだ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "カラのなかには　トロトロの　なかみが\nつまっている。　ほぼ　うごかないのは\nウッカリ　なかみが　こぼれないため。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "껍질 안은 부드러운 내용물로 가득 차 있다.\n거의 움직이지 않는 것은 무심코\n내용물이 흘러나오게 하지 않기 위해서다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "殼中塞滿了軟綿綿的身體。\n幾乎動也不動是為了防止\n身體在不留神時露出來。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "Sous sa carapace, il est tout mou et tendre.\nIl bouge très peu afin de ne pas secouer son\ncorps encore fragile.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "Sein harter Panzer birgt ein weiches Inneres.\nUm zu vermeiden, dass dieses versehentlich\nausläuft, bewegt es sich kaum.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "La dura capa que le recubre el cuerpo protege\nsus delicadas vísceras. Metapod apenas se\nmueve para evitar que estas se desparramen.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "La corazza racchiude un corpo estremamente\nmolle e il Pokémon si muove appena per paura\nche fuoriesca accidentalmente.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "Its shell is filled with its soft innards. It doesn’t\nmove much because of the risk it might\ncarelessly spill its innards out.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "カラの中には　トロトロの　中身が\n詰まっている。　ほぼ動かないのは\nウッカリ　中身が　こぼれないため。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "壳中藏着软乎乎的身体。\n几乎不动是为了防止\n身体一不留神就露出来。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "かたいと　いっても　むしの　カラ。\nわれてしまうことも　あるので\nはげしい　たたかいは　きんもつ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "단단하다고는 해도 벌레의 껍질.\n갈라질 수도 있으므로\n격렬한 싸움은 금물이다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "雖說堅硬，但還是蟲的外殼。\n有時還是會破裂的，\n所以禁止用於激烈的戰鬥。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "Même si sa carapace est solide, elle n’est guère\ncomposée que de chitine et peut se briser\naisément. Mieux vaut éviter les combats rudes.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "Sein Panzer ist zwar hart, aber dennoch anfällig\nfür Risse, da es ein Käfer-Pokémon ist.\nFür schwere Kämpfe ist es daher ungeeignet.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "Su coraza es muy dura, pero no deja de estar\nhecha de quitina, por lo que podría quebrarse.\nEs mejor no llevarlo en combates muy intensos.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "La sua corazza è piuttosto dura per un\nPokémon Coleottero, ma potrebbe comunque\nrompersi. Meglio evitare lotte troppo veementi.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "Its shell is hard, but it’s still just a bug shell.\nIt’s been known to break, so intense battles\nwith it should be avoided.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "硬いと　いっても　虫の　殻。\n割れてしまうことも　あるので\n激しい　戦いは　禁物。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "虽说坚硬，但还是虫的外壳。\n因为有时也会破裂，\n所以禁止用于激烈的战斗。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "カラのなかは　ドロドロの　えきたい。\nしんかに　そなえて　からだじゅうの\nさいぼうを　つくりなおしている。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "껍질 안은 걸쭉한 액체다.\n진화를 대비하여 몸 전체의\n세포를 재구성하고 있다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "殼裡面是黏糊糊的液體。\n為了準備迎接進化，\n正不斷更新全身的細胞。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "Sa carapace contient un liquide gluant.\nSa structure cellulaire est en cours de\nmodification en vue de son évolution prochaine.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "Sein Panzer birgt ein dickflüssiges Inneres.\nIn Vorbereitung auf seine Entwicklung wird seine\nZellstruktur vollständig umgestaltet.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "El interior del caparazón es un líquido viscoso.\nTodas las células de su cuerpo se están\nregenerando en preparación para su evolución.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "La sua corazza contiene un liquido vischioso.\nRistruttura tutte le cellule del suo corpo\npreparandosi all’evoluzione.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "Its shell is filled with a thick liquid. All of the\ncells throughout its body are being rebuilt in\npreparation for evolution.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "カラの中は　ドロドロの　液体。\n進化に　備えて　体中の\n細胞を　作りなおしている。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "壳里面是黏糊糊的液体。\n为了准备迎接进化，\n正在不断地更新体内的细胞。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "とても　かたいカラは　ツツケラに\nつつかれても　びくともしないが\nゆれて　なかみが　こぼれてしまう。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "매우 단단한 껍질은 콕코구리가\n쪼아도 꿈쩍도 하지 않지만 흔들림에\n약해서 내용물이 흘러나와 버린다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "外殼非常堅硬，就算被\n小篤兒啄到也能平安無事，\n但殼裡的身體會因為晃動而流出來。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "Sa carapace est très solide et résiste sans\npeine aux assauts des Picassaut. Si elle bascule,\npar contre, son contenu s’éparpille au sol.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "Ein Schnabelangriff von Peppeck kann Safcons\nhartem Panzer nichts anhaben, doch wenn es\nzu schaukeln beginnt, läuft sein Inneres aus.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "Su dura coraza resiste los picotazos de un\nPikipek, pero, si se agita mucho, su contenido\npuede verterse por el suelo.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "La sua dura corazza resiste anche alle beccate\ndei Pikipek ma, se oscilla troppo, il contenuto\npuò fuoriuscire.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "Its hard shell doesn’t crack a bit even if Pikipek\npecks at it, but it will tip over, spilling out\nits insides.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "とても　硬いカラは　ツツケラに\n突かれても　びくともしないが\n揺れて　中身が　こぼれてしまう。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "外壳非常坚硬，即使受到\n小笃儿的啄击也能安然无恙，\n但壳里的身体会因晃动而流出来。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "みをまもるため　ひたすら　カラを\nかたくしても　つよい　しょうげきを\nうけると　なかみが　でてしまう。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "몸을 보호하기 위해 끊임없이\n껍질을 단단하게 하지만 강한 충격을\n받으면 내용물이 나와버린다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "靠著堅硬無比的外殼來保護自己。\n然而一旦遭受到強烈衝擊，\n殼裡的身體就會跑出來。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Il renforce sa carapace pour se protéger,\nmais un coup puissant peut l’en déloger.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Um sich zu schützen, härtet es eifrig seinen\nPanzer, doch wenn es heftige Treffer einsteckt,\nwird sein Inneres entblößt.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Pese a su constante empeño por endurecer su\ncoraza para protegerse, puede romperse si\nrecibe un fuerte impacto y quedar expuesto.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Per difendersi indurisce la corazza, ma un colpo\nviolento può scaraventarlo fuori dal guscio.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Hardens its shell to protect itself. However, a\nlarge impact may cause it to pop out of its shell.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "身を守るため　ひたすら　カラを\n硬くしても　強い　衝撃を\n受けると　中身が　出てしまう。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "它会让外壳变硬来保护自己。\n然而在遇到强烈的冲击力时，\n它的身体还是会被撞出来。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "みをまもるため　ひたすら　カラを\nかたくしても　つよい　しょうげきを\nうけると　なかみが　でてしまう。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "몸을 보호하기 위해 끊임없이\n껍질을 단단하게 하지만 강한 충격을\n받으면 내용물이 나와버린다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "靠著堅硬無比的外殼來保護自己。\n然而一旦遭受到強烈衝擊，\n殼裡的身體就會跑出來。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Il renforce sa carapace pour se protéger,\nmais un coup puissant peut l’en déloger.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Um sich zu schützen, härtet es eifrig seinen\nPanzer, doch wenn es heftige Treffer einsteckt,\nwird sein Inneres entblößt.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Pese a su constante empeño por endurecer su\ncoraza para protegerse, puede romperse si\nrecibe un fuerte impacto y quedar expuesto.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Per difendersi indurisce la corazza, ma un colpo\nviolento può scaraventarlo fuori dal guscio.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Hardens its shell to protect itself. However, a\nlarge impact may cause it to pop out of its shell.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "身を守るため　ひたすら　カラを\n硬くしても　強い　衝撃を\n受けると　中身が　出てしまう。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "它会让外壳变硬来保护自己。\n然而在遇到强烈的冲击力时，\n它的身体还是会被撞出来。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "しんかを　まっている　じょうたい。\nかたくなる　ことしか　できないので\nおそわれないよう　じっとしている。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "진화를 기다리고 있는 상태다.\n단단해지는 것밖에 할 수 없어서\n공격받지 않도록 꿈쩍 않고 있다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "正處於等待進化的狀態。\n除了變硬之外什麼都做不了，\n只能動也不動以免遭受攻擊。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "En attendant sa prochaine évolution, il ne peut\nque durcir sa carapace et rester immobile\npour éviter de se faire attaquer.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "In diesem Zustand wartet es auf die Entwicklung.\nEs kann nur seinen Panzer erhärten, daher bewegt\nes sich nicht, um nicht angegriffen zu werden.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Como en este estado solo puede endurecer\nsu coraza, permanece inmóvil a la espera de\nevolucionar.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "In attesa di evolversi, l’unica cosa che può fare\nè indurire la sua corazza, quindi rimane immobile\nper evitare di essere attaccato.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "It is waiting for the moment to evolve. At this\nstage, it can only harden, so it remains\nmotionless to avoid attack.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "進化を　待っている　状態。\n硬くなる　ことしか　できないので\n襲われないよう　じっとしている。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "正处于等待进化的状态。\n除了变硬之外什么都做不了，\n只能动也不动以免引来袭击。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "かたい　カラに　つつまれているが\nなかみは　やわらかいので\nつよい　こうげきには　たえられない。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "단단한 껍질로 둘러싸여 있지만\n안은 부드럽기 때문에\n강한 공격에는 버티지 못한다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "雖然有堅硬的外殼，\n但因為殼裡的身體很軟，\n所以無法抵抗強力的攻擊。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Bien que son corps soit entouré d’une carapace\nsolide, l’intérieur est si mou qu’il ne résisterait\npas à une attaque violente.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "In seiner harten Schale ist ein weicher Körper.\nEinem brutalen Angriff hat es nichts\nentgegenzusetzen.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Aunque cuenta con una coraza muy dura, tiene\nun cuerpo bastante blando. Un ataque violento\npuede acabar con él.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "La corazza esterna è robusta ma l’interno\nè molle. Per questo non è in grado di resistere\nad attacchi particolarmente veementi.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Even though it is encased in a sturdy shell,\nthe body inside is tender. It can’t withstand a\nharsh attack.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "硬い　殻に　包まれているが\n中身は　軟らかいので\n強い　攻撃には　耐えられない。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "虽然有坚硬的外壳，\n因为壳里的身体很软，\n所以无法抵抗强力的攻击。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        }
      ],
      "form_descriptions": [],
      "forms_switchable": False,
      "gender_rate": 4,
      "genera": [
        {
          "genus": "さなぎポケモン",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          }
        },
        {
          "genus": "번데기포켓몬",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          }
        },
        {
          "genus": "蛹寶可夢",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          }
        },
        {
          "genus": "Pokémon Cocon",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          }
        },
        {
          "genus": "Kokon-Pokémon",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        },
        {
          "genus": "Pokémon Capullo",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          }
        },
        {
          "genus": "Pokémon Bozzolo",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          }
        },
        {
          "genus": "Cocoon Pokémon",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        },
        {
          "genus": "さなぎポケモン",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          }
        },
        {
          "genus": "蛹宝可梦",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          }
        }
      ],
      "generation": {
        "name": "generation-i",
        "url": "https://pokeapi.co/api/v2/generation/1/"
      },
      "growth_rate": {
        "name": "medium",
        "url": "https://pokeapi.co/api/v2/growth-rate/2/"
      },
      "habitat": {
        "name": "forest",
        "url": "https://pokeapi.co/api/v2/pokemon-habitat/2/"
      },
      "has_gender_differences": False,
      "hatch_counter": 15,
      "id": 11,
      "is_baby": False,
      "is_legendary": False,
      "is_mythical": False,
      "name": "metapod",
      "names": [
        {
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "name": "トランセル"
        },
        {
          "language": {
            "name": "roomaji",
            "url": "https://pokeapi.co/api/v2/language/2/"
          },
          "name": "Trancell"
        },
        {
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "name": "단데기"
        },
        {
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "name": "鐵甲蛹"
        },
        {
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "name": "Chrysacier"
        },
        {
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "name": "Safcon"
        },
        {
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "name": "Metapod"
        },
        {
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "name": "Metapod"
        },
        {
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "name": "Metapod"
        },
        {
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "name": "トランセル"
        },
        {
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "name": "铁甲蛹"
        }
      ],
      "order": 11,
      "pal_park_encounters": [
        {
          "area": {
            "name": "forest",
            "url": "https://pokeapi.co/api/v2/pal-park-area/1/"
          },
          "base_score": 50,
          "rate": 30
        }
      ],
      "pokedex_numbers": [
        {
          "entry_number": 11,
          "pokedex": {
            "name": "national",
            "url": "https://pokeapi.co/api/v2/pokedex/1/"
          }
        },
        {
          "entry_number": 11,
          "pokedex": {
            "name": "kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/2/"
          }
        },
        {
          "entry_number": 25,
          "pokedex": {
            "name": "original-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/3/"
          }
        },
        {
          "entry_number": 25,
          "pokedex": {
            "name": "updated-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/7/"
          }
        },
        {
          "entry_number": 24,
          "pokedex": {
            "name": "kalos-central",
            "url": "https://pokeapi.co/api/v2/pokedex/12/"
          }
        },
        {
          "entry_number": 18,
          "pokedex": {
            "name": "original-alola",
            "url": "https://pokeapi.co/api/v2/pokedex/16/"
          }
        },
        {
          "entry_number": 18,
          "pokedex": {
            "name": "original-melemele",
            "url": "https://pokeapi.co/api/v2/pokedex/17/"
          }
        },
        {
          "entry_number": 9,
          "pokedex": {
            "name": "original-akala",
            "url": "https://pokeapi.co/api/v2/pokedex/18/"
          }
        },
        {
          "entry_number": 18,
          "pokedex": {
            "name": "updated-alola",
            "url": "https://pokeapi.co/api/v2/pokedex/21/"
          }
        },
        {
          "entry_number": 18,
          "pokedex": {
            "name": "updated-melemele",
            "url": "https://pokeapi.co/api/v2/pokedex/22/"
          }
        },
        {
          "entry_number": 9,
          "pokedex": {
            "name": "updated-akala",
            "url": "https://pokeapi.co/api/v2/pokedex/23/"
          }
        },
        {
          "entry_number": 11,
          "pokedex": {
            "name": "letsgo-kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/26/"
          }
        },
        {
          "entry_number": 14,
          "pokedex": {
            "name": "galar",
            "url": "https://pokeapi.co/api/v2/pokedex/27/"
          }
        }
      ],
      "shape": {
        "name": "squiggle",
        "url": "https://pokeapi.co/api/v2/pokemon-shape/2/"
      },
      "varieties": [
        {
          "is_default": True,
          "pokemon": {
            "name": "metapod",
            "url": "https://pokeapi.co/api/v2/pokemon/11/"
          }
        }
      ]
    },
    {
      "base_happiness": 50,
      "capture_rate": 45,
      "color": {
        "name": "white",
        "url": "https://pokeapi.co/api/v2/pokemon-color/9/"
      },
      "egg_groups": [
        {
          "name": "bug",
          "url": "https://pokeapi.co/api/v2/egg-group/3/"
        }
      ],
      "evolution_chain": {
        "url": "https://pokeapi.co/api/v2/evolution-chain/4/"
      },
      "evolves_from_species": {
        "name": "metapod",
        "url": "https://pokeapi.co/api/v2/pokemon-species/11/"
      },
      "flavor_text_entries": [
        {
          "flavor_text": "In battle, it\nflaps its wings\nat high speed to\frelease highly\ntoxic dust into\nthe air.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "red",
            "url": "https://pokeapi.co/api/v2/version/1/"
          }
        },
        {
          "flavor_text": "In battle, it\nflaps its wings\nat high speed to\frelease highly\ntoxic dust into\nthe air.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "blue",
            "url": "https://pokeapi.co/api/v2/version/2/"
          }
        },
        {
          "flavor_text": "Its wings, covered\nwith poisonous\npowders, repel\fwater. This\nallows it to fly\nin the rain.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version/3/"
          }
        },
        {
          "flavor_text": "It collects honey\nevery day. It rubs\nhoney onto the\fhairs on its legs\nto carry it back\nto its nest.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "gold",
            "url": "https://pokeapi.co/api/v2/version/4/"
          }
        },
        {
          "flavor_text": "Water-repellent\npowder on its\nwings enables it\fto collect honey,\neven in the heav­\niest of rains.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "silver",
            "url": "https://pokeapi.co/api/v2/version/5/"
          }
        },
        {
          "flavor_text": "It flits from\nflower to flower,\ncollecting honey.\fIt can even\nidentify distant\nflowers in bloom.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version/6/"
          }
        },
        {
          "flavor_text": "BUTTERFREE has a superior ability to\nsearch for delicious honey from\nflowers.\fIt can even search out, extract, and\ncarry honey from flowers that are\nblooming over six miles from its nest.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "ruby",
            "url": "https://pokeapi.co/api/v2/version/7/"
          }
        },
        {
          "flavor_text": "BUTTERFREE has a superior ability to\nsearch for delicious honey from\nflowers.\fIt can even search out, extract, and\ncarry honey from flowers that are\nblooming over six miles from its nest.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sapphire",
            "url": "https://pokeapi.co/api/v2/version/8/"
          }
        },
        {
          "flavor_text": "It has a superior ability to search for\ndelicious honey from flowers. It can seek,\nextract, and carry honey from flowers\nblooming over six miles away.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version/9/"
          }
        },
        {
          "flavor_text": "The wings are protected by rain-repellent\ndust. As a result, this POKéMON can fly\nabout even in rain.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "firered",
            "url": "https://pokeapi.co/api/v2/version/10/"
          }
        },
        {
          "flavor_text": "In battle, it flaps its wings at great\nspeed to release highly toxic dust into\nthe air.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "leafgreen",
            "url": "https://pokeapi.co/api/v2/version/11/"
          }
        },
        {
          "flavor_text": "It loves the honey of flowers and\ncan locate flower patches that\nhave even tiny amounts of pollen.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "diamond",
            "url": "https://pokeapi.co/api/v2/version/12/"
          }
        },
        {
          "flavor_text": "It loves the honey of flowers and\ncan locate flower patches that\nhave even tiny amounts of pollen.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "pearl",
            "url": "https://pokeapi.co/api/v2/version/13/"
          }
        },
        {
          "flavor_text": "It loves the honey of flowers and\ncan locate flower patches that\nhave even tiny amounts of pollen.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version/14/"
          }
        },
        {
          "flavor_text": "It collects honey every day. It rubs\nhoney onto the hairs on its legs\nto carry it back to its nest.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "heartgold",
            "url": "https://pokeapi.co/api/v2/version/15/"
          }
        },
        {
          "flavor_text": "Water-repellent powder on its\nwings enables it to collect honey,\neven in the heaviest of rains.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "soulsilver",
            "url": "https://pokeapi.co/api/v2/version/16/"
          }
        },
        {
          "flavor_text": "Il raffole du nectar des fleurs. Il\nest capable de repérer la plus\npetite quantité de pollen.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "It loves the honey of flowers and\ncan locate flower patches that\nhave even tiny amounts of pollen.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "Il raffole du nectar des fleurs. Il\nest capable de repérer la plus\npetite quantité de pollen.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "It loves the honey of flowers and\ncan locate flower patches that\nhave even tiny amounts of pollen.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "It loves the honey of flowers and\ncan locate flower patches that\nhave even tiny amounts of pollen.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black-2",
            "url": "https://pokeapi.co/api/v2/version/21/"
          }
        },
        {
          "flavor_text": "It loves the honey of flowers and\ncan locate flower patches that\nhave even tiny amounts of pollen.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white-2",
            "url": "https://pokeapi.co/api/v2/version/22/"
          }
        },
        {
          "flavor_text": "はなの　ミツが　だいこうぶつ。\nわずかな　かふんで　はなばたけの\nばしょを　さがしだすことが　できる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "꽃의 꿀을 매우 좋아한다.\n약간의 꽃가루만으로 꽃밭이\n있는 장소를 찾아낼 수 있다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Il raffole du nectar des fleurs. Il est capable de\nrepérer la plus petite quantité de pollen.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Es liebt Blütenhonig. Es findet selbst Blumen,\ndie sehr wenig Pollen haben.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Adora el néctar de las flores. Puede localizar hasta las\nmás pequeñas cantidades de polen.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Adora il nettare dei fiori e riesce a localizzare i campi\nin cui si trova anche una minima quantità di polline.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "It loves the honey of flowers and can locate\nflower patches that have even tiny amounts\nof pollen.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "花の　ミツが　大好物。\nわずかな　花粉で　花畑の\n場所を　探し出すことが　できる。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "ハネは　みずを　はじく　りんぷんに\nまもられている。あめの　ひでも\nそらを　とぶことが　できる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "물을 튕겨내는 가루가\n날개를 보호하고 있다. 비가 오는 날에도\n하늘을 날 수 있다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Ses ailes sont recouvertes d’une poudre les\nprotégeant de la pluie. Ce Pokémon peut donc voler\npendant de grosses averses.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Seine Flügel sind mit Wasser abweisendem Staub\nüberzogen. Daher kann dieses Pokémon auch bei\nRegen fliegen.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Tiene las alas protegidas con una capa impermeable,\nde ahí que pueda volar también cuando llueve.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Una polvere idrorepellente gli ricopre le ali,\npermettendogli di volare anche sotto la pioggia.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "The wings are protected by rain-repellent dust.\nAs a result, this Pokémon can fly about even\nin rain.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "羽は　水を　弾く　りんぷんに\n守られている。雨の　日でも\n空を　飛ぶことが　できる。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "おいしい　はなの　ミツを　さがす　のうりょくに\nすぐれ　すみかから　１０キロはなれた　ばしょに\nさく　はなから　ミツを　あつめて　はこんでいる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "맛있는 꽃의 꿀을 찾는 능력이\n뛰어나서 사는 곳에서 10km 떨어진 장소에\n핀 꽃에서 꿀을 모아 옮긴다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Papilusion est très doué pour repérer le délicieux nectar qu’il\nbutine dans les fleurs. Il peut détecter, extraire et transporter\nle nectar de fleurs situées à plus de 10 km de son nid.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Smettbos größte Fähigkeit ist das Aufspüren köstlichen\nBlütenhonigs. Es findet sogar Honig in Blumen, die fast\n10 km von seinem Nest entfernt blühen.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Butterfree tiene una habilidad especial para encontrar\ndelicioso polen en las flores. Puede localizar, extraer y\ntransportar polen de flores que estén floreciendo a 10 km\nde distancia de su nido.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Butterfree è dotato di abilità molto raffinate per individuare\nil delizioso nettare dei fiori. Riesce a trovare, estrarre\ne trasportare il nettare dai fiori in boccio al nido anche\nper 10 km.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Butterfree has a superior ability to search for delicious honey\nfrom flowers. It can even search out, extract, and carry honey\nfrom flowers that are blooming over six miles from its nest.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "美味しい　花の　ミツを　探す　能力に\n優れ　すみかから　１０キロ離れた　場所に\n咲く　花から　ミツを　集めて　運んでいる。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "おいしい　はなの　ミツを　さがす　のうりょくに\nすぐれ　すみかから　１０キロはなれた　ばしょに\nさく　はなから　ミツを　あつめて　はこんでいる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "맛있는 꽃의 꿀을 찾는 능력이\n뛰어나서 사는 곳에서 10km 떨어진 장소에\n핀 꽃에서 꿀을 모아 옮긴다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Papilusion est très doué pour repérer le délicieux nectar qu’il\nbutine dans les fleurs. Il peut détecter, extraire et transporter\nle nectar de fleurs situées à plus de 10 km de son nid.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Smettbos größte Fähigkeit ist das Aufspüren köstlichen\nBlütenhonigs. Es findet sogar Honig in Blumen, die fast\n10 km von seinem Nest entfernt blühen.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Butterfree tiene una habilidad especial para encontrar\ndelicioso polen en las flores. Puede localizar, extraer y\ntransportar polen de flores que estén floreciendo a 10 km\nde distancia de su nido.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Butterfree è dotato di abilità molto raffinate per individuare\nil delizioso nettare dei fiori. Riesce a trovare, estrarre\ne trasportare il nettare dai fiori in boccio al nido anche\nper 10 km.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Butterfree has a superior ability to search for delicious honey\nfrom flowers. It can even search out, extract, and carry honey\nfrom flowers that are blooming over six miles from its nest.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "美味しい　花の　ミツを　探す　能力に\n優れ　すみかから　１０キロ離れた　場所に\n咲く　花から　ミツを　集めて　運んでいる。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "おおきな　めを　よく　かんさつすると\nじつは　ちいさな　めが　むすうに\nあつまって　できているのが　わかる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "커다란 눈을 잘 관찰하면\n사실 작은 눈이 무수히 모여\n만들어진 것을 알 수 있다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "仔細觀察那雙大眼睛的話，\n會發現那其實是由無數小眼睛\n聚集在一起而形成的。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "Si l’on regarde ses grands yeux de plus près,\non remarque qu’il s’agit en réalité d’une\nmultitude de petits yeux réunis.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "Bei genauerer Betrachtung zeigt sich, dass\nseine zwei großen Augen jeweils aus einer\nVielzahl an kleineren Augen bestehen.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "Al mirar sus grandes ojos desde cerca, puede\nobservarse como en realidad están compuestos\nde incontables ojos diminutos.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "Osservando da vicino i suoi grandi occhi\nsi nota che in realtà sono composti da una\nmiriade di minuscoli occhietti.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "Close examination of its large eyes reveals that\neach eye is composed of a myriad of tiny eyes.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "大きな　眼を　よく　観察すると\n実は　小さな　眼が　無数に\n集まって　できているのが　わかる。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "仔细观察那对大眼睛的话，\n会发现其实是许许多多小眼睛\n聚集在一起形成的。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "ほかの　ポケモンに　おそわれると\nどくの　りんぷんを　まきちらしながら\nはばたいて　ていこう　するのだ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "다른 포켓몬에게 습격당하면\n독 인분을 흩뿌리며\n날갯짓하여 저항한다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "如果被其他寶可夢襲擊，\n就會一邊散布有毒的鱗粉，\n一邊拍動翅膀抵抗。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "Pour se défendre contre les agressions d’autres\nPokémon, il bat des ailes en éparpillant autour\nde lui un nuage de poussière toxique.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "Wird es von einem anderen Pokémon angegriffen,\nwehrt es sich, indem es mit den Flügeln schlägt\nund giftigen Flügelstaub verstreut.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "Cuando lo atacan, Butterfree aletea con fuerza\ny esparce escamas venenosas con las que hace\nfrente a su adversario.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "Quando viene attaccato da altri Pokémon,\nsi difende sbattendo le ali e spargendo intorno\na sé polveri velenose.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "When attacked by other Pokémon, it defends\nitself by scattering its poisonous scales and\nfluttering its wings.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "他の　ポケモンに　襲われると\n毒の　鱗粉を　撒き散らしながら\n羽ばたいて　抵抗　するのだ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "如果被其他宝可梦袭击，\n就会一边挥洒有毒的鳞粉，\n一边拍动翅膀抵抗。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "ハネを　つつむ　りんぷんは　もうどく。\nキャタピーを　ねらう　とりポケモンを\nみつけると　ふりかけて　おいはらうぞ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "날개를 감싼 인분은 맹독이다.\n캐터피를 노리는 새포켓몬을\n발견하면 흩뿌려 내쫓는다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "附著在翅膀上的鱗粉帶有劇毒，\n一旦發現有鳥寶可夢要襲擊綠毛蟲，\n就會撒出鱗粉來趕跑對方。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "Lorsqu’il surprend un Pokémon oiseau attaquant\nun Chenipan, il répand les écailles très toxiques\nqui recouvrent ses ailes sur l’assaillant.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "Sieht es ein Raupy, das von Vogel-Pokémon\nangegriffen wird, schlägt es diese mit seinem\nhochgiftigen Flügelstaub in die Flucht.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "Si un Pokémon pájaro acecha a un Caterpie,\nButterfree esparcirá las escamas venenosas\nque recubren sus alas para ahuyentarlo.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "Se vede dei Pokémon alati attaccare Caterpie,\nli scaccia cospargendoli con la velenosissima \npolvere che ricopre le sue ali.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "Its wings are covered in toxic scales. If it finds\nbird Pokémon going after Caterpie, Butterfree\nsprinkles its scales on them to drive them off.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "羽を　包む　りん粉は　猛毒。\nキャタピーを　狙う　とりポケモンを\n見つけると　ふりかけて　追い払うぞ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "翅膀上覆盖着的鳞粉有剧毒。\n如果发现有鸟宝可梦要袭击绿毛虫，\n就会撒出鳞粉将它赶跑。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "きれいな　はなの　ミツが　こうぶつ。\nはなばたけで　アブリーとの　しれつな\nなわばりあらそいを　くりひろげる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "예쁜 꽃의 꿀을 좋아한다.\n꽃밭에서 에블리와 치열한\n영역 싸움을 벌인다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "愛吃美麗花朵的花蜜，\n總是在花圃和萌虻\n展開激烈的地盤爭奪戰。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "Il raffole du nectar des plus jolies fleurs.\nDans les prairies, les luttes territoriales\nl’opposant à Bombydou sont impitoyables.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "Es liebt den Blütenhonig schöner Blumen.\nAuf Blumenfeldern liefert es sich erbitterte\nRevierkämpfe mit Wommel.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "Adora el néctar de las flores más bellas. Libra\nferoces disputas territoriales en los prados con\nlos Cutiefly.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "È ghiotto del nettare dei fiori più belli.\nSi contende i prati in fiore con Cutiefly in furiose\nlotte per il territorio.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "Nectar from pretty flowers is its favorite food.\nIn fields of flowers, it has heated battles with\nCutiefly for territory.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "綺麗な　花の　ミツが　好物。\n花畑で　アブリーとの　熾烈な\n縄張り争いを　繰り広げる。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "喜食美丽花儿的花蜜。\n会在花圃里和萌虻\n展开激烈的领地之争。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "ハネの　もうどくの　りんぷんには\nみずをはじく　せいしつが　あるので\nあめのひ　でも　とびまわれる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "날개에 있는 맹독을 가진 인분에는\n물을 튕겨내는 성질이 있어\n비가 오는 날에도 날아다닐 수 있다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "翅膀上的劇毒鱗粉\n有著能夠防水的特性，\n即使在雨天也能自在飛翔。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Ses ailes sont enduites d’une poudre toxique\nimperméable lui permettant de voler sous\nla pluie.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Da die hochgiftige Staubschicht auf seinen\nFlügeln wasserabweisend ist, kann es auch\nbei Regen umherfliegen.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Sus alas están recubiertas de escamas venenosas\nimpermeables que le permiten volar bajo la\nlluvia.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Possiede ali idrorepellenti ricoperte da una\npolvere velenosa. Può volare anche quando\npiove.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Its wings, covered with poisonous powder, repel\nwater. This allows it to fly in the rain.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "ハネの　猛毒の　りん粉には\n水を弾く　性質が　あるので\n雨の日　でも　飛びまわれる。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "它翅膀上的剧毒鳞粉\n能够防水，因此即使是\n雨天也可以飞来飞去。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "ハネの　もうどくの　りんぷんには\nみずをはじく　せいしつが　あるので\nあめのひ　でも　とびまわれる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "날개에 있는 맹독을 가진 인분에는\n물을 튕겨내는 성질이 있어\n비가 오는 날에도 날아다닐 수 있다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "翅膀上的劇毒鱗粉\n有著能夠防水的特性，\n即使在雨天也能自在飛翔。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Ses ailes sont enduites d’une poudre toxique\nimperméable lui permettant de voler sous\nla pluie.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Da die hochgiftige Staubschicht auf seinen\nFlügeln wasserabweisend ist, kann es auch\nbei Regen umherfliegen.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Sus alas están recubiertas de escamas venenosas\nimpermeables que le permiten volar bajo la\nlluvia.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Possiede ali idrorepellenti ricoperte da una\npolvere velenosa. Può volare anche quando\npiove.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Its wings, covered with poisonous powder, repel\nwater. This allows it to fly in the rain.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "ハネの　猛毒の　りん粉には\n水を弾く　性質が　あるので\n雨の日　でも　飛びまわれる。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "它翅膀上的剧毒鳞粉\n能够防水，因此即使是\n雨天也可以飞来飞去。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "こまかく　はやく　はばたいたら\nもうどくの　りんぷんが\nかぜに　のって　とんでくるぞ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "매우 빠르게 날갯짓하면\n맹독성의 인분이\n바람을 타고 날아간다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "當牠飛快地拍動翅膀，\n帶有劇毒的鱗粉就會\n隨著風向這裡飄過來。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "En combat, il bat des ailes très rapidement pour\nprojeter de la poudre toxique sur ses ennemis.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Wenn es sehr schnell mit den Flügeln schlägt,\nsetzt es hochgiftigen Flügelstaub frei.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Aletea a gran velocidad para lanzar al aire sus\nescamas extremadamente tóxicas.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "Sbatte le ali a gran velocità per liberare\nle sue polveri tossiche nell’aria.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "In battle, it flaps its wings at great speed to\nrelease highly toxic dust into the air.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "こまかく　速く　羽ばたいたら\n猛毒の　りんぷんが\n風に　のって　飛んでくるぞ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "当它飞快地扑打翅膀，\n带有剧毒的鳞粉就会\n随着风向这里飘过来。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "sword",
            "url": "https://pokeapi.co/api/v2/version/33/"
          }
        },
        {
          "flavor_text": "まいにち　ミツを　あつめまわる。\nあしの　うぶげに　ミツを　ぬりこんで\nすに　もちかえる　しゅうせいをもつ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "매일 꿀을 모으러 다닌다.\n다리의 솜털에 꿀을 발라\n둥지로 가지고 가는 습성이 있다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "每天都忙著採集花蜜。\n習慣在腿部的細毛上塗滿花蜜，\n然後帶回巢穴裡。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Il ramasse du nectar chaque jour et l’agglutine\nsur les poils de ses pattes pour le transporter\njusqu’à son nid.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Es sammelt täglich Honig. Es reibt ihn in seine\nBeinhaare, um ihn in sein Nest zu transportieren.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Recoge néctar a diario y se lo adhiere al pelo de\nlas patas para llevarlo a su nido.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "Raccoglie nettare tutti i giorni e lo spalma sulla\npeluria che ricopre le sue zampe per trasportarlo\nal nido.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "It collects honey every day. It rubs honey onto\nthe hairs on its legs to carry it back to its nest.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "毎日　ミツを　集めまわる。\n脚の　産毛に　ミツを　塗りこんで\n巣に　持ち帰る　習性をもつ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        },
        {
          "flavor_text": "每天都忙着采集花蜜。\n习惯往腿部的细毛上涂满花蜜，\n然后带回巢穴里。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "shield",
            "url": "https://pokeapi.co/api/v2/version/34/"
          }
        }
      ],
      "form_descriptions": [],
      "forms_switchable": False,
      "gender_rate": 4,
      "genera": [
        {
          "genus": "ちょうちょポケモン",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          }
        },
        {
          "genus": "나비포켓몬",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          }
        },
        {
          "genus": "蝴蝶寶可夢",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          }
        },
        {
          "genus": "Pokémon Papillon",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          }
        },
        {
          "genus": "Falter-Pokémon",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        },
        {
          "genus": "Pokémon Mariposa",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          }
        },
        {
          "genus": "Pokémon Farfalla",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          }
        },
        {
          "genus": "Butterfly Pokémon",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        },
        {
          "genus": "ちょうちょポケモン",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          }
        },
        {
          "genus": "蝴蝶宝可梦",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          }
        }
      ],
      "generation": {
        "name": "generation-i",
        "url": "https://pokeapi.co/api/v2/generation/1/"
      },
      "growth_rate": {
        "name": "medium",
        "url": "https://pokeapi.co/api/v2/growth-rate/2/"
      },
      "habitat": {
        "name": "forest",
        "url": "https://pokeapi.co/api/v2/pokemon-habitat/2/"
      },
      "has_gender_differences": True,
      "hatch_counter": 15,
      "id": 12,
      "is_baby": False,
      "is_legendary": False,
      "is_mythical": False,
      "name": "butterfree",
      "names": [
        {
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "name": "バタフリー"
        },
        {
          "language": {
            "name": "roomaji",
            "url": "https://pokeapi.co/api/v2/language/2/"
          },
          "name": "Butterfree"
        },
        {
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "name": "버터플"
        },
        {
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "name": "巴大蝶"
        },
        {
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "name": "Papilusion"
        },
        {
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "name": "Smettbo"
        },
        {
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "name": "Butterfree"
        },
        {
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "name": "Butterfree"
        },
        {
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "name": "Butterfree"
        },
        {
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "name": "バタフリー"
        },
        {
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "name": "巴大蝶"
        }
      ],
      "order": 12,
      "pal_park_encounters": [
        {
          "area": {
            "name": "forest",
            "url": "https://pokeapi.co/api/v2/pal-park-area/1/"
          },
          "base_score": 70,
          "rate": 20
        }
      ],
      "pokedex_numbers": [
        {
          "entry_number": 12,
          "pokedex": {
            "name": "national",
            "url": "https://pokeapi.co/api/v2/pokedex/1/"
          }
        },
        {
          "entry_number": 12,
          "pokedex": {
            "name": "kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/2/"
          }
        },
        {
          "entry_number": 26,
          "pokedex": {
            "name": "original-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/3/"
          }
        },
        {
          "entry_number": 26,
          "pokedex": {
            "name": "updated-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/7/"
          }
        },
        {
          "entry_number": 25,
          "pokedex": {
            "name": "kalos-central",
            "url": "https://pokeapi.co/api/v2/pokedex/12/"
          }
        },
        {
          "entry_number": 19,
          "pokedex": {
            "name": "original-alola",
            "url": "https://pokeapi.co/api/v2/pokedex/16/"
          }
        },
        {
          "entry_number": 19,
          "pokedex": {
            "name": "original-melemele",
            "url": "https://pokeapi.co/api/v2/pokedex/17/"
          }
        },
        {
          "entry_number": 10,
          "pokedex": {
            "name": "original-akala",
            "url": "https://pokeapi.co/api/v2/pokedex/18/"
          }
        },
        {
          "entry_number": 19,
          "pokedex": {
            "name": "updated-alola",
            "url": "https://pokeapi.co/api/v2/pokedex/21/"
          }
        },
        {
          "entry_number": 19,
          "pokedex": {
            "name": "updated-melemele",
            "url": "https://pokeapi.co/api/v2/pokedex/22/"
          }
        },
        {
          "entry_number": 10,
          "pokedex": {
            "name": "updated-akala",
            "url": "https://pokeapi.co/api/v2/pokedex/23/"
          }
        },
        {
          "entry_number": 12,
          "pokedex": {
            "name": "letsgo-kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/26/"
          }
        },
        {
          "entry_number": 15,
          "pokedex": {
            "name": "galar",
            "url": "https://pokeapi.co/api/v2/pokedex/27/"
          }
        }
      ],
      "shape": {
        "name": "bug-wings",
        "url": "https://pokeapi.co/api/v2/pokemon-shape/13/"
      },
      "varieties": [
        {
          "is_default": True,
          "pokemon": {
            "name": "butterfree",
            "url": "https://pokeapi.co/api/v2/pokemon/12/"
          }
        },
        {
          "is_default": False,
          "pokemon": {
            "name": "butterfree-gmax",
            "url": "https://pokeapi.co/api/v2/pokemon/10198/"
          }
        }
      ]
    },
    {
      "base_happiness": 70,
      "capture_rate": 255,
      "color": {
        "name": "brown",
        "url": "https://pokeapi.co/api/v2/pokemon-color/3/"
      },
      "egg_groups": [
        {
          "name": "bug",
          "url": "https://pokeapi.co/api/v2/egg-group/3/"
        }
      ],
      "evolution_chain": {
        "url": "https://pokeapi.co/api/v2/evolution-chain/5/"
      },
      "evolves_from_species": None,
      "flavor_text_entries": [
        {
          "flavor_text": "Often found in\nforests, eating\nleaves.\fIt has a sharp\nvenomous stinger\non its head.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "red",
            "url": "https://pokeapi.co/api/v2/version/1/"
          }
        },
        {
          "flavor_text": "Often found in\nforests, eating\nleaves.\fIt has a sharp\nvenomous stinger\non its head.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "blue",
            "url": "https://pokeapi.co/api/v2/version/2/"
          }
        },
        {
          "flavor_text": "Beware of the\nsharp stinger on\nits head. It\fhides in grass\nand bushes where\nit eats leaves.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version/3/"
          }
        },
        {
          "flavor_text": "Its poison stinger\nis very powerful.\nIts bright-colored\fbody is intended\nto warn off its\nenemies.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "gold",
            "url": "https://pokeapi.co/api/v2/version/4/"
          }
        },
        {
          "flavor_text": "It attacks using a\ntwo-inch poison\nbarb on its head.\fIt can usually be\nfound under the\nleaves it eats.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "silver",
            "url": "https://pokeapi.co/api/v2/version/5/"
          }
        },
        {
          "flavor_text": "The barb on top of\nits head secretes\na strong poison.\fIt uses this toxic\nbarb to protect\nitself.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version/6/"
          }
        },
        {
          "flavor_text": "WEEDLE has an extremely acute sense\nof smell.\nIt is capable of distinguishing its\ffavorite kinds of leaves from those it\ndislikes just by sniffing with its big\nred proboscis (nose).",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "ruby",
            "url": "https://pokeapi.co/api/v2/version/7/"
          }
        },
        {
          "flavor_text": "WEEDLE has an extremely acute sense\nof smell.\nIt is capable of distinguishing its\ffavorite kinds of leaves from those it\ndislikes just by sniffing with its big\nred proboscis (nose).",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sapphire",
            "url": "https://pokeapi.co/api/v2/version/8/"
          }
        },
        {
          "flavor_text": "A WEEDLE has an extremely acute sense\nof smell. It distinguishes its favorite\nkinds of leaves from those it dislikes by\nsniffing with its big red proboscis (nose).",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version/9/"
          }
        },
        {
          "flavor_text": "Often found in forests and grasslands.\nIt has a sharp, toxic barb of around two\ninches on top of its head.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "firered",
            "url": "https://pokeapi.co/api/v2/version/10/"
          }
        },
        {
          "flavor_text": "Often found in forests, eating leaves.\nIt has a sharp stinger on its head that\ninjects poison.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "leafgreen",
            "url": "https://pokeapi.co/api/v2/version/11/"
          }
        },
        {
          "flavor_text": "It eats its weight in leaves every\nday. It fends off attackers with\nthe needle on its head.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "diamond",
            "url": "https://pokeapi.co/api/v2/version/12/"
          }
        },
        {
          "flavor_text": "It eats its weight in leaves every\nday. It fends off attackers with\nthe needle on its head.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "pearl",
            "url": "https://pokeapi.co/api/v2/version/13/"
          }
        },
        {
          "flavor_text": "It eats its weight in leaves every\nday. It fends off attackers with\nthe needle on its head.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version/14/"
          }
        },
        {
          "flavor_text": "Its poison stinger is very powerful.\nIts bright-colored body is intended\nto warn off its enemies.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "heartgold",
            "url": "https://pokeapi.co/api/v2/version/15/"
          }
        },
        {
          "flavor_text": "It attacks using a two-inch poison\nbarb on its head. It can usually be\nfound under the leaves it eats.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "soulsilver",
            "url": "https://pokeapi.co/api/v2/version/16/"
          }
        },
        {
          "flavor_text": "Il mange chaque jour son poids en\nfeuilles. Il utilise l’aiguillon sur sa\ntête pour repousser l’ennemi.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "It eats its weight in leaves every\nday. It fends off attackers with\nthe needle on its head.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "Il mange chaque jour son poids en\nfeuilles. Il utilise l’aiguillon sur sa\ntête pour repousser l’ennemi.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "It eats its weight in leaves every\nday. It fends off attackers with\nthe needle on its head.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "It eats its weight in leaves every\nday. It fends off attackers with\nthe needle on its head.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black-2",
            "url": "https://pokeapi.co/api/v2/version/21/"
          }
        },
        {
          "flavor_text": "It eats its weight in leaves every\nday. It fends off attackers with\nthe needle on its head.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white-2",
            "url": "https://pokeapi.co/api/v2/version/22/"
          }
        },
        {
          "flavor_text": "もりや　くさちに　おおく　せいそく。\nあたまの　さきに　５センチぐらいの\nちいさく　するどい　どくばりをもつ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "숲이나 풀밭에 많이 서식한다.\n머리끝에 5cm 정도의\n작고 날카로운 독침을 지니고 있다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "On trouve souvent ce Pokémon dans les forêts et\nles hautes herbes. L’aiguillon de 5 cm sur sa tête\ncontient un venin très toxique.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Es lebt bevorzugt in Wäldern und in hohem Gras.\nAuf dem Kopf trägt es einen circa 5 cm langen,\nspitzen, giftigen Stachel.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Suele habitar bosques y praderas. Tiene un afilado y\nvenenoso aguijón de unos 5 cm encima de la cabeza.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Vive soprattutto nei boschi e nei prati. Sul capo ha\nun affilato e velenoso pungiglione lungo 5 cm.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Often found in forests and grasslands.\nIt has a sharp, toxic barb of around two inches\non top of its head.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "森や　草地に　多く　生息。\n頭の　先に　５センチぐらいの\n小さく　鋭い　毒針を持つ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "どくばりは　とても　きょうりょく。\nめだつ　からだの　いろは\nあいてに　けいかいを　させるためだ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "독침이 매우 강력하다.\n눈에 띄는 몸의 색깔은\n상대방을 경계시키기 위해서다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Son aiguillon empoisonné est très dangereux.\nSon corps est coloré afin de repousser ses ennemis.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Sein Giftstachel ist gefährlich. Sein hellleuchtender\nKörper soll Feinde abschrecken.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Su venenoso aguijón es muy potente y su colorido\ncuerpo hace que los enemigos huyan.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Ha un pungiglione molto velenoso. La vivace\ncolorazione del suo corpo è un avvertimento per i\nnemici.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Its poison stinger is very powerful.\nIts bright-colored body is intended to\nwarn off its enemies.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "毒針は　とても　強力。\n目立つ　体の　色は\n相手に　警戒を　させるためだ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "とても　するどい　きゅうかくを　もっている。\nこうぶつの　はっぱか　きらいな　はっぱか\nおおきな　あかい　はなで　かぎわける。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "굉장히 예민한 후각을 지니고 있다.\n좋아하는 잎사귀인지 싫어하는 잎사귀인지\n크고 빨간 코로 냄새 맡아 구별한다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "L’odorat d’Aspicot est extrêmement développé. Il lui suffit de\nrenifler ses feuilles préférées avec son gros appendice nasal\npour les reconnaître entre mille.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Hornliu verfügt über einen ausgezeichneten Geruchssinn.\nSo kann es seine Lieblingsblätter von denen unterscheiden,\ndie es nicht mag, indem es mit seiner großen roten Nase\ndaran schnuppert.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Weedle tiene un finísimo sentido del olfato. Es capaz de\ndistinguir las hojas que le gustan de las que no le gustan\nolisqueando un poco con la gran nariz que tiene.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Weedle ha un senso dell’olfatto estremamente sviluppato.\nRiesce a distinguere le sue foglie preferite da quelle che\nlo disgustano semplicemente annusandole con il grande\nnaso rosso.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Weedle has an extremely acute sense of smell. It is capable of\ndistinguishing its favorite kinds of leaves from those it dislikes\njust by sniffing with its big red proboscis (nose).",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "とても　鋭い　嗅覚を　持っている。\n好物の　葉っぱか　嫌いな　葉っぱか\n大きな　赤い　鼻で　嗅ぎ分ける。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "とても　するどい　きゅうかくを　もっている。\nこうぶつの　はっぱか　きらいな　はっぱか\nおおきな　あかい　はなで　かぎわける。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "굉장히 예민한 후각을 지니고 있다.\n좋아하는 잎사귀인지 싫어하는 잎사귀인지\n크고 빨간 코로 냄새 맡아 구별한다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "L’odorat d’Aspicot est extrêmement développé. Il lui suffit de\nrenifler ses feuilles préférées avec son gros appendice nasal\npour les reconnaître entre mille.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Hornliu verfügt über einen ausgezeichneten Geruchssinn.\nEs ist in der Lage, seine Lieblingsblätter von denen zu\nunterscheiden, die es nicht mag, indem es mit seinem großen\nroten Rüssel daran schnuppert.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Weedle tiene un finísimo sentido del olfato. Es capaz de\ndistinguir las hojas que le gustan de las que no le gustan\nolisqueando un poco con la gran nariz que tiene.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Weedle ha un senso dell’olfatto estremamente sviluppato.\nRiesce a distinguere le sue foglie preferite da quelle che\nlo disgustano semplicemente annusandole con il grande\nnaso rosso.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Weedle has an extremely acute sense of smell. It is capable\nof distinguishing its favorite kinds of leaves from those it\ndislikes just by sniffing with its big red proboscis (nose).",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "とても　鋭い　嗅覚を　持っている。\n好物の　葉っぱか　嫌いな　葉っぱか\n大きな　赤い　鼻で　嗅ぎ分ける。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "あたまに　するどい　ハリを　もつ。\nもりや　くさちの　しげみに　かくれ\nひたすら　ハッパを　たべている。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "머리에 날카로운 침을 지니고 있다.\n우거진 숲이나 풀밭에 숨어\n끊임없이 풀잎을 먹고 있다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "頭上長著尖銳的針。\n總是躲在森林或是草叢裡，\n不停地吃著葉子。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "L’aiguillon sur son front est très pointu.\nIl se cache dans les bois et les hautes herbes,\noù il se gave de feuilles.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Auf seinem Kopf befindet sich ein spitzer\nStachel. Es versteckt sich im hohen Gras\nsowie in Wäldern und frisst eifrig Blätter.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "El aguijón de la cabeza es muy puntiagudo.\nSe alimenta de hojas oculto en la espesura\nde bosques y praderas.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Ha un pungiglione acuminato sul capo. Vive tra\nl’erba alta e nei boschi, dove si nutre di foglie.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Beware of the sharp stinger on its head. It hides\nin grass and bushes where it eats leaves.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "頭に　鋭い　ハリを　もつ。\n森や　草地の　茂みに　隠れ\nひたすら　ハッパを　食べている。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "头上长有尖锐的针。\n它喜欢藏在森林或\n草丛里大量吞食树叶。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "あたまに　するどい　ハリを　もつ。\nもりや　くさちの　しげみに　かくれ\nひたすら　ハッパを　たべている。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "머리에 날카로운 침을 지니고 있다.\n우거진 숲이나 풀밭에 숨어\n끊임없이 풀잎을 먹고 있다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "頭上長著尖銳的針。\n總是躲在森林或是草叢裡，\n不停地吃著葉子。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "L’aiguillon sur son front est très pointu.\nIl se cache dans les bois et les hautes herbes,\noù il se gave de feuilles.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Auf seinem Kopf befindet sich ein spitzer\nStachel. Es versteckt sich im hohen Gras\nsowie in Wäldern und frisst eifrig Blätter.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "El aguijón de la cabeza es muy puntiagudo.\nSe alimenta de hojas oculto en la espesura\nde bosques y praderas.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Ha un pungiglione acuminato sul capo. Vive tra\nl’erba alta e nei boschi, dove si nutre di foglie.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Beware of the sharp stinger on its head. It hides\nin grass and bushes where it eats leaves.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "頭に　鋭い　ハリを　もつ。\n森や　草地の　茂みに　隠れ\nひたすら　ハッパを　食べている。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "头上长有尖锐的针。\n它喜欢藏在森林或\n草丛里大量吞食树叶。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        }
      ],
      "form_descriptions": [],
      "forms_switchable": False,
      "gender_rate": 4,
      "genera": [
        {
          "genus": "けむしポケモン",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          }
        },
        {
          "genus": "송충이포켓몬",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          }
        },
        {
          "genus": "毛毛蟲寶可夢",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          }
        },
        {
          "genus": "Pokémon Insectopic",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          }
        },
        {
          "genus": "Raupe",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        },
        {
          "genus": "Pokémon Oruga",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          }
        },
        {
          "genus": "Pokémon Millepiedi",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          }
        },
        {
          "genus": "Hairy Bug Pokémon",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        },
        {
          "genus": "けむしポケモン",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          }
        },
        {
          "genus": "毛毛虫宝可梦",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          }
        }
      ],
      "generation": {
        "name": "generation-i",
        "url": "https://pokeapi.co/api/v2/generation/1/"
      },
      "growth_rate": {
        "name": "medium",
        "url": "https://pokeapi.co/api/v2/growth-rate/2/"
      },
      "habitat": {
        "name": "forest",
        "url": "https://pokeapi.co/api/v2/pokemon-habitat/2/"
      },
      "has_gender_differences": False,
      "hatch_counter": 15,
      "id": 13,
      "is_baby": False,
      "is_legendary": False,
      "is_mythical": False,
      "name": "weedle",
      "names": [
        {
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "name": "ビードル"
        },
        {
          "language": {
            "name": "roomaji",
            "url": "https://pokeapi.co/api/v2/language/2/"
          },
          "name": "Beedle"
        },
        {
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "name": "뿔충이"
        },
        {
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "name": "獨角蟲"
        },
        {
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "name": "Aspicot"
        },
        {
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "name": "Hornliu"
        },
        {
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "name": "Weedle"
        },
        {
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "name": "Weedle"
        },
        {
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "name": "Weedle"
        },
        {
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "name": "ビードル"
        },
        {
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "name": "独角虫"
        }
      ],
      "order": 13,
      "pal_park_encounters": [
        {
          "area": {
            "name": "forest",
            "url": "https://pokeapi.co/api/v2/pal-park-area/1/"
          },
          "base_score": 30,
          "rate": 50
        }
      ],
      "pokedex_numbers": [
        {
          "entry_number": 13,
          "pokedex": {
            "name": "national",
            "url": "https://pokeapi.co/api/v2/pokedex/1/"
          }
        },
        {
          "entry_number": 13,
          "pokedex": {
            "name": "kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/2/"
          }
        },
        {
          "entry_number": 27,
          "pokedex": {
            "name": "original-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/3/"
          }
        },
        {
          "entry_number": 27,
          "pokedex": {
            "name": "updated-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/7/"
          }
        },
        {
          "entry_number": 26,
          "pokedex": {
            "name": "kalos-central",
            "url": "https://pokeapi.co/api/v2/pokedex/12/"
          }
        },
        {
          "entry_number": 13,
          "pokedex": {
            "name": "letsgo-kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/26/"
          }
        }
      ],
      "shape": {
        "name": "armor",
        "url": "https://pokeapi.co/api/v2/pokemon-shape/14/"
      },
      "varieties": [
        {
          "is_default": True,
          "pokemon": {
            "name": "weedle",
            "url": "https://pokeapi.co/api/v2/pokemon/13/"
          }
        }
      ]
    },
    {
      "base_happiness": 70,
      "capture_rate": 120,
      "color": {
        "name": "yellow",
        "url": "https://pokeapi.co/api/v2/pokemon-color/10/"
      },
      "egg_groups": [
        {
          "name": "bug",
          "url": "https://pokeapi.co/api/v2/egg-group/3/"
        }
      ],
      "evolution_chain": {
        "url": "https://pokeapi.co/api/v2/evolution-chain/5/"
      },
      "evolves_from_species": {
        "name": "weedle",
        "url": "https://pokeapi.co/api/v2/pokemon-species/13/"
      },
      "flavor_text_entries": [
        {
          "flavor_text": "Almost incapable\nof moving, this\nPOKéMON can only\fharden its shell\nto protect itself\nfrom predators.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "red",
            "url": "https://pokeapi.co/api/v2/version/1/"
          }
        },
        {
          "flavor_text": "Almost incapable\nof moving, this\nPOKéMON can only\fharden its shell\nto protect itself\nfrom predators.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "blue",
            "url": "https://pokeapi.co/api/v2/version/2/"
          }
        },
        {
          "flavor_text": "Able to move only\nslightly. When\nendangered, it\fmay stick out its\nstinger and poison\nits enemy.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version/3/"
          }
        },
        {
          "flavor_text": "Although it is a\ncocoon, it can\nmove a little. It\fcan extend its\npoison barb if it\nis attacked.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "gold",
            "url": "https://pokeapi.co/api/v2/version/4/"
          }
        },
        {
          "flavor_text": "From this form,\nit will grow into\nan adult. As its\fbody becomes soft­\ner, the external\nshell hardens.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "silver",
            "url": "https://pokeapi.co/api/v2/version/5/"
          }
        },
        {
          "flavor_text": "Nearly incapable\nof movement, it\nleans against\fstout trees while\nwaiting for its\nevolution.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version/6/"
          }
        },
        {
          "flavor_text": "KAKUNA remains virtually immobile as it\nclings to a tree. However, on the\ninside, it is extremely busy as it\fprepares for its coming evolution.\nThis is evident from how hot the shell\nbecomes to the touch.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "ruby",
            "url": "https://pokeapi.co/api/v2/version/7/"
          }
        },
        {
          "flavor_text": "KAKUNA remains virtually immobile as it\nclings to a tree. However, on the\ninside, it is extremely busy as it\fprepares for its coming evolution.\nThis is evident from how hot the shell\nbecomes to the touch.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sapphire",
            "url": "https://pokeapi.co/api/v2/version/8/"
          }
        },
        {
          "flavor_text": "It remains virtually immobile while it\nclings to a tree. However, on the inside,\nit busily prepares for evolution. This is\nevident from how hot its shell becomes.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version/9/"
          }
        },
        {
          "flavor_text": "This POKéMON is in a temporary stage\nwhile making its body. It is almost\ncompletely unable to move on its own.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "firered",
            "url": "https://pokeapi.co/api/v2/version/10/"
          }
        },
        {
          "flavor_text": "Almost incapable of moving, this POKéMON\ncan only harden its shell to protect\nitself when it is in danger.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "leafgreen",
            "url": "https://pokeapi.co/api/v2/version/11/"
          }
        },
        {
          "flavor_text": "While awaiting evolution, it\nhides from predators under\nleaves and in nooks of branches.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "diamond",
            "url": "https://pokeapi.co/api/v2/version/12/"
          }
        },
        {
          "flavor_text": "While awaiting evolution, it\nhides from predators under\nleaves and in nooks of branches.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "pearl",
            "url": "https://pokeapi.co/api/v2/version/13/"
          }
        },
        {
          "flavor_text": "While awaiting evolution, it\nhides from predators under\nleaves and in nooks of branches.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version/14/"
          }
        },
        {
          "flavor_text": "Although it is a cocoon, it can\nmove a little. It can extend its\npoison barb if it is attacked.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "heartgold",
            "url": "https://pokeapi.co/api/v2/version/15/"
          }
        },
        {
          "flavor_text": "From this form, it will grow into\nan adult. As its body becomes softer,\nthe external shell hardens.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "soulsilver",
            "url": "https://pokeapi.co/api/v2/version/16/"
          }
        },
        {
          "flavor_text": "Il se cache sous les feuilles et les\nbranches pour fuir les prédateurs\nen attendant d’évoluer.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "While awaiting evolution, it\nhides from predators under\nleaves and in nooks of branches.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "Il se cache sous les feuilles et les\nbranches pour fuir les prédateurs\nen attendant d’évoluer.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "While awaiting evolution, it\nhides from predators under\nleaves and in nooks of branches.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "While awaiting evolution, it\nhides from predators under\nleaves and in nooks of branches.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black-2",
            "url": "https://pokeapi.co/api/v2/version/21/"
          }
        },
        {
          "flavor_text": "While awaiting evolution, it\nhides from predators under\nleaves and in nooks of branches.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white-2",
            "url": "https://pokeapi.co/api/v2/version/22/"
          }
        },
        {
          "flavor_text": "じぶんでは　ほとんど　うごけないが\nあぶないときは　かたくなって\nみを　まもっているようだ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "스스로는 거의 움직일 수 없지만\n위험할 때는 단단해져서\n몸을 보호하고 있는 것 같다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Incapable de se déplacer de lui-même, il se défend en\ndurcissant sa carapace.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Dieses Pokémon kann sich kaum bewegen.\nBei drohender Gefahr verhärtet es seinen Panzer.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Casi incapaz de moverse, este Pokémon solo puede\nendurecer su caparazón para protegerse.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Quasi incapace di muoversi, questo Pokémon può\nsolo indurire il proprio guscio per proteggersi.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Almost incapable of moving, this Pokémon can only\nharden its shell to protect itself when it is\nin danger.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "自分では　ほとんど　動けないが\n危ないときは　硬くなって\n身を守っているようだ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "てんてきに　みつからないように\nはっぱの　うらや　えだの　すきまに\nかくれて　しんかの　ときを　まつ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "천적에게 발견되지 않도록\n잎사귀 뒷면이나 가지의 틈새에\n숨어서 진화할 때를 기다린다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Il se cache sous les feuilles et les branches pour fuir\nles prédateurs en attendant d’évoluer.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Während es auf seine Entwicklung wartet, versteckt es\nsich unter Blättern und zwischen Ästen.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Se esconde de sus atacantes entre las ramas de los\nárboles mientras espera a evolucionar.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Si nasconde dai predatori dietro le foglie e fra i rami,\nin attesa dell’evoluzione.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "While awaiting evolution, it hides from predators\nunder leaves and in nooks of branches.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "天敵に　見つからないように\n葉っぱの　裏や　枝の　すきまに　隠れて\n進化の　ときを　待つ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "ほとんど　うごかず　きに　つかまっているが\nなかでは　しんかの　じゅんびで　おおいそがし。\nその　しょうこに　からだが　あつくなっているぞ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "거의 움직이지 않고 나무에 매달려 있지만\n내부는 진화 준비로 굉장히 바쁜 상태다.\n그 증거로 몸이 뜨거워져 있다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Coconfort est la plupart du temps immobile et reste\naccroché à un arbre. Cependant, intérieurement, il est\ntrès actif, car il se prépare pour sa prochaine évolution.\nEn touchant sa carapace, on peut sentir sa chaleur.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Kokuna bewegt sich kaum, wenn es an einem Baum haftet.\nIn seinem Inneren jedoch regt sich einiges, da es sich auf\nseine bevorstehende Entwicklung vorbereitet. Dabei wird\nseine Schale sehr heiß.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Kakuna permanece prácticamente inmóvil al encaramarse a\nlos árboles, aunque la actividad interna de su organismo\ntiene un ritmo frenético, pues se prepara para su evolución.\nPrueba de esto es la alta temperatura de su caparazón.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Kakuna rimane praticamente immobile abbarbicato agli alberi.\nTuttavia, internamente è intento a preparare la sua futura\nevoluzione. Lo si può capire dall’intensità del calore\nsviluppato dal guscio.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Kakuna remains virtually immobile as it clings to a tree.\nHowever, on the inside, it is extremely busy as it prepares for\nits coming evolution. This is evident from how hot the shell\nbecomes to the touch.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "ほとんど　動かず　木に　つかまっているが\n中では　進化の　準備で　大忙し。\nその　証拠に　体が　熱くなっているぞ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "ほとんど　うごかず　きに　つかまっているが\nなかでは　しんかの　じゅんびで　おおいそがし。\nその　しょうこに　からだが　あつくなっているぞ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "거의 움직이지 않고 나무에 매달려 있지만\n내부는 진화 준비로 굉장히 바쁜 상태다.\n그 증거로 몸이 뜨거워져 있다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Coconfort est la plupart du temps immobile et reste\naccroché à un arbre. Cependant, intérieurement, il est\ntrès actif, car il se prépare pour sa prochaine évolution.\nEn touchant sa carapace, on peut sentir sa chaleur.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Kokuna bewegt sich kaum, wenn es sich an einen Baum heftet.\nIn seinem Inneren jedoch regt sich einiges, da es sich auf\nseine bevorstehende Entwicklung vorbereitet. Dabei wird seine\nSchale sehr heiß.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Kakuna permanece prácticamente inmóvil al encaramarse a\nlos árboles, aunque la actividad interna de su organismo\ntiene un ritmo frenético, pues se prepara para su evolución.\nPrueba de esto es la alta temperatura de su caparazón.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Kakuna rimane praticamente immobile abbarbicato agli alberi.\nTuttavia, internamente è intento a preparare la sua futura\nevoluzione. Lo si può capire dall’intensità del calore\nsviluppato dal guscio.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Kakuna remains virtually immobile as it clings to a tree.\nHowever, on the inside, it is extremely busy as it prepares\nfor its coming evolution.\nThis is evident from how hot the shell becomes to the touch.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "ほとんど　動かず　木に　つかまっているが\n中では　進化の　準備で　大忙し。\nその　証拠に　体が　熱くなっているぞ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "じぶんでは　ほとんど　うごけないが\nあぶなくなると　ハリをだして\nどくを　あたえることも　あるらしい。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "스스로는 거의 움직일 수 없지만\n위험해지면 침을 세워서\n독을 뿜을 때도 있는 듯하다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "雖然幾乎動也動不了，\n但如果遭遇到了危險，\n有時似乎會豎起毒刺來反抗。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Il peut à peine bouger. Quand il est menacé,\nil sort parfois son aiguillon pour empoisonner\nses ennemis.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Obwohl es sich kaum bewegen kann, ist es bei\nGefahr in der Lage, einen Stachel auszufahren,\nmit dem es seine Gegner vergiftet.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Aunque es casi incapaz de moverse, en caso\nde sentirse amenazado puede envenenar a los\nenemigos con su aguijón.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "È molto limitato nei movimenti. Se si sente\nminacciato, estrae il pungiglione e avvelena\nil nemico.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Able to move only slightly. When endangered, it\nmay stick out its stinger and poison its enemy.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "自分では　ほとんど　動けないが\n危なくなると　ハリを出して\n毒を　与えることも　あるらしい。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "虽然几乎动也动不了，\n但是如果遇到了危险，\n有时似乎会竖起毒刺来反抗。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "じぶんでは　ほとんど　うごけないが\nあぶなくなると　ハリをだして\nどくを　あたえることも　あるらしい。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "스스로는 거의 움직일 수 없지만\n위험해지면 침을 세워서\n독을 뿜을 때도 있는 듯하다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "雖然幾乎動也動不了，\n但如果遭遇到了危險，\n有時似乎會豎起毒刺來反抗。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Il peut à peine bouger. Quand il est menacé,\nil sort parfois son aiguillon pour empoisonner\nses ennemis.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Obwohl es sich kaum bewegen kann, ist es bei\nGefahr in der Lage, einen Stachel auszufahren,\nmit dem es seine Gegner vergiftet.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Aunque es casi incapaz de moverse, en caso\nde sentirse amenazado puede envenenar a los\nenemigos con su aguijón.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "È molto limitato nei movimenti. Se si sente\nminacciato, estrae il pungiglione e avvelena\nil nemico.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Able to move only slightly. When endangered, it\nmay stick out its stinger and poison its enemy.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "自分では　ほとんど　動けないが\n危なくなると　ハリを出して\n毒を　与えることも　あるらしい。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "虽然几乎动也动不了，\n但是如果遇到了危险，\n有时似乎会竖起毒刺来反抗。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        }
      ],
      "form_descriptions": [],
      "forms_switchable": False,
      "gender_rate": 4,
      "genera": [
        {
          "genus": "さなぎポケモン",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          }
        },
        {
          "genus": "번데기포켓몬",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          }
        },
        {
          "genus": "蛹寶可夢",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          }
        },
        {
          "genus": "Pokémon Cocon",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          }
        },
        {
          "genus": "Kokon",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        },
        {
          "genus": "Pokémon Capullo",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          }
        },
        {
          "genus": "Pokémon Bozzolo",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          }
        },
        {
          "genus": "Cocoon Pokémon",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        },
        {
          "genus": "さなぎポケモン",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          }
        },
        {
          "genus": "蛹宝可梦",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          }
        }
      ],
      "generation": {
        "name": "generation-i",
        "url": "https://pokeapi.co/api/v2/generation/1/"
      },
      "growth_rate": {
        "name": "medium",
        "url": "https://pokeapi.co/api/v2/growth-rate/2/"
      },
      "habitat": {
        "name": "forest",
        "url": "https://pokeapi.co/api/v2/pokemon-habitat/2/"
      },
      "has_gender_differences": False,
      "hatch_counter": 15,
      "id": 14,
      "is_baby": False,
      "is_legendary": False,
      "is_mythical": False,
      "name": "kakuna",
      "names": [
        {
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "name": "コクーン"
        },
        {
          "language": {
            "name": "roomaji",
            "url": "https://pokeapi.co/api/v2/language/2/"
          },
          "name": "Cocoon"
        },
        {
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "name": "딱충이"
        },
        {
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "name": "鐵殼蛹"
        },
        {
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "name": "Coconfort"
        },
        {
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "name": "Kokuna"
        },
        {
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "name": "Kakuna"
        },
        {
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "name": "Kakuna"
        },
        {
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "name": "Kakuna"
        },
        {
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "name": "コクーン"
        },
        {
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "name": "铁壳蛹"
        }
      ],
      "order": 14,
      "pal_park_encounters": [
        {
          "area": {
            "name": "forest",
            "url": "https://pokeapi.co/api/v2/pal-park-area/1/"
          },
          "base_score": 50,
          "rate": 30
        }
      ],
      "pokedex_numbers": [
        {
          "entry_number": 14,
          "pokedex": {
            "name": "national",
            "url": "https://pokeapi.co/api/v2/pokedex/1/"
          }
        },
        {
          "entry_number": 14,
          "pokedex": {
            "name": "kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/2/"
          }
        },
        {
          "entry_number": 28,
          "pokedex": {
            "name": "original-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/3/"
          }
        },
        {
          "entry_number": 28,
          "pokedex": {
            "name": "updated-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/7/"
          }
        },
        {
          "entry_number": 27,
          "pokedex": {
            "name": "kalos-central",
            "url": "https://pokeapi.co/api/v2/pokedex/12/"
          }
        },
        {
          "entry_number": 14,
          "pokedex": {
            "name": "letsgo-kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/26/"
          }
        }
      ],
      "shape": {
        "name": "squiggle",
        "url": "https://pokeapi.co/api/v2/pokemon-shape/2/"
      },
      "varieties": [
        {
          "is_default": True,
          "pokemon": {
            "name": "kakuna",
            "url": "https://pokeapi.co/api/v2/pokemon/14/"
          }
        }
      ]
    },
    {
      "base_happiness": 70,
      "capture_rate": 45,
      "color": {
        "name": "yellow",
        "url": "https://pokeapi.co/api/v2/pokemon-color/10/"
      },
      "egg_groups": [
        {
          "name": "bug",
          "url": "https://pokeapi.co/api/v2/egg-group/3/"
        }
      ],
      "evolution_chain": {
        "url": "https://pokeapi.co/api/v2/evolution-chain/5/"
      },
      "evolves_from_species": {
        "name": "kakuna",
        "url": "https://pokeapi.co/api/v2/pokemon-species/14/"
      },
      "flavor_text_entries": [
        {
          "flavor_text": "It has three poisonous stingers on its forelegs and\nits tail. They are used to jab its enemy repeatedly.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Flies at high\nspeed and attacks\nusing its large\fvenomous stingers\non its forelegs\nand tail.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "red",
            "url": "https://pokeapi.co/api/v2/version/1/"
          }
        },
        {
          "flavor_text": "Flies at high\nspeed and attacks\nusing its large\fvenomous stingers\non its forelegs\nand tail.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "blue",
            "url": "https://pokeapi.co/api/v2/version/2/"
          }
        },
        {
          "flavor_text": "It has 3 poisonous\nstingers on its\nforelegs and its\ftail. They are\nused to jab its\nenemy repeatedly.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version/3/"
          }
        },
        {
          "flavor_text": "It can take down\nany opponent with\nits powerful poi­\fson stingers. It\nsometimes attacks\nin swarms.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "gold",
            "url": "https://pokeapi.co/api/v2/version/4/"
          }
        },
        {
          "flavor_text": "It has three\npoison barbs.\nThe barb on its\ftail secretes the\nmost powerful\npoison.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "silver",
            "url": "https://pokeapi.co/api/v2/version/5/"
          }
        },
        {
          "flavor_text": "It uses sharp,\npoisonous stings\nto defeat prey,\fthen takes the\nvictim back to its\nnest for food.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version/6/"
          }
        },
        {
          "flavor_text": "BEEDRILL is extremely territorial.\nNo one should ever approach its nest -\nthis is for their own safety.\fIf angered, they will attack in a furious\nswarm.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "ruby",
            "url": "https://pokeapi.co/api/v2/version/7/"
          }
        },
        {
          "flavor_text": "BEEDRILL is extremely territorial.\nNo one should ever approach its nest -\nthis is for their own safety.\fIf angered, they will attack in a furious\nswarm.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sapphire",
            "url": "https://pokeapi.co/api/v2/version/8/"
          }
        },
        {
          "flavor_text": "A BEEDRILL is extremely territorial.\nFor safety reasons, no one should \never approach its nest. If angered,\nthey will attack in a swarm.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version/9/"
          }
        },
        {
          "flavor_text": "May appear in a swarm. Flies at violent\nspeeds, all the while stabbing with the\ntoxic stinger on its rear.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "firered",
            "url": "https://pokeapi.co/api/v2/version/10/"
          }
        },
        {
          "flavor_text": "It flies at high speed and attacks using \nthe large venomous stingers on its\nforelegs and tail.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "leafgreen",
            "url": "https://pokeapi.co/api/v2/version/11/"
          }
        },
        {
          "flavor_text": "Its best attack involves flying\naround at high speed, striking with\npoison needles, then flying off.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "diamond",
            "url": "https://pokeapi.co/api/v2/version/12/"
          }
        },
        {
          "flavor_text": "Its best attack involves flying\naround at high speed, striking with\npoison needles, then flying off.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "pearl",
            "url": "https://pokeapi.co/api/v2/version/13/"
          }
        },
        {
          "flavor_text": "Its best attack involves flying\naround at high speed, striking with\npoison needles, then flying off.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version/14/"
          }
        },
        {
          "flavor_text": "It can take down any opponent with\nits powerful poison stingers.\nIt sometimes attacks in swarms.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "heartgold",
            "url": "https://pokeapi.co/api/v2/version/15/"
          }
        },
        {
          "flavor_text": "It has three poison barbs.\nThe barb on its tail secretes the\nmost powerful poison.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "soulsilver",
            "url": "https://pokeapi.co/api/v2/version/16/"
          }
        },
        {
          "flavor_text": "Il virevolte rapidement autour de\nl’ennemi et frappe de son dard\nempoisonné avant de décamper.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "Its best attack involves flying\naround at high speed, striking with\npoison needles, then flying off.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "Il virevolte rapidement autour de\nl’ennemi et frappe de son dard\nempoisonné avant de décamper.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "Its best attack involves flying\naround at high speed, striking with\npoison needles, then flying off.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "Its best attack involves flying\naround at high speed, striking with\npoison needles, then flying off.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black-2",
            "url": "https://pokeapi.co/api/v2/version/21/"
          }
        },
        {
          "flavor_text": "Its best attack involves flying\naround at high speed, striking with\npoison needles, then flying off.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white-2",
            "url": "https://pokeapi.co/api/v2/version/22/"
          }
        },
        {
          "flavor_text": "りょうてと　おしりにある　３ぼんの\nどくばりで　あいてを　さして　さして\nさしまくって　こうげきする。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "양손과 엉덩이에 있는 3개의\n독침으로 상대를 찌르고 찌르고\n또 찌르며 공격한다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Il se sert de ses trois aiguillons empoisonnés pour\nattaquer sans relâche ses adversaires.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Dieses Pokémon verfügt über drei Giftstachel.\nEs kann seine Gegner damit wiederholt stechen.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Tiene 3 aguijones venenosos en sus patas y cola.\nSuelen pinchar a sus enemigos repetidas veces.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Possiede tre aculei velenosi sulle zampe anteriori e\nsull’addome con cui punge i nemici ripetutamente.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "両手と　お尻にある　３本の　毒針で\n相手を　刺して　刺して\n刺しまくって　攻撃する。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "しゅうだんで　あらわれることもある。\nもうスピードで　とびまわり\nおしりの　どくばりで　さしまくる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "집단으로 나타나기도 한다.\n맹렬한 스피드로 날아\n엉덩이의 독침으로 마구 찌른다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "On le voit souvent voler dans un essaim. Il vole très\nrapidement, piquant sans cesse ses adversaires de\nson dard toxique.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Es kann in Schwärmen auftauchen. Während seines\nrasanten Fluges sticht es mit dem Giftstachel\nan seinem Hinterteil zu.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Puede aparecer en enjambres volando a gran\nvelocidad. Suele usar el venenoso aguijón inferior\npara atacar.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Si può trovare anche in sciami. Vola a incredibili\nvelocità, colpendo con il velenoso pungiglione\nsituato sull’addome.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "May appear in a swarm. Flies at violent speeds,\nall the while stabbing with the toxic stinger on\nits rear.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "集団で　現れることもある。\n猛スピードで　飛び回り\nお尻の　毒針で　刺しまくる。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "なわばりいしきが　とても　つよいので　スピアーの\nすみかには　ちかづかない　ほうが　みの　ためだ。\nおこると　しゅうだんで　おそって　くるぞ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "영역에 대한 집착이 매우 강해서 독침붕이\n사는 곳에는 가까이 가지 않는 것이 신상에 좋다.\n화나면 집단으로 습격해 온다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Dardargnan est extrêmement possessif. Il vaut mieux ne pas\ntoucher son nid si on veut éviter d’avoir des ennuis.\nLorsqu’ils sont en colère, ces Pokémon attaquent en masse.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Bibor sind sehr wehrhaft. Es sollte sich besser niemand\nihrem Nest nähern. Wenn man sie ärgert, greifen sie in\nSchwärmen an.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Los Beedrill defienden su territorio a toda costa. No es\nconveniente acercarse a su colmena, por seguridad. Si se\nles molesta, todo un enjambre atacará ferozmente.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Beedrill difende strenuamente il proprio territorio. Per ragioni\ndi sicurezza nessuno può avvicinarsi al suo nido. Se vengono\ndisturbati, questi Pokémon attaccano violentemente in sciami.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Beedrill is extremely territorial. No one should ever approach\nits nest—this is for their own safety. If angered, they will attack\nin a furious swarm.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "縄張り意識が　とても　強いので　スピアーの\nすみかには　近づかない　ほうが　身の　ためだ。\n怒ると　集団で　襲って　くるぞ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "なわばりいしきが　とても　つよいので　スピアーの\nすみかには　ちかづかない　ほうが　みの　ためだ。\nおこると　しゅうだんで　おそって　くるぞ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "영역에 대한 집착이 매우 강해서 독침붕이\n사는 곳에는 가까이 가지 않는 것이 신상에 좋다.\n화나면 집단으로 습격해 온다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Dardargnan est extrêmement possessif. Il vaut mieux ne pas\ntoucher son nid si on veut éviter d’avoir des ennuis.\nLorsqu’ils sont en colère, ces Pokémon attaquent en masse.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Bibor ist sehr wehrhaft. Es sollte sich besser niemand\nseinem Nest nähern. Wenn man sie ärgert, greifen sie in\nSchwärmen an.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Los Beedrill defienden su territorio a toda costa. No es\nconveniente acercarse a su colmena, por seguridad. Si se\nles molesta, todo un enjambre atacará ferozmente.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Beedrill difende strenuamente il proprio territorio. Per ragioni\ndi sicurezza nessuno può avvicinarsi al suo nido. Se vengono\ndisturbati, questi Pokémon attaccano violentemente in sciami.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Beedrill is extremely territorial. No one should ever approach\nits nest—this is for their own safety. If angered, they will attack\nin a furious swarm.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "縄張り意識が　とても　強いので　スピアーの\nすみかには　近づかない　ほうが　身の　ためだ。\n怒ると　集団で　襲って　くるぞ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "りょうてと　おしりにある　３ぼんの\nどくバリで　あいてを　さして\nさして　さしまくって　こうげきする。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "양손과 엉덩이에 있는 3개의\n독침으로 상대를 찌르고 찌르고\n또 찌르며 공격한다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "會用雙手和屁股上的\n３根毒針不斷猛刺\n來攻擊對手。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Il se sert de ses trois aiguillons empoisonnés\nsitués sur les pattes avant et l’abdomen pour\nattaquer sans relâche ses adversaires.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Es verfügt über insgesamt drei Giftstachel,\nzwei an den Armen und einen am Hinterleib,\nmit denen es seine Gegner wiederholt angreift.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Tiene tres aguijones venenosos, dos en las patas\nanteriores y uno en la parte baja del abdomen,\ncon los que ataca a sus enemigos una y otra vez.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Possiede tre aculei velenosi, due sulle zampe\nanteriori e uno sull’addome, con cui punge\nripetutamente i nemici.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "It has three poisonous stingers on its\nforelegs and its tail. They are used to jab\nits enemy repeatedly.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "両手と　お尻にある　３本の\n毒バリで　相手を　刺して\n刺して　刺しまくって　攻撃する。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "它会用双手和\n尾部的３根毒针\n反复刺伤敌人。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "りょうてと　おしりにある　３ぼんの\nどくバリで　あいてを　さして\nさして　さしまくって　こうげきする。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "양손과 엉덩이에 있는 3개의\n독침으로 상대를 찌르고 찌르고\n또 찌르며 공격한다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "會用雙手和屁股上的\n３根毒針不斷猛刺\n來攻擊對手。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Il se sert de ses trois aiguillons empoisonnés\nsitués sur les pattes avant et l’abdomen pour\nattaquer sans relâche ses adversaires.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Es verfügt über insgesamt drei Giftstachel,\nzwei an den Armen und einen am Hinterleib,\nmit denen es seine Gegner wiederholt angreift.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Tiene tres aguijones venenosos, dos en las patas\nanteriores y uno en la parte baja del abdomen,\ncon los que ataca a sus enemigos una y otra vez.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Possiede tre aculei velenosi, due sulle zampe\nanteriori e uno sull’addome, con cui punge\nripetutamente i nemici.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "It has three poisonous stingers on its\nforelegs and its tail. They are used to jab\nits enemy repeatedly.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "両手と　お尻にある　３本の\n毒バリで　相手を　刺して\n刺して　刺しまくって　攻撃する。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "它会用双手和\n尾部的３根毒针\n反复刺伤敌人。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        }
      ],
      "form_descriptions": [],
      "forms_switchable": True,
      "gender_rate": 4,
      "genera": [
        {
          "genus": "どくばちポケモン",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          }
        },
        {
          "genus": "독벌포켓몬",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          }
        },
        {
          "genus": "毒蜂寶可夢",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          }
        },
        {
          "genus": "Pokémon Guêpoison",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          }
        },
        {
          "genus": "Giftbiene",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        },
        {
          "genus": "Pokémon Abeja Veneno",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          }
        },
        {
          "genus": "Pokémon Velenape",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          }
        },
        {
          "genus": "Poison Bee Pokémon",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        },
        {
          "genus": "どくばちポケモン",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          }
        },
        {
          "genus": "毒蜂宝可梦",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          }
        }
      ],
      "generation": {
        "name": "generation-i",
        "url": "https://pokeapi.co/api/v2/generation/1/"
      },
      "growth_rate": {
        "name": "medium",
        "url": "https://pokeapi.co/api/v2/growth-rate/2/"
      },
      "habitat": {
        "name": "forest",
        "url": "https://pokeapi.co/api/v2/pokemon-habitat/2/"
      },
      "has_gender_differences": False,
      "hatch_counter": 15,
      "id": 15,
      "is_baby": False,
      "is_legendary": False,
      "is_mythical": False,
      "name": "beedrill",
      "names": [
        {
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "name": "スピアー"
        },
        {
          "language": {
            "name": "roomaji",
            "url": "https://pokeapi.co/api/v2/language/2/"
          },
          "name": "Spear"
        },
        {
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "name": "독침붕"
        },
        {
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "name": "大針蜂"
        },
        {
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "name": "Dardargnan"
        },
        {
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "name": "Bibor"
        },
        {
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "name": "Beedrill"
        },
        {
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "name": "Beedrill"
        },
        {
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "name": "Beedrill"
        },
        {
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "name": "スピアー"
        },
        {
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "name": "大针蜂"
        }
      ],
      "order": 15,
      "pal_park_encounters": [
        {
          "area": {
            "name": "forest",
            "url": "https://pokeapi.co/api/v2/pal-park-area/1/"
          },
          "base_score": 70,
          "rate": 20
        }
      ],
      "pokedex_numbers": [
        {
          "entry_number": 15,
          "pokedex": {
            "name": "national",
            "url": "https://pokeapi.co/api/v2/pokedex/1/"
          }
        },
        {
          "entry_number": 15,
          "pokedex": {
            "name": "kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/2/"
          }
        },
        {
          "entry_number": 29,
          "pokedex": {
            "name": "original-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/3/"
          }
        },
        {
          "entry_number": 29,
          "pokedex": {
            "name": "updated-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/7/"
          }
        },
        {
          "entry_number": 177,
          "pokedex": {
            "name": "conquest-gallery",
            "url": "https://pokeapi.co/api/v2/pokedex/11/"
          }
        },
        {
          "entry_number": 28,
          "pokedex": {
            "name": "kalos-central",
            "url": "https://pokeapi.co/api/v2/pokedex/12/"
          }
        },
        {
          "entry_number": 15,
          "pokedex": {
            "name": "letsgo-kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/26/"
          }
        }
      ],
      "shape": {
        "name": "bug-wings",
        "url": "https://pokeapi.co/api/v2/pokemon-shape/13/"
      },
      "varieties": [
        {
          "is_default": True,
          "pokemon": {
            "name": "beedrill",
            "url": "https://pokeapi.co/api/v2/pokemon/15/"
          }
        },
        {
          "is_default": False,
          "pokemon": {
            "name": "beedrill-mega",
            "url": "https://pokeapi.co/api/v2/pokemon/10090/"
          }
        }
      ]
    },
    {
      "base_happiness": 70,
      "capture_rate": 255,
      "color": {
        "name": "brown",
        "url": "https://pokeapi.co/api/v2/pokemon-color/3/"
      },
      "egg_groups": [
        {
          "name": "flying",
          "url": "https://pokeapi.co/api/v2/egg-group/4/"
        }
      ],
      "evolution_chain": {
        "url": "https://pokeapi.co/api/v2/evolution-chain/6/"
      },
      "evolves_from_species": None,
      "flavor_text_entries": [
        {
          "flavor_text": "A common sight in\nforests and woods.\nIt flaps its\fwings at ground\nlevel to kick up\nblinding sand.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "red",
            "url": "https://pokeapi.co/api/v2/version/1/"
          }
        },
        {
          "flavor_text": "A common sight in\nforests and woods.\nIt flaps its\fwings at ground\nlevel to kick up\nblinding sand.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "blue",
            "url": "https://pokeapi.co/api/v2/version/2/"
          }
        },
        {
          "flavor_text": "Very docile. If\nattacked, it will\noften kick up\fsand to protect\nitself rather\nthan fight back.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version/3/"
          }
        },
        {
          "flavor_text": "It usually hides\nin tall grass. Be­\ncause it dislikes\ffighting, it pro­\ntects itself by\nkicking up sand.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "gold",
            "url": "https://pokeapi.co/api/v2/version/4/"
          }
        },
        {
          "flavor_text": "Common in grassy\nareas and forests,\nit is very docile\fand will chase off\nenemies by flap­\nping up sand.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "silver",
            "url": "https://pokeapi.co/api/v2/version/5/"
          }
        },
        {
          "flavor_text": "It rapidly flaps\nits wings in the\ngrass, stirring up\fa dust cloud that\ndrives insect prey\nout into the open.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version/6/"
          }
        },
        {
          "flavor_text": "PIDGEY has an extremely sharp sense\nof direction.\nIt is capable of unerringly returning\fhome to its nest, however far it may be\nremoved from its familiar surroundings.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "ruby",
            "url": "https://pokeapi.co/api/v2/version/7/"
          }
        },
        {
          "flavor_text": "PIDGEY has an extremely sharp sense\nof direction.\nIt is capable of unerringly returning\fhome to its nest, however far it may be\nremoved from its familiar surroundings.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sapphire",
            "url": "https://pokeapi.co/api/v2/version/8/"
          }
        },
        {
          "flavor_text": "It has an extremely sharp sense of\ndirection. It can unerringly return home to\nits nest, however far it may be removed\nfrom its familiar surroundings.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version/9/"
          }
        },
        {
          "flavor_text": "Does not like to fight. It hides in\ntall grass and so on, foraging for food\nsuch as small bugs.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "firered",
            "url": "https://pokeapi.co/api/v2/version/10/"
          }
        },
        {
          "flavor_text": "A common sight in forests and woods.\nIt flaps its wings at ground level to kick\nup blinding sand.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "leafgreen",
            "url": "https://pokeapi.co/api/v2/version/11/"
          }
        },
        {
          "flavor_text": "It is docile and prefers to avoid\nconflict. If disturbed, however,\nit can ferociously strike back.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "diamond",
            "url": "https://pokeapi.co/api/v2/version/12/"
          }
        },
        {
          "flavor_text": "It is docile and prefers to avoid\nconflict. If disturbed, however,\nit can ferociously strike back.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "pearl",
            "url": "https://pokeapi.co/api/v2/version/13/"
          }
        },
        {
          "flavor_text": "It is docile and prefers to avoid\nconflict. If disturbed, however,\nit can ferociously strike back.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version/14/"
          }
        },
        {
          "flavor_text": "It usually hides in tall grass.\nBecause it dislikes fighting,\nit protects itself by kicking up sand.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "heartgold",
            "url": "https://pokeapi.co/api/v2/version/15/"
          }
        },
        {
          "flavor_text": "Common in grassy areas and forests,\nit is very docile and will chase off\nenemies by flapping up sand.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "soulsilver",
            "url": "https://pokeapi.co/api/v2/version/16/"
          }
        },
        {
          "flavor_text": "Ce Pokémon docile préfère éviter\nle combat. Toutefois, il se montre\ntrès féroce quand on l’agresse.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "It is docile and prefers to avoid\nconflict. If disturbed, however,\nit can ferociously strike back.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "Ce Pokémon docile préfère éviter\nle combat. Toutefois, il se montre\ntrès féroce quand on l’agresse.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "It is docile and prefers to avoid\nconflict. If disturbed, however,\nit can ferociously strike back.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "It is docile and prefers to avoid\nconflict. If disturbed, however,\nit can ferociously strike back.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black-2",
            "url": "https://pokeapi.co/api/v2/version/21/"
          }
        },
        {
          "flavor_text": "It is docile and prefers to avoid\nconflict. If disturbed, however,\nit can ferociously strike back.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white-2",
            "url": "https://pokeapi.co/api/v2/version/22/"
          }
        },
        {
          "flavor_text": "もりや　はやしに　おおく　ぶんぷ。\nちじょうでも　はげしく　はばたいて\nすなを　かけたりする。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "숲이나 수풀에 많이 분포해 있다.\n땅에서도 격렬한 날갯짓으로\n모래를 뿌리기도 한다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "On l’aperçoit souvent dans les forêts. Avec ses ailes,\nil brasse l’air près du sol pour projeter du sable.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Ein vorwiegend in Wäldern lebendes Pokémon,\ndas zur Verteidigung mit den Flügeln Sand aufwirbelt.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Muy común en bosques y selvas. Aletea al nivel del\nsuelo para levantar la gravilla.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Molto comune in boschi e foreste, sbatte le ali a\nlivello del suolo per sollevare sabbia accecante.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "A common sight in forests and woods. It flaps\nits wings at ground level to kick up blinding sand.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "森や　林に　多く　分布。\n地上でも　激しく　はばたいて\n砂を　かけたりする。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "たたかいを　このまない　おとなしい\nせいかくだが　へたに　てを　だすと\nきょうれつに　はんげきされるぞ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "싸움을 좋아하지 않는 얌전한\n성격이지만 어설프게 건드리면\n강력한 반격을 당하게 된다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Ce Pokémon docile préfère éviter le combat.\nToutefois, il se montre très féroce quand on l’agresse.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Reizt man dieses an sich gutmütige Pokémon,\nwehrt es sich wütend.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Es manso y prefiere evitar los problemas. Sin embargo,\nsi le molestan atacará ferozmente.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "È docile e preferisce evitare i conflitti. Ma se viene\ndisturbato, contrattacca ferocemente.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "It is docile and prefers to avoid conflict.\nIf disturbed, however, it can ferociously strike back.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "戦いを　好まない　おとなしい\n性格だが　下手に　手を　出すと\n強烈に　反撃されるぞ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "ほうこう　かんかくに　とても　すぐれているので\nどんなに　はなれた　ばしょからでも　まよわずに\nじぶんの　す　まで　かえる　ことが　できる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "방향 감각이 매우 뛰어나서\n아무리 멀리 떨어진 곳에서도 헤매지 않고\n자신의 둥지까지 찾아 돌아올 수 있다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Roucool a un excellent sens de l’orientation. Il est capable de\nretrouver son nid sans jamais se tromper, même s’il est très\nloin de chez lui et dans un environnement qu’il ne connaît pas.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Taubsi verfügt über einen sehr geschulten Orientierungssinn.\nEs kehrt zielsicher zu seinem Nest zurück, egal, wie weit es\nsich von seiner gewohnten Umgebung entfernt hat.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Pidgey tiene un sentido de la orientación muy desarrollado.\nEs capaz de regresar a su nido, por lejos que se encuentre\nde las zonas que le resultan familiares.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Pidgey ha un senso dell’orientamento molto sviluppato.\nÈ sempre in grado di ritornare al suo nido, anche quando\nsi spinge molto lontano dal suo ambiente abituale.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Pidgey has an extremely sharp sense of direction. It is capable\nof unerringly returning home to its nest, however far it may be\nremoved from its familiar surroundings.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "方向　感覚に　とても　優れているので\nどんなに　離れた　場所からでも　迷わずに\n自分の　巣　まで　帰る　ことが　できる。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "ほうこう　かんかくに　とても　すぐれているので\nどんなに　はなれた　ばしょからでも　まよわずに\nじぶんの　す　まで　かえる　ことが　できる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "방향 감각이 매우 뛰어나서\n아무리 멀리 떨어진 곳에서도 헤매지 않고\n자신의 둥지까지 찾아 돌아올 수 있다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Roucool a un excellent sens de l’orientation. Il est capable de\nretrouver son nid sans jamais se tromper, même s’il est très\nloin de chez lui et dans un environnement qu’il ne connaît pas.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Taubsi verfügt über einen sehr geschulten Orientierungssinn.\nEs kehrt zielsicher zu seinem Nest zurück, egal, wie weit es\nsich von seiner gewohnten Umgebung entfernt hat.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Pidgey tiene un sentido de la orientación muy desarrollado.\nEs capaz de regresar a su nido, por lejos que se encuentre\nde las zonas que le resultan familiares.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Pidgey ha un senso dell’orientamento molto sviluppato.\nÈ sempre in grado di ritornare al suo nido, anche quando\nsi spinge molto lontano dal suo ambiente abituale.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Pidgey has an extremely sharp sense of direction.\nIt is capable of unerringly returning home to its nest,\nhowever far it may be removed from its familiar surroundings.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "方向　感覚に　とても　優れているので\nどんなに　離れた　場所からでも　迷わずに\n自分の　巣　まで　帰る　ことが　できる。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "おとなしい　せいかくで　おそわれても\nはんげき　せずに　すなを　かけて\nみを　まもることが　おおい。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "얌전한 성격이라 습격당해도\n반격하지 않고 모래를 뿌려서\n몸을 지키는 경우가 많다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "性情溫馴，即使遭到襲擊\n也很少反擊，只會朝對手\n潑沙子來保護自己。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "De nature très docile, il préfère projeter\ndu sable pour se défendre plutôt que\ncontre-attaquer.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Ein sanftmütiges Pokémon, welches lieber Sand\nzum Schutz aufwirbelt, als zurückzuschlagen.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Su docilidad es tal que suelen defenderse\nlevantando arena en lugar de contraatacar.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Di indole docile, preferisce gettare sabbia\nverso il nemico per proteggersi piuttosto\nche attaccarlo.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Very docile. If attacked, it will often kick up\nsand to protect itself rather than fight back.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "おとなしい　性格で　襲われても\n反撃　せずに　砂を　かけて\n身を　守ることが　多い。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "性格沉着冷静，即使受到\n攻击也很少反击，只会朝\n对手扬起沙子保护自己。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "おとなしい　せいかくで　おそわれても\nはんげき　せずに　すなを　かけて\nみを　まもることが　おおい。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "얌전한 성격이라 습격당해도\n반격하지 않고 모래를 뿌려서\n몸을 지키는 경우가 많다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "性情溫馴，即使遭到襲擊\n也很少反擊，只會朝對手\n潑沙子來保護自己。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "De nature très docile, il préfère projeter\ndu sable pour se défendre plutôt que\ncontre-attaquer.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Ein sanftmütiges Pokémon, welches lieber Sand\nzum Schutz aufwirbelt, als zurückzuschlagen.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Su docilidad es tal que suelen defenderse\nlevantando arena en lugar de contraatacar.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Di indole docile, preferisce gettare sabbia\nverso il nemico per proteggersi piuttosto\nche attaccarlo.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Very docile. If attacked, it will often kick up\nsand to protect itself rather than fight back.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "おとなしい　性格で　襲われても\n反撃　せずに　砂を　かけて\n身を　守ることが　多い。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "性格沉着冷静，即使受到\n攻击也很少反击，只会朝\n对手扬起沙子保护自己。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        }
      ],
      "form_descriptions": [],
      "forms_switchable": False,
      "gender_rate": 4,
      "genera": [
        {
          "genus": "ことりポケモン",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          }
        },
        {
          "genus": "아기새포켓몬",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          }
        },
        {
          "genus": "小鳥寶可夢",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          }
        },
        {
          "genus": "Pokémon Minoiseau",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          }
        },
        {
          "genus": "Kleinvogel",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        },
        {
          "genus": "Pokémon Pajarito",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          }
        },
        {
          "genus": "Pokémon Uccellino",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          }
        },
        {
          "genus": "Tiny Bird Pokémon",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        },
        {
          "genus": "ことりポケモン",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          }
        },
        {
          "genus": "小鸟宝可梦",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          }
        }
      ],
      "generation": {
        "name": "generation-i",
        "url": "https://pokeapi.co/api/v2/generation/1/"
      },
      "growth_rate": {
        "name": "medium-slow",
        "url": "https://pokeapi.co/api/v2/growth-rate/4/"
      },
      "habitat": {
        "name": "forest",
        "url": "https://pokeapi.co/api/v2/pokemon-habitat/2/"
      },
      "has_gender_differences": False,
      "hatch_counter": 15,
      "id": 16,
      "is_baby": False,
      "is_legendary": False,
      "is_mythical": False,
      "name": "pidgey",
      "names": [
        {
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "name": "ポッポ"
        },
        {
          "language": {
            "name": "roomaji",
            "url": "https://pokeapi.co/api/v2/language/2/"
          },
          "name": "Poppo"
        },
        {
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "name": "구구"
        },
        {
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "name": "波波"
        },
        {
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "name": "Roucool"
        },
        {
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "name": "Taubsi"
        },
        {
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "name": "Pidgey"
        },
        {
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "name": "Pidgey"
        },
        {
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "name": "Pidgey"
        },
        {
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "name": "ポッポ"
        },
        {
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "name": "波波"
        }
      ],
      "order": 16,
      "pal_park_encounters": [
        {
          "area": {
            "name": "field",
            "url": "https://pokeapi.co/api/v2/pal-park-area/2/"
          },
          "base_score": 30,
          "rate": 50
        }
      ],
      "pokedex_numbers": [
        {
          "entry_number": 16,
          "pokedex": {
            "name": "national",
            "url": "https://pokeapi.co/api/v2/pokedex/1/"
          }
        },
        {
          "entry_number": 16,
          "pokedex": {
            "name": "kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/2/"
          }
        },
        {
          "entry_number": 10,
          "pokedex": {
            "name": "original-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/3/"
          }
        },
        {
          "entry_number": 10,
          "pokedex": {
            "name": "updated-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/7/"
          }
        },
        {
          "entry_number": 17,
          "pokedex": {
            "name": "kalos-central",
            "url": "https://pokeapi.co/api/v2/pokedex/12/"
          }
        },
        {
          "entry_number": 16,
          "pokedex": {
            "name": "letsgo-kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/26/"
          }
        }
      ],
      "shape": {
        "name": "wings",
        "url": "https://pokeapi.co/api/v2/pokemon-shape/9/"
      },
      "varieties": [
        {
          "is_default": True,
          "pokemon": {
            "name": "pidgey",
            "url": "https://pokeapi.co/api/v2/pokemon/16/"
          }
        }
      ]
    },
    {
      "base_happiness": 70,
      "capture_rate": 120,
      "color": {
        "name": "brown",
        "url": "https://pokeapi.co/api/v2/pokemon-color/3/"
      },
      "egg_groups": [
        {
          "name": "flying",
          "url": "https://pokeapi.co/api/v2/egg-group/4/"
        }
      ],
      "evolution_chain": {
        "url": "https://pokeapi.co/api/v2/evolution-chain/6/"
      },
      "evolves_from_species": {
        "name": "pidgey",
        "url": "https://pokeapi.co/api/v2/pokemon-species/16/"
      },
      "flavor_text_entries": [
        {
          "flavor_text": "Very protective\nof its sprawling\nterritorial area,\fthis POKéMON will\nfiercely peck at\nany intruder.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "red",
            "url": "https://pokeapi.co/api/v2/version/1/"
          }
        },
        {
          "flavor_text": "Very protective\nof its sprawling\nterritorial area,\fthis POKéMON will\nfiercely peck at\nany intruder.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "blue",
            "url": "https://pokeapi.co/api/v2/version/2/"
          }
        },
        {
          "flavor_text": "This POKéMON is\nfull of vitality.\nIt constantly\fflies around its\nlarge territory in\nsearch of prey.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version/3/"
          }
        },
        {
          "flavor_text": "It has outstanding\nvision. However\nhigh it flies, it\fis able to distin­\nguish the move­\nments of its prey.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "gold",
            "url": "https://pokeapi.co/api/v2/version/4/"
          }
        },
        {
          "flavor_text": "It immobilizes its\nprey using well-\ndeveloped claws,\fthen carries the\nprey more than 60\nmiles to its nest.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "silver",
            "url": "https://pokeapi.co/api/v2/version/5/"
          }
        },
        {
          "flavor_text": "It slowly flies in\na circular pat­\ntern, all the\fwhile keeping a\nsharp lookout for\nprey.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version/6/"
          }
        },
        {
          "flavor_text": "PIDGEOTTO claims a large area as its\nown territory. This POKéMON flies\naround, patrolling its living space.\fIf its territory is violated, it shows\nno mercy in thoroughly punishing the\nfoe with its sharp claws.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "ruby",
            "url": "https://pokeapi.co/api/v2/version/7/"
          }
        },
        {
          "flavor_text": "PIDGEOTTO claims a large area as its\nown territory. This POKéMON flies\naround, patrolling its living space.\fIf its territory is violated, it shows\nno mercy in thoroughly punishing the\nfoe with its sharp claws.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sapphire",
            "url": "https://pokeapi.co/api/v2/version/8/"
          }
        },
        {
          "flavor_text": "This POKéMON flies around, patrolling its\nlarge territory. If its living space is\nviolated, it shows no mercy in thoroughly\npunishing the foe with its sharp claws.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version/9/"
          }
        },
        {
          "flavor_text": "The claws on its feet are well developed.\nIt can carry prey such as an EXEGGCUTE\nto its nest over 60 miles away.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "firered",
            "url": "https://pokeapi.co/api/v2/version/10/"
          }
        },
        {
          "flavor_text": "Very protective of its sprawling\nterritorial area, this POKéMON will\nfiercely peck at any intruder.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "leafgreen",
            "url": "https://pokeapi.co/api/v2/version/11/"
          }
        },
        {
          "flavor_text": "It flies over its wide territory in\nsearch of prey, downing it\nwith its highly developed claws.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "diamond",
            "url": "https://pokeapi.co/api/v2/version/12/"
          }
        },
        {
          "flavor_text": "It flies over its wide territory in\nsearch of prey, downing it\nwith its highly developed claws.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "pearl",
            "url": "https://pokeapi.co/api/v2/version/13/"
          }
        },
        {
          "flavor_text": "It flies over its wide territory in\nsearch of prey, downing it\nwith its highly developed claws.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version/14/"
          }
        },
        {
          "flavor_text": "It has outstanding vision. However\nhigh it flies, it is able to distinguish\nthe movements of its prey.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "heartgold",
            "url": "https://pokeapi.co/api/v2/version/15/"
          }
        },
        {
          "flavor_text": "It renders its prey immobile using \nwell-developed claws, then carries the\nprey more than 60 miles to its nest.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "soulsilver",
            "url": "https://pokeapi.co/api/v2/version/16/"
          }
        },
        {
          "flavor_text": "Il survole son vaste territoire en\nquête d’une proie avant de fondre\nsur elle toutes griffes en avant.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "It flies over its wide territory in\nsearch of prey, downing it\nwith its highly developed claws.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "Il survole son vaste territoire en\nquête d’une proie avant de fondre\nsur elle toutes griffes en avant.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "It flies over its wide territory in\nsearch of prey, downing it\nwith its highly developed claws.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "It flies over its wide territory in\nsearch of prey, downing it\nwith its highly developed claws.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black-2",
            "url": "https://pokeapi.co/api/v2/version/21/"
          }
        },
        {
          "flavor_text": "It flies over its wide territory in\nsearch of prey, downing it\nwith its highly developed claws.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white-2",
            "url": "https://pokeapi.co/api/v2/version/22/"
          }
        },
        {
          "flavor_text": "あしの　ツメが　はったつしている。\nエサの　タマタマを　つかんで\n１００キロさきの　す　まで　はこぶ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "발톱이 발달해 있다.\n먹이인 아라리를 잡아\n100km 떨어져 있는 둥지까지 나른다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Grâce à ses griffes très puissantes, il est capable\nde transporter des Noeunoeuf vers un nid éloigné\nde plus de 100 km.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Die Krallen an seinen Füßen sind sehr ausgeprägt.\nEs kann sogar ein Owei zu seinem Nest\nin 100 km Entfernung tragen.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Tiene unas garras desarrolladas. Puede atrapar un\nExeggcute y transportarlo desde una distancia de\ncasi 100 km.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Grazie ai potenti artigli può trasportare una preda\ndelle dimensioni di un Exeggcute per oltre 100 km.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "The claws on its feet are well developed.\nIt can carry prey such as an Exeggcute\nto its nest over 60 miles away.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "足の　ツメが　発達している。\nエサの　タマタマを　つかんで\n１００キロ先の　巣まで　運ぶ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "ひろい　なわばりを　もっており\nしんにゅうする　じゃまものは\nてっていてきに　つつかれてしまう。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "넓은 영역을 가지고 있어\n침입한 방해자는\n철저하게 쪼아버린다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Il protège son territoire avec ardeur et repousse à\ncoups de bec tout intrus.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Dieses Pokémon verteidigt sein abgegrenztes Areal\nsorgsam gegen alle Eindringlinge.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Muy protector de su amplio territorio, este Pokémon\npicoteará ferozmente a los intrusos.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Strenuo difensore del suo ampio territorio, becca\nferocemente ogni intruso.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Very protective of its sprawling territorial area,\nthis Pokémon will fiercely peck at any intruder.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "広い　縄張りを　持っており\n侵入する　邪魔者は\n徹底的に　つつかれてしまう。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "ひろい　なわばりを　とんで　みまわりを　する。\nなわばりを　あらす　あいては　ようしゃ　しない。\nするどい　ツメで　てっていてきに　こらしめるぞ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "넓은 영역을 날며 순찰한다.\n영역을 침범하는 상대는 용서하지 않는다.\n날카로운 발톱으로 철저히 혼내준다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Roucoups utilise une vaste surface pour son territoire.\nCe Pokémon surveille régulièrement son espace aérien.\nSi quelqu’un pénètre sur son territoire, il corrige l’ennemi\nsans pitié d’un coup de ses terribles serres.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Tauboga nennt ein großes Gebiet sein Eigen. Es fliegt\numher und kontrolliert seinen Lebensraum. Wenn jemand\nsein Gebiet betritt, zeigt es keine Gnade und greift seine\nGegner mit seinen scharfen Krallen an.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Pidgeotto se apodera de una zona muy vasta como su\nterritorio y la sobrevuela para controlarla. Si alguien invade\nsu espacio vital, no tendrá ningún reparo en castigarlo con\nsus afiladas garras.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Pidgeotto delimita come proprio un territorio immenso, che\ndifende controllandolo costantemente. Se tale territorio viene\ninvaso, questo Pokémon non ha pietà nel punire i nemici con\ni suoi artigli affilati.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Pidgeotto claims a large area as its own territory.\nThis Pokémon flies around, patrolling its living space.\nIf its territory is violated, it shows no mercy in thoroughly\npunishing the foe with its sharp claws.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "広い　縄張りを　飛んで　見まわりを　する。\n縄張りを　荒らす　相手は　容赦　しない。\n鋭い　ツメで　徹底的に　懲らしめるぞ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "ひろい　なわばりを　とんで　みまわりを　する。\nなわばりを　あらす　あいては　ようしゃ　しない。\nするどい　ツメで　てっていてきに　こらしめるぞ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "넓은 영역을 날며 순찰한다.\n영역을 침범하는 상대는 용서하지 않는다.\n날카로운 발톱으로 철저히 혼내준다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Roucoups utilise une vaste surface pour son territoire.\nCe Pokémon surveille régulièrement son espace aérien.\nSi quelqu’un pénètre sur son territoire, il corrige l’ennemi\nsans pitié d’un coup de ses terribles serres.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Tauboga nennt ein großes Gebiet sein Eigen. Es fliegt\numher und kontrolliert seinen Lebensraum. Wenn jemand\nsein Gebiet betritt, zeigt es keine Gnade und greift seine\nGegner mit seinen scharfen Krallen an.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Pidgeotto se apodera de una zona muy vasta como su\nterritorio y la sobrevuela para controlarla. Si alguien invade\nsu espacio vital, no tendrá ningún reparo en castigarlo con\nsus afiladas garras.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Pidgeotto delimita come proprio un territorio immenso, che\ndifende controllandolo costantemente. Se tale territorio viene\ninvaso, questo Pokémon non ha pietà nel punire i nemici con\ni suoi artigli affilati.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Pidgeotto claims a large area as its own territory. This\nPokémon flies around, patrolling its living space. If its territory\nis violated, it shows no mercy in thoroughly punishing the foe\nwith its sharp claws.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "広い　縄張りを　飛んで　見まわりを　する。\n縄張りを　荒らす　相手は　容赦　しない。\n鋭い　ツメで　徹底的に　懲らしめるぞ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "ありあまる　たいりょくの　もちぬしで\nひろい　なわばりを　とびまわり\nとおくまで　エサを　さがしにいく。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "어마어마한 체력의 소유자로\n넓은 영역을 날아다니며\n먼 곳까지 먹이를 찾으러 간다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "擁有著超乎尋常的體力，\n會在廣大的地盤裡四處飛行，\n到遠處去尋找食物。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Ce Pokémon est très endurant. Il survole\nen permanence son territoire pour chasser.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Dieses kraftvolle Pokémon wacht unermüdlich\nüber sein riesiges Territorium und fliegt weite\nStrecken auf der Suche nach Beute.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Su extraordinaria vitalidad y resistencia le\npermiten cubrir grandes distancias del territorio\nque habita en busca de presas.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Un Pokémon pieno di vitalità che vola\ninstancabile sul suo territorio in cerca di prede.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "This Pokémon is full of vitality. It constantly flies\naround its large territory in search of prey.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "あり余る　体力の　持ち主で\n広い　縄張りを　飛びまわり\n遠くまで　エサを　探しにいく。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "拥有超群的体力，而且\n飞翔范围广，经常飞到\n很远的地方寻找食物。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "ありあまる　たいりょくの　もちぬしで\nひろい　なわばりを　とびまわり\nとおくまで　エサを　さがしにいく。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "어마어마한 체력의 소유자로\n넓은 영역을 날아다니며\n먼 곳까지 먹이를 찾으러 간다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "擁有著超乎尋常的體力，\n會在廣大的地盤裡四處飛行，\n到遠處去尋找食物。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Ce Pokémon est très endurant. Il survole\nen permanence son territoire pour chasser.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Dieses kraftvolle Pokémon wacht unermüdlich\nüber sein riesiges Territorium und fliegt weite\nStrecken auf der Suche nach Beute.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Su extraordinaria vitalidad y resistencia le\npermiten cubrir grandes distancias del territorio\nque habita en busca de presas.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Un Pokémon pieno di vitalità che vola\ninstancabile sul suo territorio in cerca di prede.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "This Pokémon is full of vitality. It constantly flies\naround its large territory in search of prey.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "あり余る　体力の　持ち主で\n広い　縄張りを　飛びまわり\n遠くまで　エサを　探しにいく。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "拥有超群的体力，而且\n飞翔范围广，经常飞到\n很远的地方寻找食物。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        }
      ],
      "form_descriptions": [],
      "forms_switchable": False,
      "gender_rate": 4,
      "genera": [
        {
          "genus": "とりポケモン",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          }
        },
        {
          "genus": "새포켓몬",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          }
        },
        {
          "genus": "鳥寶可夢",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          }
        },
        {
          "genus": "Pokémon Oiseau",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          }
        },
        {
          "genus": "Vogel",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        },
        {
          "genus": "Pokémon Pájaro",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          }
        },
        {
          "genus": "Pokémon Uccello",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          }
        },
        {
          "genus": "Bird Pokémon",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        },
        {
          "genus": "とりポケモン",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          }
        },
        {
          "genus": "鸟宝可梦",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          }
        }
      ],
      "generation": {
        "name": "generation-i",
        "url": "https://pokeapi.co/api/v2/generation/1/"
      },
      "growth_rate": {
        "name": "medium-slow",
        "url": "https://pokeapi.co/api/v2/growth-rate/4/"
      },
      "habitat": {
        "name": "forest",
        "url": "https://pokeapi.co/api/v2/pokemon-habitat/2/"
      },
      "has_gender_differences": False,
      "hatch_counter": 15,
      "id": 17,
      "is_baby": False,
      "is_legendary": False,
      "is_mythical": False,
      "name": "pidgeotto",
      "names": [
        {
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "name": "ピジョン"
        },
        {
          "language": {
            "name": "roomaji",
            "url": "https://pokeapi.co/api/v2/language/2/"
          },
          "name": "Pigeon"
        },
        {
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "name": "피죤"
        },
        {
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "name": "比比鳥"
        },
        {
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "name": "Roucoups"
        },
        {
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "name": "Tauboga"
        },
        {
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "name": "Pidgeotto"
        },
        {
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "name": "Pidgeotto"
        },
        {
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "name": "Pidgeotto"
        },
        {
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "name": "ピジョン"
        },
        {
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "name": "比比鸟"
        }
      ],
      "order": 17,
      "pal_park_encounters": [
        {
          "area": {
            "name": "field",
            "url": "https://pokeapi.co/api/v2/pal-park-area/2/"
          },
          "base_score": 50,
          "rate": 30
        }
      ],
      "pokedex_numbers": [
        {
          "entry_number": 17,
          "pokedex": {
            "name": "national",
            "url": "https://pokeapi.co/api/v2/pokedex/1/"
          }
        },
        {
          "entry_number": 17,
          "pokedex": {
            "name": "kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/2/"
          }
        },
        {
          "entry_number": 11,
          "pokedex": {
            "name": "original-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/3/"
          }
        },
        {
          "entry_number": 11,
          "pokedex": {
            "name": "updated-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/7/"
          }
        },
        {
          "entry_number": 18,
          "pokedex": {
            "name": "kalos-central",
            "url": "https://pokeapi.co/api/v2/pokedex/12/"
          }
        },
        {
          "entry_number": 17,
          "pokedex": {
            "name": "letsgo-kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/26/"
          }
        }
      ],
      "shape": {
        "name": "wings",
        "url": "https://pokeapi.co/api/v2/pokemon-shape/9/"
      },
      "varieties": [
        {
          "is_default": True,
          "pokemon": {
            "name": "pidgeotto",
            "url": "https://pokeapi.co/api/v2/pokemon/17/"
          }
        }
      ]
    },
    {
      "base_happiness": 70,
      "capture_rate": 45,
      "color": {
        "name": "brown",
        "url": "https://pokeapi.co/api/v2/pokemon-color/3/"
      },
      "egg_groups": [
        {
          "name": "flying",
          "url": "https://pokeapi.co/api/v2/egg-group/4/"
        }
      ],
      "evolution_chain": {
        "url": "https://pokeapi.co/api/v2/evolution-chain/6/"
      },
      "evolves_from_species": {
        "name": "pidgeotto",
        "url": "https://pokeapi.co/api/v2/pokemon-species/17/"
      },
      "flavor_text_entries": [
        {
          "flavor_text": "When hunting, it\nskims the surface\nof water at high\fspeed to pick off\nunwary prey such\nas MAGIKARP.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "red",
            "url": "https://pokeapi.co/api/v2/version/1/"
          }
        },
        {
          "flavor_text": "When hunting, it\nskims the surface\nof water at high\fspeed to pick off\nunwary prey such\nas MAGIKARP.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "blue",
            "url": "https://pokeapi.co/api/v2/version/2/"
          }
        },
        {
          "flavor_text": "This POKéMON flies\nat Mach 2 speed,\nseeking prey.\fIts large talons\nare feared as\nwicked weapons.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version/3/"
          }
        },
        {
          "flavor_text": "Its well-developed\nchest muscles make\nit strong enough\fto whip up a gusty\nwindstorm with\njust a few flaps.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "gold",
            "url": "https://pokeapi.co/api/v2/version/4/"
          }
        },
        {
          "flavor_text": "It spreads its\nbeautiful wings\nwide to frighten\fits enemies. It\ncan fly at Mach 2\nspeed.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "silver",
            "url": "https://pokeapi.co/api/v2/version/5/"
          }
        },
        {
          "flavor_text": "Its outstanding\nvision allows it\nto spot splashing\fMAGIKARP, even\nwhile flying at\n3300 feet.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version/6/"
          }
        },
        {
          "flavor_text": "This POKéMON has a dazzling plumage of\nbeautifully glossy feathers.\nMany TRAINERS are captivated by the\fstriking beauty of the feathers on its\nhead, compelling them to choose PIDGEOT\nas their POKéMON.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "ruby",
            "url": "https://pokeapi.co/api/v2/version/7/"
          }
        },
        {
          "flavor_text": "This POKéMON has a dazzling plumage of\nbeautifully glossy feathers.\nMany TRAINERS are captivated by the\fstriking beauty of the feathers on its\nhead, compelling them to choose PIDGEOT\nas their POKéMON.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sapphire",
            "url": "https://pokeapi.co/api/v2/version/8/"
          }
        },
        {
          "flavor_text": "This POKéMON has gorgeous, glossy\nfeathers. Many TRAINERS are so captivated\nby the beautiful feathers on its head that\nthey choose PIDGEOT as their POKéMON.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version/9/"
          }
        },
        {
          "flavor_text": "It spreads its gorgeous wings widely to\nintimidate enemies. It races through the\nskies at Mach-2 speed.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "firered",
            "url": "https://pokeapi.co/api/v2/version/10/"
          }
        },
        {
          "flavor_text": "When hunting, it skims the surface of\nwater at high speed to pick off unwary\nprey such as MAGIKARP.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "leafgreen",
            "url": "https://pokeapi.co/api/v2/version/11/"
          }
        },
        {
          "flavor_text": "By flapping its wings with all its\nmight, PIDGEOT can make a gust of\nwind capable of bending tall trees.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "diamond",
            "url": "https://pokeapi.co/api/v2/version/12/"
          }
        },
        {
          "flavor_text": "By flapping its wings with all its\nmight, PIDGEOT can make a gust of\nwind capable of bending tall trees.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "pearl",
            "url": "https://pokeapi.co/api/v2/version/13/"
          }
        },
        {
          "flavor_text": "By flapping its wings with all its\nmight, PIDGEOT can make a gust of\nwind capable of bending tall trees.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version/14/"
          }
        },
        {
          "flavor_text": "Its well-developed chest muscles make\nit strong enough to whip up a gusty\nwindstorm with just a few flaps.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "heartgold",
            "url": "https://pokeapi.co/api/v2/version/15/"
          }
        },
        {
          "flavor_text": "It spreads its beautiful wings\nwide to frighten its enemies. It\ncan fly at Mach 2 speed.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "soulsilver",
            "url": "https://pokeapi.co/api/v2/version/16/"
          }
        },
        {
          "flavor_text": "En battant des ailes de toutes ses\nforces, Roucarnage génère une\nrafale à en déraciner les arbres.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "By flapping its wings with all its\nmight, Pidgeot can make a gust of\nwind capable of bending tall trees.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "En battant des ailes de toutes ses\nforces, Roucarnage génère une\nrafale à en déraciner les arbres.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "By flapping its wings with all its\nmight, Pidgeot can make a gust of\nwind capable of bending tall trees.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "By flapping its wings with all its\nmight, Pidgeot can make a gust of\nwind capable of bending tall trees.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black-2",
            "url": "https://pokeapi.co/api/v2/version/21/"
          }
        },
        {
          "flavor_text": "By flapping its wings with all its\nmight, Pidgeot can make a gust of\nwind capable of bending tall trees.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white-2",
            "url": "https://pokeapi.co/api/v2/version/22/"
          }
        },
        {
          "flavor_text": "エサを　さがすとき　すいめん\nすれすれを　すべるように　とんで\nコイキングなどを　わしづかみにする。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "먹이를 찾을 때 수면을\n아슬아슬하게 미끄러지듯 날아\n잉어킹 등을 움켜잡는다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Il survole la surface de l’eau pour repérer une proie\net plonge en piqué pour l’attraper.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Dieses Pokémon schnellt bei der Jagd blitzschnell\nunter Wasser, um seine ahnungslose Beute zu fangen.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Cuando caza, vuela muy deprisa a ras del agua y\nsorprende a inocentes presas como Magikarp.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Quando caccia, vola velocissimo sul pelo dell’acqua\ne cattura ignare prede come Magikarp.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "When hunting, it skims the surface of water\nat high speed to pick off unwary prey such\nas Magikarp.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "エサを　探すとき　水面　すれすれを\n滑るように　飛んで\nコイキングなどを　わしづかみにする。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "うつくしい　ハネを　ひろげて\nあいてを　いかくする。\nマッハ２で　そらを　とびまわる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "아름다운 날개를 펼쳐\n상대를 위협한다.\n마하2로 하늘을 날아다닌다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Roucarnage déploie ses ailes majestueuses pour\neffrayer ses ennemis. Il peut voler à Mach 2.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Es breitet seine betörenden Schwingen aus,\num den Gegner einzuschüchtern.\nSeine Fluggeschwindigkeit liegt bei Mach 2.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Para intimidar a su enemigo, extiende las increíbles\nalas que tiene. Este Pokémon vuela a una velocidad\nincreíble.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Intimidisce i nemici spiegando le possenti ali.\nIn volo raggiunge la velocità di Mach 2.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "It spreads its gorgeous wings widely to intimidate\nenemies. It races through the skies at\nMach-2 speed.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "美しい　羽を　広げて\n相手を　威嚇する。\nマッハ２で　空を　飛び回る。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "うつくしい　こうたくの　はねを　もつ　ポケモン。\nあたまの　はねの　うつくしさに　こころ　うばわれ\nピジョットを　そだてる　トレーナーも　おおい。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "아름답게 윤이 나는 깃털을 가진 포켓몬이다.\n머리 깃털의 아름다움에 마음을 빼앗겨\n피죤투를 기르는 트레이너도 많다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Ce Pokémon est doté d’un plumage magnifique et luisant.\nBien des Dresseurs sont captivés par la beauté fatale de\nsa huppe et décident de choisir Roucarnage comme leur\nPokémon favori.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Dieses Pokémon hat ein wunderschönes, glänzendes\nGefieder. Viele Trainer sind von der auffälligen Schönheit\nseines Federkleids begeistert, sodass sie Tauboss als ihr\nPokémon wählen.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "El plumaje de este Pokémon es bonito e hipnótico.\nMuchos Entrenadores se quedan embobados ante la belleza\nimpactante de las plumas que tiene en la cabeza; lo que les\nlleva a elegir a Pidgeot como su Pokémon.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Questo Pokémon è caratterizzato da uno stupendo piumaggio\ndai colori vivaci e brillanti. Molti Allenatori sono colpiti\ndall’evidente bellezza delle piume sulla testa. Per questo\nspesso scelgono Pidgeot come loro Pokémon.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "This Pokémon has a dazzling plumage of beautifully\nglossy feathers. Many Trainers are captivated by the\nstriking beauty of the feathers on its head, compelling\nthem to choose Pidgeot as their Pokémon.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "美しい　光沢の　羽を　持つ　ポケモン。\n頭の　羽の　美しさに　心　奪われ\nピジョットを　育てる　トレーナーも　多い。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "うつくしい　こうたくの　はねを　もつ　ポケモン。\nあたまの　はねの　うつくしさに　こころ　うばわれ\nピジョットを　そだてる　トレーナーも　おおい。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "아름답게 윤이 나는 깃털을 가진 포켓몬이다.\n머리 깃털의 아름다움에 마음을 빼앗겨\n피죤투를 기르는 트레이너도 많다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Ce Pokémon est doté d’un plumage magnifique et luisant.\nBien des Dresseurs sont captivés par la beauté fatale de\nsa huppe et décident de choisir Roucarnage comme leur\nPokémon favori.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Dieses Pokémon hat ein wunderschönes, glänzendes\nGefieder. Viele Trainer sind von der auffälligen Schönheit\nseines Federkleids begeistert, sodass sie Tauboss als ihr\nPokémon wählen.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "El plumaje de este Pokémon es bonito e hipnótico.\nMuchos Entrenadores se quedan embobados ante la belleza\nimpactante de las plumas que tiene en la cabeza; lo que les\nlleva a elegir a Pidgeot como su Pokémon.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Questo Pokémon è caratterizzato da uno stupendo piumaggio\ndai colori vivaci e brillanti. Molti Allenatori sono colpiti\ndall’evidente bellezza delle piume sulla testa. Per questo\nspesso scelgono Pidgeot come loro Pokémon.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "This Pokémon has a dazzling plumage of beautifully\nglossy feathers. Many Trainers are captivated by the\nstriking beauty of the feathers on its head, compelling\nthem to choose Pidgeot as their Pokémon.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "美しい　光沢の　羽を　持つ　ポケモン。\n頭の　羽の　美しさに　心　奪われ\nピジョットを　育てる　トレーナーも　多い。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "マッハ２で　ひこうし　エサをさがす。\nその　おおきな　ツメは　ぶきと\nしても　おそれられている。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "마하2의 속도로 비행하여 먹이를 찾는다.\n그 커다란 발톱은 무기로서도\n두려움의 대상이다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "會以２馬赫的速度飛行\n來尋找食物。巨大的爪子\n是很可怕的武器。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Ce Pokémon vole à Mach 2 quand il chasse.\nSes grandes serres sont des armes redoutables.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Auf der Jagd nach Beute fliegt es mit einer\nGeschwindigkeit von bis zu Mach 2. Seine\nmächtigen Klauen gelten als gefürchtete Waffen.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Este Pokémon vuela a una velocidad de 2 mach\nen busca de presas. Sus grandes garras son armas\nmuy peligrosas.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Può volare a una velocità di Mach 2 in cerca\ndi prede. I suoi artigli sono armi micidiali.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "This Pokémon flies at Mach 2 speed,\nseeking prey. Its large talons are feared\nas wicked weapons.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "マッハ２で　飛行し　エサを探す。\nその　大きな　ツメは　武器と\nしても　恐れられている。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "以２马赫的飞行速度来\n觅食。它巨大的爪子是\n非常令人惧怕的武器。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "マッハ２で　ひこうし　エサをさがす。\nその　おおきな　ツメは　ぶきと\nしても　おそれられている。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "마하2의 속도로 비행하여 먹이를 찾는다.\n그 커다란 발톱은 무기로서도\n두려움의 대상이다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "會以２馬赫的速度飛行\n來尋找食物。巨大的爪子\n是很可怕的武器。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Ce Pokémon vole à Mach 2 quand il chasse.\nSes grandes serres sont des armes redoutables.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Auf der Jagd nach Beute fliegt es mit einer\nGeschwindigkeit von bis zu Mach 2. Seine\nmächtigen Klauen gelten als gefürchtete Waffen.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Este Pokémon vuela a una velocidad de 2 mach\nen busca de presas. Sus grandes garras son armas\nmuy peligrosas.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Può volare a una velocità di Mach 2 in cerca\ndi prede. I suoi artigli sono armi micidiali.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "This Pokémon flies at Mach 2 speed,\nseeking prey. Its large talons are feared\nas wicked weapons.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "マッハ２で　飛行し　エサを探す。\nその　大きな　ツメは　武器と\nしても　恐れられている。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "以２马赫的飞行速度来\n觅食。它巨大的爪子是\n非常令人惧怕的武器。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        }
      ],
      "form_descriptions": [],
      "forms_switchable": True,
      "gender_rate": 4,
      "genera": [
        {
          "genus": "とりポケモン",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          }
        },
        {
          "genus": "새포켓몬",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          }
        },
        {
          "genus": "鳥寶可夢",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          }
        },
        {
          "genus": "Pokémon Oiseau",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          }
        },
        {
          "genus": "Vogel",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        },
        {
          "genus": "Pokémon Pájaro",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          }
        },
        {
          "genus": "Pokémon Uccello",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          }
        },
        {
          "genus": "Bird Pokémon",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        },
        {
          "genus": "とりポケモン",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          }
        },
        {
          "genus": "鸟宝可梦",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          }
        }
      ],
      "generation": {
        "name": "generation-i",
        "url": "https://pokeapi.co/api/v2/generation/1/"
      },
      "growth_rate": {
        "name": "medium-slow",
        "url": "https://pokeapi.co/api/v2/growth-rate/4/"
      },
      "habitat": {
        "name": "forest",
        "url": "https://pokeapi.co/api/v2/pokemon-habitat/2/"
      },
      "has_gender_differences": False,
      "hatch_counter": 15,
      "id": 18,
      "is_baby": False,
      "is_legendary": False,
      "is_mythical": False,
      "name": "pidgeot",
      "names": [
        {
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "name": "ピジョット"
        },
        {
          "language": {
            "name": "roomaji",
            "url": "https://pokeapi.co/api/v2/language/2/"
          },
          "name": "Pigeot"
        },
        {
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "name": "피죤투"
        },
        {
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "name": "大比鳥"
        },
        {
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "name": "Roucarnage"
        },
        {
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "name": "Tauboss"
        },
        {
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "name": "Pidgeot"
        },
        {
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "name": "Pidgeot"
        },
        {
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "name": "Pidgeot"
        },
        {
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "name": "ピジョット"
        },
        {
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "name": "大比鸟"
        }
      ],
      "order": 18,
      "pal_park_encounters": [
        {
          "area": {
            "name": "field",
            "url": "https://pokeapi.co/api/v2/pal-park-area/2/"
          },
          "base_score": 70,
          "rate": 20
        }
      ],
      "pokedex_numbers": [
        {
          "entry_number": 18,
          "pokedex": {
            "name": "national",
            "url": "https://pokeapi.co/api/v2/pokedex/1/"
          }
        },
        {
          "entry_number": 18,
          "pokedex": {
            "name": "kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/2/"
          }
        },
        {
          "entry_number": 12,
          "pokedex": {
            "name": "original-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/3/"
          }
        },
        {
          "entry_number": 12,
          "pokedex": {
            "name": "updated-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/7/"
          }
        },
        {
          "entry_number": 19,
          "pokedex": {
            "name": "kalos-central",
            "url": "https://pokeapi.co/api/v2/pokedex/12/"
          }
        },
        {
          "entry_number": 18,
          "pokedex": {
            "name": "letsgo-kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/26/"
          }
        }
      ],
      "shape": {
        "name": "wings",
        "url": "https://pokeapi.co/api/v2/pokemon-shape/9/"
      },
      "varieties": [
        {
          "is_default": True,
          "pokemon": {
            "name": "pidgeot",
            "url": "https://pokeapi.co/api/v2/pokemon/18/"
          }
        },
        {
          "is_default": False,
          "pokemon": {
            "name": "pidgeot-mega",
            "url": "https://pokeapi.co/api/v2/pokemon/10073/"
          }
        }
      ]
    },
    {
      "base_happiness": 70,
      "capture_rate": 255,
      "color": {
        "name": "purple",
        "url": "https://pokeapi.co/api/v2/pokemon-color/7/"
      },
      "egg_groups": [
        {
          "name": "ground",
          "url": "https://pokeapi.co/api/v2/egg-group/5/"
        }
      ],
      "evolution_chain": {
        "url": "https://pokeapi.co/api/v2/evolution-chain/7/"
      },
      "evolves_from_species": None,
      "flavor_text_entries": [
        {
          "flavor_text": "キバが２つ。とにかく　なんでも\nかじってみる。１ぴき　みつけたら\n４０ぴきは　そこに　すんでるはず。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Bites anything\nwhen it attacks.\nSmall and very\fquick, it is a\ncommon sight in\nmany places.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "red",
            "url": "https://pokeapi.co/api/v2/version/1/"
          }
        },
        {
          "flavor_text": "Bites anything\nwhen it attacks.\nSmall and very\fquick, it is a\ncommon sight in\nmany places.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "blue",
            "url": "https://pokeapi.co/api/v2/version/2/"
          }
        },
        {
          "flavor_text": "Will chew on any­\nthing with its\nfangs. If you see\fone, it is certain\nthat 40 more live\nin the area.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version/3/"
          }
        },
        {
          "flavor_text": "It eats anything.\nWherever food is\navailable, it will\fsettle down and\nproduce offspring\ncontinuously.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "gold",
            "url": "https://pokeapi.co/api/v2/version/4/"
          }
        },
        {
          "flavor_text": "Living wherever\nthere is food\navailable, it\fceaselessly scav­\nenges for edibles\nthe entire day.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "silver",
            "url": "https://pokeapi.co/api/v2/version/5/"
          }
        },
        {
          "flavor_text": "This POKéMON's\nimpressive vital­\nity allows it to\flive anywhere. It\nalso multiplies\nvery quickly.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version/6/"
          }
        },
        {
          "flavor_text": "RATTATA is cautious in the extreme.\nEven while it is asleep, it constantly\nlistens by moving its ears around.\fIt is not picky about where it lives -\nit will make its nest anywhere.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "ruby",
            "url": "https://pokeapi.co/api/v2/version/7/"
          }
        },
        {
          "flavor_text": "RATTATA is cautious in the extreme.\nEven while it is asleep, it constantly\nlistens by moving its ears around.\fIt is not picky about where it lives -\nit will make its nest anywhere.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sapphire",
            "url": "https://pokeapi.co/api/v2/version/8/"
          }
        },
        {
          "flavor_text": "A RATTATA is cautious in the extreme.\nEven while it is asleep, it constantly\nmoves its ears and listens for danger.\nIt will make its nest anywhere.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version/9/"
          }
        },
        {
          "flavor_text": "Its fangs are long and very sharp.\nThey grow continuously, so it gnaws on\nhard things to whittle them down.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "firered",
            "url": "https://pokeapi.co/api/v2/version/10/"
          }
        },
        {
          "flavor_text": "Bites anything when it attacks. Small and\nvery quick, it is a common sight in many\nplaces.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "leafgreen",
            "url": "https://pokeapi.co/api/v2/version/11/"
          }
        },
        {
          "flavor_text": "Cautious in the extreme, its\nhardy vitality lets it live in\nany kind of environment.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "diamond",
            "url": "https://pokeapi.co/api/v2/version/12/"
          }
        },
        {
          "flavor_text": "Cautious in the extreme, its\nhardy vitality lets it live in\nany kind of environment.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "pearl",
            "url": "https://pokeapi.co/api/v2/version/13/"
          }
        },
        {
          "flavor_text": "Cautious in the extreme, its\nhardy vitality lets it live in\nany kind of environment.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version/14/"
          }
        },
        {
          "flavor_text": "It eats anything. Wherever food is\navailable, it will settle down and\nproduce offspring continuously.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "heartgold",
            "url": "https://pokeapi.co/api/v2/version/15/"
          }
        },
        {
          "flavor_text": "Living wherever there is food\navailable, it ceaselessly scavenges\nfor edibles the entire day.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "soulsilver",
            "url": "https://pokeapi.co/api/v2/version/16/"
          }
        },
        {
          "flavor_text": "D’une prudence extrême, sa nature\nrobuste lui permet de s’adapter à\ntous les terrains.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "Cautious in the extreme, its\nhardy vitality lets it live in\nany kind of environment.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "D’une prudence extrême, sa nature\nrobuste lui permet de s’adapter à\ntous les terrains.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "Cautious in the extreme, its\nhardy vitality lets it live in\nany kind of environment.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "It searches for food all day. It gnaws\non hard objects to wear down its fangs,\nwhich grow constantly during its lifetime.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black-2",
            "url": "https://pokeapi.co/api/v2/version/21/"
          }
        },
        {
          "flavor_text": "It searches for food all day. It gnaws\non hard objects to wear down its fangs,\nwhich grow constantly during its lifetime.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white-2",
            "url": "https://pokeapi.co/api/v2/version/22/"
          }
        },
        {
          "flavor_text": "たべるものが　あるところなら\nどこにだって　せいそくする。\n１にちじゅう　エサを　さがしている。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "먹을 것이 있는 곳이라면\n어디서든 서식한다.\n온종일 먹이를 찾아다닌다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Vivant là où se trouve la nourriture, ce charognard\npasse ses journées à la rechercher.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Es baut sein Nest, wo es Futter findet. Es ist den\nganzen Tag auf der Suche nach etwas Essbarem.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Vive allí donde haya comida disponible. Busca todo\nel día, sin descanso, algo comestible.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Vive ovunque si trovi del cibo, cercando\nincessantemente qualsiasi cosa sia commestibile.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Living wherever there is food available,\nit ceaselessly scavenges for edibles\nthe entire day.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "食べるものが　あるところなら\nどこにだって　生息する。\n１日中　エサを　探している。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "キバは　ながくて　するどい。\nいっしょう　のびつづけるので\nかたい　モノを　かじって　けずる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "송곳니는 길고 날카롭다.\n평생 자라나기 때문에\n단단한 것을 갉아서 깎는다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Les dents de Rattata sont longues et tranchantes.\nComme elles poussent sans arrêt, il doit ronger tout\nce qu’il trouve pour pouvoir les tailler.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Seine Reißzähne sind lang und scharf. Da sie\nständig wachsen, nagt es immerzu an etwas,\num sie abzuwetzen.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Tiene unos largos y afilados colmillos que no dejan de\ncrecer. Le resultan muy útiles para destruir cosas.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "I denti affilati gli continuano a crescere, costringendolo\na limarseli mordicchiando oggetti molto duri.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Its fangs are long and very sharp. They grow\ncontinuously, so it gnaws on hard things to whittle\nthem down.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "キバは　長くて　鋭い。\n一生　伸び続けるので\n硬い　ものを　かじって　削る。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "けいかいしんが　とても　つよく　ねている　ときも\nみみを　うごかし　まわりの　おとを　きいている。\nどこにでも　すみつき　す　を　つくる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "경계심이 매우 강해서 자고 있을 때도\n귀를 움직여 주변의 소리를 듣고 있다.\n어디에든 자리를 잡고 둥지를 만든다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Rattata est extrêmement prudent. Même lorsqu’il est endormi,\nil fait pivoter ses oreilles pour écouter autour de lui.\nEn ce qui concerne son habitat, il n’est vraiment pas difficile.\nIl peut faire son nid n’importe où.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Rattfratz ist extrem vorsichtig. Sogar im Schlaf nimmt es\nalles wahr, indem es seine Ohren bewegt. Es stellt keine\ngroßen Ansprüche an seinen Lebensraum und richtet sein\nNest überall ein.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Rattata es cauto como él solo. Hasta cuando duerme mueve\nlas orejas para oír todos los ruidos. No es nada delicado a\nla hora de elegir su hábitat. Cualquier sitio es bueno para\ncavar su madriguera.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Rattata è estremamente cauto. Anche quando dorme tiene\nsempre le orecchie tese, muovendole come sonde. Non ha\nparticolari esigenze di habitat: costruisce la propria tana\novunque.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Rattata is cautious in the extreme. Even while it is asleep,\nit constantly listens by moving its ears around. It is not picky\nabout where it lives—it will make its nest anywhere.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "警戒心が　とても　強く　寝ている　ときも\n耳を　動かし　周りの　音を　聞いている。\nどこにでも　すみつき　巣　を　つくる。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "けいかいしんが　とても　つよく　ねている　ときも\nみみを　うごかし　まわりの　おとを　きいている。\nどこにでも　すみつき　す　を　つくる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "경계심이 매우 강해서 자고 있을 때도\n귀를 움직여 주변의 소리를 듣고 있다.\n어디에든 자리를 잡고 둥지를 만든다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Rattata est extrêmement prudent. Même lorsqu’il est endormi,\nil fait pivoter ses oreilles pour écouter autour de lui.\nEn ce qui concerne son habitat, il n’est vraiment pas difficile.\nIl peut faire son nid n’importe où.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Rattfratz ist extrem vorsichtig. Sogar im Schlaf nimmt es\nalles wahr, indem es seine Ohren bewegt. Es stellt keine\ngroßen Ansprüche an seinen Lebensraum und richtet sein\nNest überall ein.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "2개의 이빨로 뭐든지 일단\n갉고 본다. 1마리를 발견했다면\n그곳에 40마리는 살고 있을 것이다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Rattata es cauto como él solo. Hasta cuando duerme mueve\nlas orejas para oír todos los ruidos. No es nada delicado a\nla hora de elegir su hábitat. Cualquier sitio es bueno para\ncavar su madriguera.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Rattata è estremamente cauto. Anche quando dorme tiene\nsempre le orecchie tese, muovendole come sonde. Non ha\nparticolari esigenze di habitat: costruisce la propria tana\novunque.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Rattata is cautious in the extreme. Even while it is asleep,\nit constantly listens by moving its ears around. It is not\npicky about where it lives—it will make its nest anywhere.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "警戒心が　とても　強く　寝ている　ときも\n耳を　動かし　周りの　音を　聞いている。\nどこにでも　すみつき　巣　を　つくる。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "まえばは　しぬまで　のびつづけるので\nメンテナンスが　ひつよう。　ヤスリを\nよういしないと　はしらを　かじられる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "앞니는 죽을 때까지 계속 자라기 때문에\n관리가 필요하다. 이갈이 용품을\n준비하지 않으면 기둥을 갉는다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "門牙會終生生長，所以要隨時保養。\n不幫牠準備好銼刀的話，\n牠就會去咬柱子來磨牙。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "Il doit toujours prendre soin de ses incisives\ncar elles poussent sans arrêt. S’il n’a rien pour\nles limer, il se rabattra sur un pilier.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "Seine Nagezähne benötigen ständige Pflege, da\nsie sein ganzes Leben lang wachsen. Steht kein\nNagestein zur Verfügung, knabbert es an Holz.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "Debe cuidar regularmente sus incisivos, pues\nestos siguen creciendo hasta que muere. Si no\ntiene nada con qué afilarlos, suele roer pilares.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "I suoi incisivi non smettono mai di crescere e\nrichiedono continue cure. Se non gli viene data\nuna lima per regolarli, rosicchia i tavoli o altro.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "Its incisors continue growing until its death.\nIf its Trainer doesn’t offer it a file to gnaw on, it\nwill gnaw on door frames, table legs, and so on.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "前歯は　死ぬまで　伸び続けるので\nメンテナンスが　必要。　ヤスリを\n用意しないと　柱を　かじられる。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "门牙会终生生长，所以必须要保养。\n不准备好锉刀的话，会把柱子都啃掉。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "せいめいりょくが　つよく　きたない\nばしょでも　へいきで　くらす。\nほっておくと　どんどん　ふえていく。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "생명력이 강해서 더러운\n곳에서도 사는데 문제없다.\n내버려두면 점점 수가 불어난다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "生命力很強，\n即使在骯髒的地方也能安然生活。\n放任不管的話會不停繁殖。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "Un Pokémon très résistant, capable de survivre\nmême dans des milieux très insalubres.\nIl prolifère si l’on n’y prend pas garde.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "Sie strotzen vor Lebenskraft und können selbst\nan schmutzigen Orten problemlos überleben.\nBleiben sie ungestört, vermehren sie sich rasch.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "Su gran resistencia le permite vivir en los\nlugares más insalubres. Su población puede\ncrecer rápidamente.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "La sua straordinaria resistenza gli permette di\nadattarsi anche ad habitat insalubri. Se lasciato\nindisturbato, si riproduce in gran numero.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "With their strong capacity for survival, they can\nlive in dirty places without concern. Left\nunchecked, their numbers multiply rapidly.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "生命力が　強く　汚い\n場所でも　平気で　暮らす。\nほっておくと　どんどん　増えていく。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "生命力很强，\n即使在肮脏的地方也能坦然生活。\n放任不管的话会不停繁殖。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "いっしょう　まえばが　のびつづける。\nあまりに　のびすぎると　エサが\nたべられなくなって　がし　する。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "평생 앞니가 계속 자란다.\n너무 많이 자라면 먹이를\n먹을 수 없어 굶어 죽는다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "門牙會終生生長，\n如果長得太長，\n就會因為無法進食而餓死。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "Ses incisives poussent tout au long de sa vie.\nSi elles dépassent une certaine longueur,\nil ne peut plus s’alimenter et meurt de faim.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "Seine Nagezähne wachsen sein ganzes Leben\nüber. Werden sie allzu lang, kann es damit nicht\nmehr fressen und verhungert.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "Sus incisivos crecen durante toda su vida. Si\naumentan demasiado de tamaño, no puede\nalimentarse y muere de inanición.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "I suoi incisivi continuano a crescere per tutta\nla vita. Se si allungano troppo, non riesce più\na nutrirsi e muore di fame.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "Its incisors grow continuously throughout its life.\nIf its incisors get too long, this Pokémon\nbecomes unable to eat, and it starves to death.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "一生　前歯が　伸び続ける。\nあまりに　伸びすぎると　エサが\n食べられなくなって　餓死　する。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "门牙会终生生长。\n但要是长得太长，\n就会因无法进食而饿死。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "ありふれた　ポケモンだが　ちゅうい。\nするどい　まえばは　かたい\nざいもくさえ　かんたんに　へしおる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "흔한 포켓몬이지만 주의해야 한다.\n날카로운 앞니는 단단한 나무도\n간단하게 부러뜨린다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "雖然是常見的寶可夢，但還是要小心。\n銳利的門牙十分堅硬，\n就連木材也能輕易咬斷。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "Prenez garde à ce Pokémon très répandu :\nses puissantes incisives sont si acérées\nqu’elles peuvent couper des troncs d’arbre.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "Ein weitverbreitetes Pokémon, das nicht ganz\nungefährlich ist. Selbst hartes Holz zerkleinert\nes mit seinen scharfen Nagezähnen mühelos.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "Un Pokémon muy extendido con el que conviene\ntener cuidado ya que sus afilados incisivos son\ncapaces de roer maderas nobles sin problema.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "È un Pokémon molto comune con il quale è\nmeglio fare attenzione: con i suoi incisivi affilati\npuò tranciare anche un’asse di legno durissimo.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "This Pokémon is common but hazardous. Its\nsharp incisors can easily cut right through\nhard wood.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "ありふれた　ポケモンだが　注意。\n鋭い　前歯は　堅い\n材木さえ　簡単に　へしおる。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "虽是常见的宝可梦，但也不能掉以轻心。\n锋利的门牙甚至连坚硬的\n木材都能轻易咬断。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "長著２顆大牙，碰到什麼都會\n先咬上一口。只要看見１隻出沒，\n附近肯定還住著40隻以上。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Il peut ronger n’importe quoi avec ses\ndeux dents. Quand on en voit un, il y en\na certainement 40 dans le coin.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Es knabbert mit seinen zwei Nagezähnen alles\nund jeden an. Stößt man auf eines, findet man\nsicherlich 40 weitere in der Gegend.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Es propenso a hincar los incisivos en cualquier\ncosa que se le ponga por delante. Si se ve\nalguno, seguramente haya cuarenta cerca.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Con i suoi incisivi rode qualsiasi cosa.\nSe se ne avvista uno, è probabile che\nin zona vivano almeno 40 esemplari.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Will chew on anything with its fangs. If you\nsee one, you can be certain that 40 more\nlive in the area.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "キバが２つ。とにかく　なんでも\nかじってみる。１匹　見つけたら\n４０匹は　そこに　住んでるはず。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "有两颗大门牙，见什么咬什么。\n只要看到１只小拉达出没，\n附近肯定还住着40只以上。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "キバが２つ。とにかく　なんでも\nかじってみる。１ぴき　みつけたら\n４０ぴきは　そこに　すんでるはず。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "2개의 이빨로 뭐든지 일단\n갉고 본다. 1마리를 발견했다면\n그곳에 40마리는 살고 있을 것이다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "長著２顆大牙，碰到什麼都會\n先咬上一口。只要看見１隻出沒，\n附近肯定還住著40隻以上。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Il peut ronger n’importe quoi avec ses\ndeux dents. Quand on en voit un, il y en\na certainement 40 dans le coin.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Es knabbert mit seinen zwei Nagezähnen alles\nund jeden an. Stößt man auf eines, findet man\nsicherlich 40 weitere in der Gegend.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Es propenso a hincar los incisivos en cualquier\ncosa que se le ponga por delante. Si se ve\nalguno, seguramente haya cuarenta cerca.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Con i suoi incisivi rode qualsiasi cosa.\nSe se ne avvista uno, è probabile che\nin zona vivano almeno 40 esemplari.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Will chew on anything with its fangs. If you\nsee one, you can be certain that 40 more\nlive in the area.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "キバが２つ。とにかく　なんでも\nかじってみる。１匹　見つけたら\n４０匹は　そこに　住んでるはず。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "有两颗大门牙，见什么咬什么。\n只要看到１只小拉达出没，\n附近肯定还住着40只以上。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        }
      ],
      "form_descriptions": [],
      "forms_switchable": False,
      "gender_rate": 4,
      "genera": [
        {
          "genus": "ねずみポケモン",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          }
        },
        {
          "genus": "쥐포켓몬",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          }
        },
        {
          "genus": "鼠寶可夢",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          }
        },
        {
          "genus": "Pokémon Souris",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          }
        },
        {
          "genus": "Maus",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        },
        {
          "genus": "Pokémon Ratón",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          }
        },
        {
          "genus": "Pokémon Topo",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          }
        },
        {
          "genus": "Mouse Pokémon",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        },
        {
          "genus": "ねずみポケモン",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          }
        },
        {
          "genus": "鼠宝可梦",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          }
        }
      ],
      "generation": {
        "name": "generation-i",
        "url": "https://pokeapi.co/api/v2/generation/1/"
      },
      "growth_rate": {
        "name": "medium",
        "url": "https://pokeapi.co/api/v2/growth-rate/2/"
      },
      "habitat": {
        "name": "grassland",
        "url": "https://pokeapi.co/api/v2/pokemon-habitat/3/"
      },
      "has_gender_differences": True,
      "hatch_counter": 15,
      "id": 19,
      "is_baby": False,
      "is_legendary": False,
      "is_mythical": False,
      "name": "rattata",
      "names": [
        {
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "name": "コラッタ"
        },
        {
          "language": {
            "name": "roomaji",
            "url": "https://pokeapi.co/api/v2/language/2/"
          },
          "name": "Koratta"
        },
        {
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "name": "꼬렛"
        },
        {
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "name": "小拉達"
        },
        {
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "name": "Rattata"
        },
        {
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "name": "Rattfratz"
        },
        {
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "name": "Rattata"
        },
        {
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "name": "Rattata"
        },
        {
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "name": "Rattata"
        },
        {
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "name": "コラッタ"
        },
        {
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "name": "小拉达"
        }
      ],
      "order": 19,
      "pal_park_encounters": [
        {
          "area": {
            "name": "field",
            "url": "https://pokeapi.co/api/v2/pal-park-area/2/"
          },
          "base_score": 30,
          "rate": 50
        }
      ],
      "pokedex_numbers": [
        {
          "entry_number": 19,
          "pokedex": {
            "name": "national",
            "url": "https://pokeapi.co/api/v2/pokedex/1/"
          }
        },
        {
          "entry_number": 19,
          "pokedex": {
            "name": "kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/2/"
          }
        },
        {
          "entry_number": 17,
          "pokedex": {
            "name": "original-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/3/"
          }
        },
        {
          "entry_number": 17,
          "pokedex": {
            "name": "updated-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/7/"
          }
        },
        {
          "entry_number": 59,
          "pokedex": {
            "name": "updated-unova",
            "url": "https://pokeapi.co/api/v2/pokedex/9/"
          }
        },
        {
          "entry_number": 15,
          "pokedex": {
            "name": "original-alola",
            "url": "https://pokeapi.co/api/v2/pokedex/16/"
          }
        },
        {
          "entry_number": 15,
          "pokedex": {
            "name": "original-melemele",
            "url": "https://pokeapi.co/api/v2/pokedex/17/"
          }
        },
        {
          "entry_number": 6,
          "pokedex": {
            "name": "original-akala",
            "url": "https://pokeapi.co/api/v2/pokedex/18/"
          }
        },
        {
          "entry_number": 6,
          "pokedex": {
            "name": "original-ulaula",
            "url": "https://pokeapi.co/api/v2/pokedex/19/"
          }
        },
        {
          "entry_number": 6,
          "pokedex": {
            "name": "original-poni",
            "url": "https://pokeapi.co/api/v2/pokedex/20/"
          }
        },
        {
          "entry_number": 15,
          "pokedex": {
            "name": "updated-alola",
            "url": "https://pokeapi.co/api/v2/pokedex/21/"
          }
        },
        {
          "entry_number": 15,
          "pokedex": {
            "name": "updated-melemele",
            "url": "https://pokeapi.co/api/v2/pokedex/22/"
          }
        },
        {
          "entry_number": 6,
          "pokedex": {
            "name": "updated-akala",
            "url": "https://pokeapi.co/api/v2/pokedex/23/"
          }
        },
        {
          "entry_number": 6,
          "pokedex": {
            "name": "updated-ulaula",
            "url": "https://pokeapi.co/api/v2/pokedex/24/"
          }
        },
        {
          "entry_number": 6,
          "pokedex": {
            "name": "updated-poni",
            "url": "https://pokeapi.co/api/v2/pokedex/25/"
          }
        },
        {
          "entry_number": 19,
          "pokedex": {
            "name": "letsgo-kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/26/"
          }
        }
      ],
      "shape": {
        "name": "quadruped",
        "url": "https://pokeapi.co/api/v2/pokemon-shape/8/"
      },
      "varieties": [
        {
          "is_default": True,
          "pokemon": {
            "name": "rattata",
            "url": "https://pokeapi.co/api/v2/pokemon/19/"
          }
        },
        {
          "is_default": False,
          "pokemon": {
            "name": "rattata-alola",
            "url": "https://pokeapi.co/api/v2/pokemon/10091/"
          }
        }
      ]
    },
    {
      "base_happiness": 70,
      "capture_rate": 127,
      "color": {
        "name": "brown",
        "url": "https://pokeapi.co/api/v2/pokemon-color/3/"
      },
      "egg_groups": [
        {
          "name": "ground",
          "url": "https://pokeapi.co/api/v2/egg-group/5/"
        }
      ],
      "evolution_chain": {
        "url": "https://pokeapi.co/api/v2/evolution-chain/7/"
      },
      "evolves_from_species": {
        "name": "rattata",
        "url": "https://pokeapi.co/api/v2/pokemon-species/19/"
      },
      "flavor_text_entries": [
        {
          "flavor_text": "Ses pattes arrière lui permettent de traverser les\nrivières. Il est toujours en quête de nourriture.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "It uses its whis­\nkers to maintain\nits balance.\fIt apparently\nslows down if\nthey are cut off.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "red",
            "url": "https://pokeapi.co/api/v2/version/1/"
          }
        },
        {
          "flavor_text": "It uses its whis­\nkers to maintain\nits balance.\fIt apparently\nslows down if\nthey are cut off.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "blue",
            "url": "https://pokeapi.co/api/v2/version/2/"
          }
        },
        {
          "flavor_text": "Its hind feet are\nwebbed. They act\nas flippers, so\fit can swim in\nrivers and hunt\nfor prey.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version/3/"
          }
        },
        {
          "flavor_text": "Gnaws on anything\nwith its tough\nfangs. It can even\ftopple concrete\nbuildings by gnaw­\ning on them.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "gold",
            "url": "https://pokeapi.co/api/v2/version/4/"
          }
        },
        {
          "flavor_text": "Its whiskers help\nit to maintain\nbalance. Its fangs\fnever stop grow­\ning, so it gnaws\nto pare them down.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "silver",
            "url": "https://pokeapi.co/api/v2/version/5/"
          }
        },
        {
          "flavor_text": "The webs on its\nhind legs enable\nit to cross\frivers. It search­\nes wide areas for\nfood.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version/6/"
          }
        },
        {
          "flavor_text": "RATICATE’s sturdy fangs grow steadily.\nTo keep them ground down, it gnaws\non rocks and logs.\fIt may even chew on the walls of\nhouses.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "ruby",
            "url": "https://pokeapi.co/api/v2/version/7/"
          }
        },
        {
          "flavor_text": "RATICATE’s sturdy fangs grow steadily.\nTo keep them ground down, it gnaws\non rocks and logs.\fIt may even chew on the walls of\nhouses.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sapphire",
            "url": "https://pokeapi.co/api/v2/version/8/"
          }
        },
        {
          "flavor_text": "A RATICATE’s sturdy fangs grow steadily.\nTo keep them ground down, it gnaws on\nrocks and logs. It may even chew on the\nwalls of houses.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version/9/"
          }
        },
        {
          "flavor_text": "Its rear feet have three toes each.\nThey are webbed, enabling it to swim\nacross rivers.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "firered",
            "url": "https://pokeapi.co/api/v2/version/10/"
          }
        },
        {
          "flavor_text": "It uses its whiskers to maintain its\nbalance. It apparently slows down if\nthey are cut off.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "leafgreen",
            "url": "https://pokeapi.co/api/v2/version/11/"
          }
        },
        {
          "flavor_text": "It whittles its constantly growing\nfangs by gnawing on hard things.\nIt can chew apart cinder walls.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "diamond",
            "url": "https://pokeapi.co/api/v2/version/12/"
          }
        },
        {
          "flavor_text": "It whittles its constantly growing\nfangs by gnawing on hard things.\nIt can chew apart cinder walls.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "pearl",
            "url": "https://pokeapi.co/api/v2/version/13/"
          }
        },
        {
          "flavor_text": "It whittles its constantly growing\nfangs by gnawing on hard things.\nIt can chew apart cinder walls.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version/14/"
          }
        },
        {
          "flavor_text": "Gnaws on anything with its tough\nfangs. It can even topple concrete\nbuildings by gnawing on them.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "heartgold",
            "url": "https://pokeapi.co/api/v2/version/15/"
          }
        },
        {
          "flavor_text": "Its whiskers help it to maintain\nbalance. Its fangs never stop growing,\nso it gnaws to pare them down.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "soulsilver",
            "url": "https://pokeapi.co/api/v2/version/16/"
          }
        },
        {
          "flavor_text": "Il grignote sans cesse pour apaiser\nla poussée de ses crocs. Il peut\ntranspercer un mur de parpaings.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "It whittles its constantly growing\nfangs by gnawing on hard things.\nIt can chew apart cinder walls.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black",
            "url": "https://pokeapi.co/api/v2/version/17/"
          }
        },
        {
          "flavor_text": "Il grignote sans cesse pour apaiser\nla poussée de ses crocs. Il peut\ntranspercer un mur de parpaings.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "It whittles its constantly growing\nfangs by gnawing on hard things.\nIt can chew apart cinder walls.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white",
            "url": "https://pokeapi.co/api/v2/version/18/"
          }
        },
        {
          "flavor_text": "With its long fangs, this surprisingly\nviolent Pokémon can gnaw away\neven thick concrete with ease.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "black-2",
            "url": "https://pokeapi.co/api/v2/version/21/"
          }
        },
        {
          "flavor_text": "With its long fangs, this surprisingly\nviolent Pokémon can gnaw away\neven thick concrete with ease.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "white-2",
            "url": "https://pokeapi.co/api/v2/version/22/"
          }
        },
        {
          "flavor_text": "のびつづける　まえばを　けずるため\nかたい　ものを　かじる　しゅうせい。\nブロックべいも　かじって　こわす。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "계속 자라는 앞니를 갈아내려고\n딱딱한 것을 갉는 습성이 있다.\n벽돌로 된 벽도 갉아서 부순다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Il grignote sans cesse pour apaiser la poussée de ses\ncrocs. Il peut transpercer un mur de parpaings.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Es wetzt seine ständig wachsenden Zähne an\nharten Dingen. Es kann Wände aus Beton zernagen.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Lima sus colmillos royendo objetos duros. Con ellos\npuede destruir incluso paredes de hormigón.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "Si affila le zanne in perenne crescita rosicchiando\ncose dure. Riesce a frantumare persino i muri.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "It whittles its constantly growing fangs by gnawing\non hard things. It can chew apart cinder walls.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "伸び続ける　前歯を　削るため\n硬い　ものを　かじる　習性。\nブロック塀も　かじって　壊す。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "x",
            "url": "https://pokeapi.co/api/v2/version/23/"
          }
        },
        {
          "flavor_text": "うしろあしに　ついた　みずかきを\nつかって　かわをわたり　ひろい\nはんいで　エサを　さがしまわる。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "뒷다리에 달린 물갈퀴를\n사용하여 강을 건너 넓은\n범위에서 먹이를 찾아다닌다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Auf der Suche nach Nahrung kann es mit den\nSchwimmhäuten an seinen Hinterbeinen\nFlüsse durchqueren.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Con las membranas de las patas traseras, puede\natravesar ríos. Busca su alimento en zonas extensas.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "Attraversa i fiumi con le zampe posteriori palmate.\nPerlustra vaste aree cercando cibo.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "The webs on its hind legs enable it to cross rivers.\nIt searches wide areas for food.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "後ろ足に　ついた　水かきを　使って\n川を　渡り　広い　範囲で\nエサを　探し回る。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "y",
            "url": "https://pokeapi.co/api/v2/version/24/"
          }
        },
        {
          "flavor_text": "じょうぶな　キバは　どんどん　のびるので\nいわや　たいぼくを　かじって　けずっている。\nいえの　カベを　かじられる　ことも　あるよ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "튼튼한 이빨은 계속 자라기 때문에\n바위나 큰 나무를 갉아서 갈아낸다.\n집의 벽을 갉아 놓기도 한다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Les crocs robustes de Rattatac poussent constamment.\nPour éviter qu’ils raclent le sol, il se fait les dents sur\ndes cailloux ou des troncs d’arbre. Il lui arrive même\nde ronger les murs des maisons.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Rattikarls kräftige Zähne wachsen ständig. Deshalb nagt es\nunablässig Steine und Baumstämme an, um sie abzuwetzen.\nManchmal knabbert es sogar Hauswände an.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "A Raticate le crecen los incisivos firmes y fuertes.\nPara mantenerlos afilados roe troncos y rocas, e incluso\nlas paredes de las casas.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Le potenti zanne di Raticate crescono in continuazione.\nPer ridurne la crescita rode rocce e tronchi. Spesso si vedono\ni segni delle sue zanne anche sui muri delle case.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "Raticate’s sturdy fangs grow steadily. To keep them ground\ndown, it gnaws on rocks and logs. It may even chew on the\nwalls of houses.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "丈夫な　キバは　どんどん　伸びるので\n岩や　大木を　かじって　削っている。\n家の　カベを　かじられる　ことも　あるよ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "omega-ruby",
            "url": "https://pokeapi.co/api/v2/version/25/"
          }
        },
        {
          "flavor_text": "じょうぶな　キバは　どんどん　のびるので\nいわや　たいぼくを　かじって　けずっている。\nいえの　カベを　かじられる　ことも　あるよ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "튼튼한 이빨은 계속 자라기 때문에\n바위나 큰 나무를 갉아서 갈아낸다.\n집의 벽을 갉아 놓기도 한다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Les crocs robustes de Rattatac poussent constamment.\nPour éviter qu’ils raclent le sol, il se fait les dents sur\ndes cailloux ou des troncs d’arbre. Il lui arrive même\nde ronger les murs des maisons.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Rattikarls kräftige Zähne wachsen immer nach. Deshalb nagt\nes ständig Steine und Baumstämme an. Manchmal knabbert es\nsogar Hauswände an.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "A Raticate le crecen los incisivos firmes y fuertes.\nPara mantenerlos afilados roe troncos y rocas, e incluso\nlas paredes de las casas.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Le potenti zanne di Raticate crescono in continuazione.\nPer ridurne la crescita rode rocce e tronchi. Spesso si vedono\ni segni delle sue zanne anche sui muri delle case.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "Raticate’s sturdy fangs grow steadily. To keep them\nground down, it gnaws on rocks and logs. It may\neven chew on the walls of houses.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "丈夫な　キバは　どんどん　伸びるので\n岩や　大木を　かじって　削っている。\n家の　カベを　かじられる　ことも　あるよ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version/26/"
          }
        },
        {
          "flavor_text": "およぐのが　とくい。　うしろあしに\nちいさな　みずかきが　ついていて\nかわや　ときに　うみを　わたることも。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "수영이 특기. 뒷발에\n작은 물갈퀴가 달려있어\n강 때로는 바다를 건너기도 한다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "擅長游泳。後腳帶有小小的足蹼，\n會游過河流，有時還會渡過大海。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "C’est un très bon nageur. Les doigts de ses\npattes arrière sont palmés, ce qui lui permet de\ntraverser les rivières et parfois même les mers.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "Ein guter Schwimmer. An seinen Hinterläufen\nhat es Schwimmhäute, mit denen es Flüsse\nund manchmal sogar Meere durchquert.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "Es un excelente nadador. Gracias a las\npequeñas membranas de sus patas traseras\npuede cruzar ríos y, en ocasiones, hasta mares.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "Abile nuotatore, attraversa fiumi e a volte\npersino il mare grazie alle minuscole membrane\ntra le dita delle zampe posteriori.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "Its hind feet are webbed, so it’s a strong\nswimmer. It can cross rivers and sometimes\neven oceans.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "泳ぐのが　得意。　後ろ足に\n小さな　水かきが　ついていて\n河や　ときに　海を　渡ることも。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "游泳很在行。后脚带有小小的蹼，\n会渡过河流，有时还会渡过大海。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "sun",
            "url": "https://pokeapi.co/api/v2/version/27/"
          }
        },
        {
          "flavor_text": "みためよりも　ずっと　きょうぼうな\nせいしつ。　かおの　まえに　てを\nのばすと　かみちぎられる　かも。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "겉모습보다 훨씬 난폭한\n성질을 가졌다. 얼굴 앞에 손을\n내밀면 물어뜯길 수도 있다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "性格比外表看來殘暴得多。\n如果把手伸到牠面前，\n或許會被一口咬斷。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "Beaucoup plus agressif qu’il n’en a l’air, mieux\nvaut éviter de lui tendre la main si l’on veut la\nrécupérer entière.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "Es ist aggressiver, als sein Äußeres vermuten\nlässt. Hält man einen Finger vor sein Gesicht,\nmuss man damit rechnen, dass es hineinbeißt.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "No hay que dejarse engañar por su aspecto,\npues es más feroz de lo que parece. Si alguien\nintenta tocarlo, puede llevarse un mordisco.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "È molto più feroce di quanto non sembri.\nSe si allunga una mano verso di lui, potrebbe\nstaccarla con un morso.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "Its disposition is far more violent than its looks\nwould suggest. Don’t let your hand get too close\nto its face, as it could bite your hand clean off.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "見た目よりも　ずっと　凶暴な\n性質。　顔の　前に　手を\n伸ばすと　噛み千切られる　かも。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "性格比外表看起来凶残得多。\n如果把手伸到面前，\n或许会被一口咬断。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "moon",
            "url": "https://pokeapi.co/api/v2/version/28/"
          }
        },
        {
          "flavor_text": "うしろあしの　ちいさい　みずかきで\nうみを　およいで　しまを　わたり\nてきから　にげていた　という。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "뒷발의 작의 물갈퀴로\n바다를 헤엄쳐 섬을 건너\n적을 피해 도망쳤다고 한다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "據說牠為了躲避敵人，\n會用後腳的小蹼在海中游泳，\n渡海逃往別的島嶼。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "Les petites palmes de ses pattes postérieures\nlui permettraient de se rendre d’île en île\nà la nage afin d’échapper à ses prédateurs.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "Auf der Flucht vor seinen Feinden nutzt es die\nSchwimmhäute an seinen Hinterläufen, um von\nInsel zu Insel zu schwimmen.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "Las pequeñas membranas que tiene en las\npatas traseras le permiten nadar entre las islas\nde Alola y escapar así de sus depredadores.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "Si dice che sia sfuggito ai nemici nuotando da\nun’isola all’altra grazie alle minuscole membrane\ntra le dita delle zampe posteriori.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "People say that it fled from its enemies by\nusing its small webbed hind feet to swim\nfrom island to island in Alola.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "後ろ足の　小さい　水かきで\n海を　泳いで　島を　渡り\n敵から　逃げていた　という。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "据说会用后脚上小小的蹼\n泅水渡海，穿越岛屿\n来躲避敌人的追击。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "ultra-sun",
            "url": "https://pokeapi.co/api/v2/version/29/"
          }
        },
        {
          "flavor_text": "ヒゲは　バランスを　とる　たいせつな\nきかん。　どんなに　なかよくなっても\nさわられると　おこって　かみつく。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "수염은 밸런스를 잡기 위한 중요한\n기관이다. 아무리 친해져도\n만지면 화를 내며 문다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "鬍鬚是用來保持平衡的重要器官。\n就算感情再好，如果摸了牠的鬍鬚，\n牠都會生氣地咬過來。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "Il se sert de ses moustaches pour garder\nl’équilibre. Que le Rattatac soit apprivoisé\nou non, ne le touchez pas ou il vous mordrait !",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "Mit seinen Barthaaren hält es die Balance.\nBerührt man sie, wird es wütend und beißt zu,\negal, wie zutraulich es auch sein mag.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "Mantiene el equilibrio gracias a sus bigotes.\nAunque le coja confianza a alguien, uno puede\nllevarse un mordisco si intenta tocarlo.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "Usa i baffi per mantenersi in equilibrio.\nSe qualcuno li sfiora, si arrabbia e morde anche\nquelli a cui è molto affezionato.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "Its whiskers are essential for maintaining its\nbalance. No matter how friendly you are, it will\nget angry and bite you if you touch its whiskers.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "ヒゲは　バランスを　とる　大切な\n器官。　どんなに　仲良くなっても\n触られると　怒って　噛みつく。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "胡须是用来保持平衡的重要器官。\n即使感情再好，只要摸了它的胡须，\n它就会发火咬你。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "ultra-moon",
            "url": "https://pokeapi.co/api/v2/version/30/"
          }
        },
        {
          "flavor_text": "うしろあしにある　ちいさな　みずかきで\nかわを　およぐのは　みずのなかの\nエサを　とるためだ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "뒷다리에 달린 작은 물갈퀴로\n강을 헤엄치는 이유는 물속에 있는\n먹이를 잡기 위해서다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "為了取得水中的食物，\n牠會利用後腳上的小蹼\n在河裡游泳。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Ses pattes arrière sont palmées. Il peut donc\npoursuivre sa proie dans les cours d’eau et\nles rivières.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Die Hinterbeine dieses Pokémon verfügen über\nkleine Schwimmhäute. So kann es in Flüssen\njagen.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Gracias a las pequeñas membranas de las patas\ntraseras, puede nadar por los ríos para capturar\npresas.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Dispone di zampe posteriori palmate che\ngli permettono di nuotare nei fiumi in cerca\ndi prede.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "Its hind feet are webbed. They act as flippers,\nso it can swim in rivers and hunt for prey.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "後ろ足にある　小さな　水かきで\n川を　泳ぐのは　水の中の\nエサを　捕るためだ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "它的后脚上长着\n小蹼，以便它在\n水中游泳寻找食物。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-pikachu",
            "url": "https://pokeapi.co/api/v2/version/31/"
          }
        },
        {
          "flavor_text": "うしろあしにある　ちいさな　みずかきで\nかわを　およぐのは　みずのなかの\nエサを　とるためだ。",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "뒷다리에 달린 작은 물갈퀴로\n강을 헤엄치는 이유는 물속에 있는\n먹이를 잡기 위해서다.",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "為了取得水中的食物，\n牠會利用後腳上的小蹼\n在河裡游泳。",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Ses pattes arrière sont palmées. Il peut donc\npoursuivre sa proie dans les cours d’eau et\nles rivières.",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Die Hinterbeine dieses Pokémon verfügen über\nkleine Schwimmhäute. So kann es in Flüssen\njagen.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Gracias a las pequeñas membranas de las patas\ntraseras, puede nadar por los ríos para capturar\npresas.",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Dispone di zampe posteriori palmate che\ngli permettono di nuotare nei fiumi in cerca\ndi prede.",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "Its hind feet are webbed. They act as flippers,\nso it can swim in rivers and hunt for prey.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "後ろ足にある　小さな　水かきで\n川を　泳ぐのは　水の中の\nエサを　捕るためだ。",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        },
        {
          "flavor_text": "它的后脚上长着\n小蹼，以便它在\n水中游泳寻找食物。",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "version": {
            "name": "lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version/32/"
          }
        }
      ],
      "form_descriptions": [],
      "forms_switchable": False,
      "gender_rate": 4,
      "genera": [
        {
          "genus": "ねずみポケモン",
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          }
        },
        {
          "genus": "쥐포켓몬",
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          }
        },
        {
          "genus": "鼠寶可夢",
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          }
        },
        {
          "genus": "Pokémon Souris",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          }
        },
        {
          "genus": "Maus",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        },
        {
          "genus": "Pokémon Ratón",
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          }
        },
        {
          "genus": "Pokémon Topo",
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          }
        },
        {
          "genus": "Mouse Pokémon",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        },
        {
          "genus": "ねずみポケモン",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          }
        },
        {
          "genus": "鼠宝可梦",
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          }
        }
      ],
      "generation": {
        "name": "generation-i",
        "url": "https://pokeapi.co/api/v2/generation/1/"
      },
      "growth_rate": {
        "name": "medium",
        "url": "https://pokeapi.co/api/v2/growth-rate/2/"
      },
      "habitat": {
        "name": "grassland",
        "url": "https://pokeapi.co/api/v2/pokemon-habitat/3/"
      },
      "has_gender_differences": True,
      "hatch_counter": 15,
      "id": 20,
      "is_baby": False,
      "is_legendary": False,
      "is_mythical": False,
      "name": "raticate",
      "names": [
        {
          "language": {
            "name": "ja-Hrkt",
            "url": "https://pokeapi.co/api/v2/language/1/"
          },
          "name": "ラッタ"
        },
        {
          "language": {
            "name": "roomaji",
            "url": "https://pokeapi.co/api/v2/language/2/"
          },
          "name": "Ratta"
        },
        {
          "language": {
            "name": "ko",
            "url": "https://pokeapi.co/api/v2/language/3/"
          },
          "name": "레트라"
        },
        {
          "language": {
            "name": "zh-Hant",
            "url": "https://pokeapi.co/api/v2/language/4/"
          },
          "name": "拉達"
        },
        {
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          },
          "name": "Rattatac"
        },
        {
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          },
          "name": "Rattikarl"
        },
        {
          "language": {
            "name": "es",
            "url": "https://pokeapi.co/api/v2/language/7/"
          },
          "name": "Raticate"
        },
        {
          "language": {
            "name": "it",
            "url": "https://pokeapi.co/api/v2/language/8/"
          },
          "name": "Raticate"
        },
        {
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "name": "Raticate"
        },
        {
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "name": "ラッタ"
        },
        {
          "language": {
            "name": "zh-Hans",
            "url": "https://pokeapi.co/api/v2/language/12/"
          },
          "name": "拉达"
        }
      ],
      "order": 20,
      "pal_park_encounters": [
        {
          "area": {
            "name": "field",
            "url": "https://pokeapi.co/api/v2/pal-park-area/2/"
          },
          "base_score": 50,
          "rate": 30
        }
      ],
      "pokedex_numbers": [
        {
          "entry_number": 20,
          "pokedex": {
            "name": "national",
            "url": "https://pokeapi.co/api/v2/pokedex/1/"
          }
        },
        {
          "entry_number": 20,
          "pokedex": {
            "name": "kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/2/"
          }
        },
        {
          "entry_number": 18,
          "pokedex": {
            "name": "original-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/3/"
          }
        },
        {
          "entry_number": 18,
          "pokedex": {
            "name": "updated-johto",
            "url": "https://pokeapi.co/api/v2/pokedex/7/"
          }
        },
        {
          "entry_number": 60,
          "pokedex": {
            "name": "updated-unova",
            "url": "https://pokeapi.co/api/v2/pokedex/9/"
          }
        },
        {
          "entry_number": 16,
          "pokedex": {
            "name": "original-alola",
            "url": "https://pokeapi.co/api/v2/pokedex/16/"
          }
        },
        {
          "entry_number": 16,
          "pokedex": {
            "name": "original-melemele",
            "url": "https://pokeapi.co/api/v2/pokedex/17/"
          }
        },
        {
          "entry_number": 7,
          "pokedex": {
            "name": "original-akala",
            "url": "https://pokeapi.co/api/v2/pokedex/18/"
          }
        },
        {
          "entry_number": 7,
          "pokedex": {
            "name": "original-ulaula",
            "url": "https://pokeapi.co/api/v2/pokedex/19/"
          }
        },
        {
          "entry_number": 7,
          "pokedex": {
            "name": "original-poni",
            "url": "https://pokeapi.co/api/v2/pokedex/20/"
          }
        },
        {
          "entry_number": 16,
          "pokedex": {
            "name": "updated-alola",
            "url": "https://pokeapi.co/api/v2/pokedex/21/"
          }
        },
        {
          "entry_number": 16,
          "pokedex": {
            "name": "updated-melemele",
            "url": "https://pokeapi.co/api/v2/pokedex/22/"
          }
        },
        {
          "entry_number": 7,
          "pokedex": {
            "name": "updated-akala",
            "url": "https://pokeapi.co/api/v2/pokedex/23/"
          }
        },
        {
          "entry_number": 7,
          "pokedex": {
            "name": "updated-ulaula",
            "url": "https://pokeapi.co/api/v2/pokedex/24/"
          }
        },
        {
          "entry_number": 7,
          "pokedex": {
            "name": "updated-poni",
            "url": "https://pokeapi.co/api/v2/pokedex/25/"
          }
        },
        {
          "entry_number": 20,
          "pokedex": {
            "name": "letsgo-kanto",
            "url": "https://pokeapi.co/api/v2/pokedex/26/"
          }
        }
      ],
      "shape": {
        "name": "quadruped",
        "url": "https://pokeapi.co/api/v2/pokemon-shape/8/"
      },
      "varieties": [
        {
          "is_default": True,
          "pokemon": {
            "name": "raticate",
            "url": "https://pokeapi.co/api/v2/pokemon/20/"
          }
        },
        {
          "is_default": False,
          "pokemon": {
            "name": "raticate-alola",
            "url": "https://pokeapi.co/api/v2/pokemon/10092/"
          }
        },
        {
          "is_default": False,
          "pokemon": {
            "name": "raticate-totem-alola",
            "url": "https://pokeapi.co/api/v2/pokemon/10093/"
          }
        }
      ]
    }
]


@router.get("/species", response_model=PokemonList)
async def get_pokemon_list(count: PositiveInt = 20, index: Optional[PositiveInt] = None):
    base_url = "https://pokeapi.co/api/v2/pokemon-species"
    get_species_url = f"{base_url}?limit={count}&offset={index * count if index else 0}"

    client = HttpClient()
    data = await client.get(get_species_url)

    if data.get('error', None):
        raise HTTPException(status_code=500, detail=f"{base_url} {data['error']}")

    urls = [itm["url"] for itm in data["results"]]
    aggregated_response = await client.make_requests(urls)
    await client.close()

    species_computed = []
    for itm in aggregated_response:
        try:
            item = PokemonItem(
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
            detail = [i.strip() for i in str(e).split('\n')]
            raise HTTPException(status_code=500, detail=detail)

    return {"species": species_computed}

@router.post("/pokemon")
async def fetch_pokemon_details():
    return {"message": "Ok", "status": 200}
