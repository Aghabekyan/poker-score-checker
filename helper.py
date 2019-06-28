from collections import Counter

class PokerManager:
    _cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, hand_cards):
        self.hand_cards = hand_cards
        self.sorted_cards_indexes = sorted([self._cards.index(item['card']) for item in self.hand_cards])
        self.card_types = [item['type'] for item in self.hand_cards]

    def _is_straight(self):
        return self.sorted_cards_indexes == list(range(min(self.sorted_cards_indexes), max(self.sorted_cards_indexes)+1))

    def _is_flush(self):
        tmp_type = self.hand_cards[0]['type']
        for item in self.hand_cards:
            if tmp_type != item['type']:
                return False
        return True

    def _is_royal_flush(self):
        return self._is_straight() and self._is_flush() and self._cards[self.sorted_cards_indexes[-1]] == 'A'

    def _is_straight_flush(self):
        return self._is_straight() and self._is_flush()

    def _is_four_of_a_kind(self):
        ret_value = False
        for i in range(2):
            if self.sorted_cards_indexes.count(self.sorted_cards_indexes[0]) == 4:
                ret_value = True
        return ret_value

    def _is_full_house(self):
        grouped_indexes_dict = Counter(self.sorted_cards_indexes)
        grouped_indexes_list = [ [k,]*v for k,v in grouped_indexes_dict.items()]
        return len(grouped_indexes_list) == 2 and (len(grouped_indexes_list[0]) == 2 or len(grouped_indexes_list[0]) == 3)

    def _is_three_of_a_kind(self):
        grouped_indexes_dict = Counter(self.sorted_cards_indexes)
        grouped_indexes_list = [ [k,]*v for k,v in grouped_indexes_dict.items()]
        return len(grouped_indexes_list) > 2 and (len(grouped_indexes_list[0]) == 3 or
                                                  len(grouped_indexes_list[1]) == 3 or 
                                                  len(grouped_indexes_list[1]) == 3)

    def _is_pair(self):
        grouped_indexes_dict = Counter(self.sorted_cards_indexes)
        grouped_indexes_list = [ [k,]*v for k,v in grouped_indexes_dict.items()]
        return len(grouped_indexes_list) == 3

    def check_score(self):
        if self._is_royal_flush(): return 'Royal Flush'
        if self._is_straight_flush(): return 'Straight Flush'
        if self._is_four_of_a_kind(): return 'Four of a kind'
        if self._is_full_house(): return 'Full House'
        if self._is_flush(): return 'Flush'
        if self._is_straight(): return 'Straight'
        if self._is_three_of_a_kind(): return 'Three of a kind'
        if self._is_pair(): return 'Pair'
        return self._cards[self.sorted_cards_indexes[-1]]
