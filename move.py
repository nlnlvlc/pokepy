from dataclasses import dataclass

@dataclass
class Move:
    name: str
    move_type: str
    pokemon_type: str
    damage: int = None
    multiturn: bool = False
    turns: int = 1

    def check_move_type(self):
        """
        Checks the move's type.
        Options:
        1. physical
        2. special
        :return: str representing move type
        """
        return self.move_type

    def check_pokemon_type(self):
        """
        Checks the pokemon type associated with move.
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
        return self.pokemon_type

    def check_damage(self):
        return self.damage

    def isMultiturn(self):
        return self.multiturn

    def last_turns(self):
        return self.turns

    def __repr__(self):
        return f"{self.name}"
