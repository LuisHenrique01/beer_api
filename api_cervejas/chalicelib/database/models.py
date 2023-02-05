from dataclasses import dataclass
from typing import List
from .base_models import Model


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

    def to_dict(self):
        self.amount = self.amount.to_dict()
        return super().to_dict()
    
    @classmethod
    def from_dict(cls, data: dict):
        data['amount'] = BoilVolume.from_dict(data['amount'])
        return super().from_dict(data)


@dataclass
class Malt(Model):
    name: str
    amount: BoilVolume

    def to_dict(self):
        self.amount = self.amount.to_dict()
        return super().to_dict()
    
    @classmethod
    def from_dict(cls, data: dict):
        data['amount'] = BoilVolume.from_dict(data['amount'])
        return super().from_dict(data)


@dataclass
class Ingredients(Model):
    malt: List[Malt]
    hops: List[Hop]
    yeast: str

    def to_dict(self):
        self.malt = list(map(lambda item: item.to_dict(), self.malt))
        self.hops = list(map(lambda item: item.to_dict(), self.hops))
        return super().to_dict()
    
    @classmethod
    def from_dict(cls, data: dict):
        data['malt'] = list(map(lambda item: Malt.from_dict(item), data['malt']))
        data['hops'] = list(map(lambda item: Hop.from_dict(item), data['hops']))
        return super().from_dict(data)


@dataclass
class Fermentation(Model):
    temp: BoilVolume

    def to_dict(self):
        self.temp = self.temp.to_dict()
        return super().to_dict()
    
    @classmethod
    def from_dict(cls, data: dict):
        data['temp'] = BoilVolume.from_dict(data['temp'])
        return super().from_dict(data)


@dataclass
class MashTemp(Model):
    temp: BoilVolume
    duration: int

    def to_dict(self):
        self.temp = self.temp.to_dict()
        return super().to_dict()
    
    @classmethod
    def from_dict(cls, data: dict):
        data['temp'] = BoilVolume.from_dict(data['temp'])
        return super().from_dict(data)


@dataclass
class Method(Model):
    mash_temp: List[MashTemp]
    fermentation: Fermentation
    twist: None

    def to_dict(self):
        self.mash_temp = list(map(lambda item: item.to_dict(), self.mash_temp))
        self.fermentation = self.fermentation.to_dict()
        return super().to_dict()
    
    @classmethod
    def from_dict(cls, data: dict):
        data['mash_temp'] = list(map(lambda item: MashTemp.from_dict(item), data['mash_temp']))
        data['fermentation'] = Fermentation.from_dict(data['fermentation'])
        return super().from_dict(data)


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

    def to_dict(self):
        self.volume = self.volume.to_dict()
        self.boil_volume = self.boil_volume.to_dict()
        self.method = self.method.to_dict()
        self.ingredients = self.ingredients.to_dict()
        return super().to_dict()
    
    @classmethod
    def from_dict(cls, data: dict):
        data['volume'] = BoilVolume.from_dict(data['volume'])
        data['boil_volume'] = BoilVolume.from_dict(data['boil_volume'])
        data['method'] = Method.from_dict(data['method'])
        data['ingredients'] = Ingredients.from_dict(data['ingredients'])
        return super().from_dict(data)
