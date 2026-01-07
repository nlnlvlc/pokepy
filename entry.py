from dataclasses import dataclass

@dataclass
class PokedexEntry:
    id: int
    species: str
    url: str
    region: str = None
    description: str = None
    bio: str = None
    sexes: list(str) = [None]
    forms: list(str) = [None]
    caught: bool = False

    def __repr__(self):
        return f"Pokemon No. {self.id}: {self.species}"

    def isCaught(self):
        return self.caught

    def caught_pokemon(self):
        if not self.caught:
            self.caught = True
