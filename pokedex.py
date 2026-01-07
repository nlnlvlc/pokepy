from dataclasses import dataclass
from entry import PokedexEntry


@dataclass
class Pokedex:
    entries: dict[int, PokedexEntry] = {}
    region: str = None

    def __len__(self):
        return len(self.entries)

    def extract_pokemon(self, pokelist: list):

        print("Fetching Pokemon Data...")
        w = f"{BASE_URL}{species_query}"

        for poke in pokelist:
            entries = self.entries

            s = f'{poke["url"]}'
            _,_, res = s.partition(w)

            id = int(res[:-1].replace("/", ""))
            species = poke['name']
            url = poke['url']

            new_entry = PokedexEntry(id, species, url)

            if id not in entries.keys():
                add_pokedex_entry(id, new_entry)

        print("PokeServer data has been extracted.")

    def pull_entries(self):
        return self.entries

    def add_pokedex_entry(self, id: int, new_entry: PokedexEntry):
        self.entries[id] = new_entry

    def caught_pokemon(self, updated_entry: PokedexEntry):
        id = updated_entry.id
        curr = self.entries[id]

        if not curr.isCaught():
            curr.caught_pokemon()

    def new_description(self, descrip: str):
        pass

    def check_progress(self):
        caught = [poke for poke in self.entries.values() if poke.isCaught()]
        print(f"\nYou have caught {len(caught)} "
              f"out of {len(self.entries)} pokemon! \n")
        print(f"Pokemon caught: {', '.join([poke.species for poke in caught])}")
