from tkinter.font import names

import requests
import json
import os
import random

from entry import PokedexEntry
from pokedex import Pokedex
from pokemon import Pokemon

BASE_URL = "https://pokeapi.co/api/v2/"

species_query = "pokemon-species"
form_query = "pokemon"

def fetch_aux(param, queryType=None):
    exceptions = []
    if queryType is None:
        response = requests.get(f'https://pokeapi.co/api/v2/{param}?limit=100000&offset=0')
    else:
        response = requests.get(f'https://pokeapi.co/api/v2/{param}/{queryType}')

    if response.status_code == 200:
        return response.json()
    else:
        exceptions.append(Exception(f'Error fetching data from {param}, {response.status_code}'))

def find_pokemon(pokedex: Pokedex, name: str):
    """
    Finds the index position of a pokemon in the pokedex
    :param pokedex:
    :param name:
    :return: index if pokemon name is valid, else False
    """
    pokes = [ent for ent in pokedex.entries.values()]
    names = [poke.species for poke in pokes]

    if name.lower() in names:
        idx = names.index(name.lower)
        id = pokes[idx].id
        return pokedex.entries[id]
    else:
        print(f"{name} isn't a valid entry in Pokedex")
        return False

def new_pokedex():

    try:
        pokedex = Pokedex()
        print("New Pokedex Created\n"
              "Preparing Pokedex for connection...\n")
        response = fetch_aux(param)
        results = response['results']
        pokedex = pokedex.extract_pokemon(results)
        print("New Pokedex has been initialized. Good Luck, Trainer!\n")
        return pokedex
    except:
        print("Unable to generate new Pokedex")

def catch_pokemon(name: str, pokedex: Pokedex):

    try:
        if  name:
            curr = find_pokemon(pokedex, name)

            if curr:
                print(f"Catching a wild {name}...")
                if not curr.isCaught():
                    pokedex.caught_pokemon(curr)

                print(f"The wild {name} was successfully caught!")
                with open("pokedex.json", "w") as f:
                    json.dump(pokedex.entries, f)
            else:
                print((f"The wild {name} got away..."))
    except:
        print("Pokemon is uncatchable")

def check_party(pokedex):
    pass

def wild_encounter(pokedex):
    dex_size = len(pokedex)

    idx = random.randint(0,dex_size)

    species = pokedex[idx]['species']

    print(species)

    return Pokemon(species)

def release_pokemon(pokedex, name: str):
    idx = find_pokemon(pokedex, name)
    curr = pokedex[idx]

    if curr and curr["caught"]:
        print(f"You've release your {name}...\n"
              f"Good Luck, {name}...")
        curr["released"] = True

        pokedex[idx].update(curr)

        with open("pokedex.json", "w") as f:
            json.dump(pokedex, f)

    elif curr and curr["caught"]:
        print(f"You don't have any {name}s to release...")

def main():


    existing_pokedex = 'pokedex.json'
    if os.path.exists(existing_pokedex):
        with open(existing_pokedex) as json_file:
            pokedex = json.load(json_file)
        print("Pokedex log found and downloaded!")
    else:
        pokedex = new_pokedex()


    pokedex.check_progress(pokedex)

    for _ in range(10):
        wild = wild_encounter(pokedex)

        catch_pokemon(wild, pokedex, species_query)

        pokedex.check_progress(pokedex)
        


if __name__ == '__main__':
    main()