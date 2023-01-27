from dataclasses import dataclass
from typing import List
from .models import Model


@dataclass
class BoilVolume(Model):
    value: float
    unit: str


@dataclass
class Hop(Model):
    name: str
    amount: BoilVolume
    add: str
    attribute: str


@dataclass
class Malt(Model):
    name: str
    amount: BoilVolume


@dataclass
class Ingredients(Model):
    malt: List[Malt]
    hops: List[Hop]
    yeast: str


@dataclass
class Fermentation(Model):
    temp: BoilVolume


@dataclass
class MashTemp(Model):
    temp: BoilVolume
    duration: int


@dataclass
class Method(Model):
    mash_temp: List[MashTemp]
    fermentation: Fermentation
    twist: None


@dataclass
class Brewery(Model):
    id: int
    name: str
    tagline: str
    first_brewed: str
    description: str
    image_url: str
    abv: float
    ibu: int
    target_fg: int
    target_og: int
    ebc: int
    srm: float
    ph: float
    attenuation_level: float
    volume: BoilVolume
    boil_volume: BoilVolume
    method: Method
    ingredients: Ingredients
    food_pairing: List[str]
    brewers_tips: str
    contributed_by: str
