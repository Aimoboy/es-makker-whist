from typing import List
from ..enums.call import Call

def get_call_sequence(starting_player: int) -> List[int]:
    players = [0, 1, 2, 3]
    return players[starting_player:] + players[:starting_player]



