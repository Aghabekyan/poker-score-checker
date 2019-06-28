from helper import PokerManager

arr = [
    {
        "card": "4",
        "type": 1
    },
    {
        "card": "3",
        "type": 2
    },
    {
        "card": "3",
        "type": 2
    },
    {
        "card": "K",
        "type": 2
    },
    {
        "card": "K",
        "type": 2
    }
]


poker = PokerManager(arr)

print(poker.sorted_cards_indexes)
print(poker._is_straight())
print(poker._is_flush())
print(poker._is_straight_flush())
print(poker._is_royal_flush())
print(poker._is_kare())
print(poker._is_full_house())


print(poker.check_score())

print(poker._is_three_of_a_kind())
