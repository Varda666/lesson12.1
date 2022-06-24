from flask import Flask, jsonify, request

app = Flask(__name__)
# Чтобы заработала кириллица
app.config['JSON_AS_ASCII'] = False

books = [

    {"title": "Введение в Python", "price": 1400},
    {"title": "Python для новичков", "price": 2400},
    {"title": "Python  в схемах и мемах", "price": 1800}

]

@app.route("/")
def get_books_json():

    s = request.args.get("s")

    books_found = []

    for book in books:
        if s in book["title"].lower():
            books_found.append(book)

    return jsonify(books_found)

app.run()
