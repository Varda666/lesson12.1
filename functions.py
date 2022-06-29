from json import JSONDecodeError
import logging
from flask import Flask, request, render_template, send_from_directory, jsonify
import json
from pprint import pp

try:
    f = open("posts.json")
    data_ = json.load(f)
except FileNotFoundError:
    print('Файл posts.json отсутствует')
except JSONDecodeError:
    print('Файл posts.json не хочет превращаться в список')



def search_posts(s):
    posts_found = []
    if s in data_['content'].lower():
        posts_found.append(data_)
    logging.basicConfig(level=logging.INFO)
    logging.info("Поиск выполнен")
    return posts_found

def upload_to_json_file():
    data = {}
    data['text'] = request.values['content']
    data['picture'] = request.files.get('picture')
    with open("posts.json", "w") as write_file:
        json.dump(data, write_file)