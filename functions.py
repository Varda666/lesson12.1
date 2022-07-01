from json import JSONDecodeError
import logging
from flask import Flask, request, render_template, send_from_directory, jsonify
import json
from pprint import pp



def load_posts():
    try:
        with open("posts.json", 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print('Файл posts.json отсутствует')
    except JSONDecodeError:
        print('Файл posts.json не хочет превращаться в список')
    return data

def save_posts(data):
    with open("posts.json", 'w', encoding='utf-8') as f:
        json.dump(data, f)

def get_all_posts():
    data = load_posts()
    return data

def search_posts(s):
    data = load_posts()
    posts_found = []
    if s in data['content'].lower():
        posts_found.append(data)
    logging.basicConfig(level=logging.INFO)
    logging.info("Поиск выполнен")
    return posts_found

def add_post():
    data_ = {}
    data_['content'] = request.values['content']
    data_['pic'] = request.files.get('picture')
    with open("posts.json", "w") as write_file:
        json.dump(data_, write_file, indent=2)
    return data_