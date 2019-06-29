from helper import PokerManager
from flask import Flask,  request
import json

app = Flask(__name__)

@app.route('/check_score', methods=['POST'])
def check_score():
    if request.method == 'POST':
        data = json.loads(request.data)
        poker = PokerManager(data)
        return poker.check_score()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')








# payload
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
