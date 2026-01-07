from dataclasses import dataclass
from pokemon import Pokemon

@dataclass
class PokemonParty:
    party: list(Pokemon) = [None]
    pc: list(Pokemon) = [None]

    def add_to_party(self, poke: Pokemon):
        self.party.append(poke)
        print(f"{poke} has been added to your party!")

    def release_from_party(self):
        if not self.isPartyEmpty():
            idx = self.party.index(poke)
            self.party.pop(idx)

    def release_from_pc(self):
        if not self.isPcEmpty():
            idx = self.pc.index(poke)
            self.pc.pop(idx)

    def add_to_pc(self, poke: Pokemon):
        self.pc.append(poke)

    def transfer_to_party(self, poke: Pokemon):
        if not self.isPcEmpty() and not self.isPartyFull():
            idx = self.pc.index(poke)
            temp = self.pc.pop(idx)

            self.party.append(temp)
            print(f"{poke} has been transferred from your pc to your party")
        elif self.isPartyFull():
            print("You don't have any room in your party!")
        else:
            print("You don't have any pokemon to transfer!")

    def transfer_to_pc(self, poke: pokemon):
        if not self.isPartyEmpty():
            idx = self.party.index(poke)
            temp = self.party.pop(idx)

            self.pc.append(temp)
            print(f"{poke} has been transferred from your party to your pc")
        else:
            print("You don't have any pokemon to transfer!")

    def isPartyFull(self):
        return True if len(self.party) == 6 else False

    def isPcFull(self):
        pass

    def isPartyEmpty(self):
        return True if len(self.party) == 0 else False

    def isPcEmpty(self):
        return True if len(self.pc) == 0 else False