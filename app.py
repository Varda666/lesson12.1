from flask import Flask, request, render_template, send_from_directory, jsonify
from main.views import main_blueprint
from loader.views import loader_blueprint
import functions
import json
# from functions import ...

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint, url_prefix='/post')

@app.route("/")
def page_index():
   return main_blueprint

@app.route("/list/search/?s=поиск")
def page_tag():
    s = request.args.get("s").lower()
    data = functions.search_posts(s)
    return render_template("post_list.html", s=s, data=data)

@app.route("/post_form/", methods=["POST"])
def page_post_form():
    return render_template("post_form.html")


@app.route("/post_uploaded/", methods=["POST"])
def page_post_form():
    text = request.values['content']
    picture = request.files.get('picture')
    class NotInputError(Exception):
        def __init__(self, message=None):
            super().__init__(message)
    if text == "None":
        raise NotInputError("ошибка загрузки")
    elif picture == "None":
        raise NotInputError("ошибка загрузки")
    else:
        functions.upload_to_json_file()
        return render_template("post_uploaded.html", text=text, picture=picture)










@app.route("/post", methods=["GET", "POST"])
def page_post_form():
    pass

@app.route("/post", methods=["POST"])
def page_post_upload():
    pass


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

