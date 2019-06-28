from helper import PokerManager
from flask import Flask,  request
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'


@app.route('/check_score', methods=['POST'])
def check_score():
    data = json.loads(request.data)
    poker = PokerManager(data)
    if request.method == 'POST':
        return poker.check_score()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')









# arr = [
#     {
#         "card": "4",
#         "type": 1
#     },
#     {
#         "card": "3",
#         "type": 2
#     },
#     {
#         "card": "3",
#         "type": 2
#     },
#     {
#         "card": "K",
#         "type": 2
#     },
#     {
#         "card": "K",
#         "type": 2
#     }
# ]


# poker = PokerManager(arr)

# print(poker.sorted_cards_indexes)
# print(poker._is_straight())
# print(poker._is_flush())
# print(poker._is_straight_flush())
# print(poker._is_royal_flush())
# print(poker._is_four_of_a_kind())
# print(poker._is_full_house())

# print(poker.check_score())

# print(poker._is_three_of_a_kind())
