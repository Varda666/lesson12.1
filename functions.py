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
    for post in data:
        if s.lower() in post['content'].lower():
            posts_found.append(post)
    logging.basicConfig(level=logging.INFO)
    logging.info("Поиск выполнен")
    return posts_found


def add_post(text, filename):
    posts = load_posts()
    posts.append({
        "content": text,
        "pic": f"/uploads/images/{filename}"
    })
    save_posts(posts)
