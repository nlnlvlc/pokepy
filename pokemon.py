from dataclasses import dataclass
from move import Move

@dataclass
class Pokemon:
    species: str
    nickname: str = species
    type_one: str = "???"
    type_two: str = None
    nature: str = None
    sex: str = None
    form: str = 'default'
    ability: str = None
    abilities: list = [None]
    lvl: int = 1
    exp: int = 0
    max_hp: int = 1
    hp: int = 1
    moves: dict(Move) = {None: False}
    moveset: list(Move) = [None]
    item: str = None
    shiny: bool = False
    egg_type: str = None
    fainted: bool = False

    def __repr__(self):
        return f"{self.nickname} ({self.species})"
    def check_moves(self):
        """
        Returns list of moves the pokemon can currently use
        :return:
        """
        return self.moves

    def check_equiped_moves(self):
        """
        Check moves pokemon currently has equipped for battle
        :return:
        """
        equiped = {key: value for key, value in self.moves if value}
        return equiped.keys()

    def equip_move(self, move: Move):
        """
        Adds a move to the list of move a pokemon can use in a battle
        :param move: move to be equipped
        :return:
        """

        equipped = {key: value for key, value in self.moves if value}

        if move in equipped.keys():
            print(f"{self.nickname} already has {move} equipped.\n")
            return

        if len(equipped) < 4:
            self.moves[move] = True
            print(f"{self.nickname} has equipped {move}. It can now be used in battle!\n")
        else:
            print(f"{self.nickname} already has 4 moves ready for battle.")
            decision = input(f"Do you want to replace a move with {move}? (Y/N)")

            if decision.lower() == "y":
                print("Current Moves:\n")
                for i in range(len(equipped)): print(f"{i}. {equipped[i]}\n")
                remove = input("Enter the number (0-3) of the move you want to remove or 'X' to cancel: ")

                if 0 <= int(remove) <= 3 :
                    self.unequip_move(equipped[i])
                    self.equip_move(move)
                else:
                    print(f"{self.nickname} didn't change moves.\n")
            else:
                print(f"{self.nickname} didn't change moves.\n")

    def unequip_move(self, move: Move):
        """
        Removes a move from the available moves a pokemon can use in battle
        :param move: move to be unequipped
        :return:
        """
        self.moves[move] = False
        print(f"{move} has been unequipped and can no longer be used in battle.\n")

    def learn_move(self, move: Move):
        """
        Adds a move to the number of moves a pokemon currently knows
        :param move: move to be learned
        :return:
        """
        if move not in self.moveset:
            print(f"{self.nickname} can't learn {move}")
            return

        if move in self.moves.keys():
            self.moves.update({move})
            print(f"{self.nickname} learned {move}")
        else:
            print(f"{self.nickname} already knows {move}")

    def set_sex(self, sex):
        """
        Sets the sex of a pokemon
        :param sex: male, female, or None
        :return:
        """
        self.sex = sex

    def set_form(self, form):
        """
        Sets form of the pokemon
        :param form:
        :return:
        """
        self.form = form

    def check_type(self):
        """
        Checks the type of the pokemon. If pokemon has two types, return both types
        Options:
        1. bug
        2. dark
        3. dragon
        4. electric
        5. fairy
        6. fighting
        7. fire
        8. flying
        9. ghost
        10. grass
        11. ground
        12. ice
        13. normal
        14. poison
        15. psychic
        16. rock
        17. steel
        18. water
        19. steller
        20. ???
        :return: str representing pokemon type
        """


        if self.type_one and self.type_two:
            return f"{self.type_one}/{self.type_two}"
        else:
            return self.type_one

    def set_type(self, typeOne, typeTwo = None):
        """
        Set typing(s) for pokemon
        Options:
        1. bug
        2. dark
        3. dragon
        4. electric
        5. fairy
        6. fighting
        7. fire
        8. flying
        9. ghost
        10. grass
        11. ground
        12. ice
        13. normal
        14. poison
        15. psychic
        16. rock
        17. steel
        18. water
        19. steller
        :param typeOne: primary type for pokemon
        :param typeTwo: optional secondary type of pokemon
        :return: None
        """
        pokemon_types = [
            "normal",
            "fire",
            "water",
            "grass",
            "electric",
            "ice",
            "fighting",
            "poison",
            "ground",
            "flying",
            "psychic",
            "bug",
            "rock",
            "ghost",
            "dragon",
            "steel",
            "dark",
            "fairy",
        ]
        if typeOne and typeOne in pokemon_types:
            self.type_one = typeOne

        if typeTwo and typeTwo in pokemon_types and typeOne != typeTwo:
            self.type_two

    def set_ability(self, ability):
        """
        Sets the pokemon's ability
        :param ability:
        :return:
        """
        self.ability = ability

    def set_abilities(self, abilities: list):
        """
        Sets possible abilities a pokeman can have based on species
        :param abilities:
        :return:
        """
        self.abilities = abilities

    def set_max_hp(self, hp: int):
        """
        Sets the max hp a pokemon can currently have
        :param hp:
        :return:
        """
        self.max_hp = hp

    def update_hp(self, hp: int):
        """
        Updates a pokemon's current hp
        :param hp:
        :return:
        """
        self.hp = hp

    def check_hp(self):
        """
        checks pokemon's current hp
        :return:
        """
        return self.hp

    def take_damage(self, damage: int):
        """
        Updates pokemon's hp after taking damage
        :param damage: damage pokemon is currently taking
        :return:
        """
        hp = self.check_hp()
        diff = hp - damage

        if diff < 0:
            self.update_hp(0)
            self.faints()
        else:
            self.update_hp(diff)

    def heal(self, buff: int):
        """
        Updates pokemon's hp to increase
        :param buff: amount to heal
        :return:
        """
        max_hp = self.max_hp
        hp = self.check_hp()
        gain = hp + buff

        if hp < 0:
            self.update_hp(max_hp if gain > max_hp else gain)
        else:
            print(f"{self.nickname} is fainted. Revive before healing.")

    def change_nickname(self, nickname):
        """
        Changes a pokemon's nickname
        :param nickname:
        :return:
        """
        old_name = self.nickname
        self.nickname = nickname

        print(f"{old_name} is now {self.nickname}")

    def check_specis(self):
        """
        Checks pokemon's species
        :return:
        """
        return self.species

    def faints(self):

        self.fainted = True

    def revive(self, buff: int):

        max_hp = self.max_hp

        #check if buff is larger than max allowable hp
        #if yes, update to max hp and unfaint
        self.update_hp(max_hp if buff > max_hp else buff)
        self.fainted = False






