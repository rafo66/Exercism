# Score categories.
# Change the values as you see fit.
YACHT = "YACHT"
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"


def score(dice, category):
    """
    Score the given roll in the given category.
    Returns an integer score or None if the category cannot be scored.
    """
    if category == ONES:
        return dice.count(1)
    elif category == TWOS:
        return dice.count(2) * 2
    elif category == THREES:
        return dice.count(3) * 3
    elif category == FOURS:
        return dice.count(4) * 4
    elif category == FIVES:
        return dice.count(5) * 5
    elif category == SIXES:
        return dice.count(6) * 6
    elif category == FULL_HOUSE:
        for i in range(1, 7):
            if dice.count(i) == 3:
                return sum(dice)
        return 0

    elif category == FOUR_OF_A_KIND:
        
        # if all faces are the same
        if len(set(dice)) == 1:
            return 4 * dice[0]
            
        # if all faces but one are the same
        elif len(set(dice)) == 2:
            return sum([x for x in dice if dice.count(x) == 4])
        return 0

    elif category == LITTLE_STRAIGHT:
        if sorted(dice) == [1, 2, 3, 4, 5]:
            return 30
        return 0
    elif category == BIG_STRAIGHT:
        if sorted(dice) == [2, 3, 4, 5, 6]:
            return 30
        return 0
    elif category == CHOICE:
        return sum(dice)
    elif category == YACHT:
        if dice.count(dice[0]) == 5 or dice.count(dice[1]) == 5 or dice.count(dice[2]) == 5 or dice.count(dice[3]) == 5 or dice.count(dice[4]) == 5:
            return 50
        return 0
    return 0
