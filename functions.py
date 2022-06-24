from flask import Flask, request, render_template, send_from_directory, jsonify
import json
from pprint import pp

f = open("posts.json")
data = json.load(f)

def search_posts(s):
    posts_found = []
    if s in data['content'].lower():
        posts_found.append(data)
    return posts_found

