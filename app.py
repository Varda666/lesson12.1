from flask import Flask, request, render_template, send_from_directory, jsonify
from main.views import main_blueprint
from loader.views import loader_blueprint
import functions
import logging
import json
# from functions import ...

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

@app.route("/")
def page_index():
   return render_template('index.html')

@app.route("/uploads/post_form", methods=["POST"])
def page_post_form():
    return render_template("post_form.html")

@app.route("/uploads/post_uploaded", methods=["POST"])
def page_post_form_uploaded():
    picture = request.files.get('picture')
    if picture:
        ALLOWED_EXT = {'png', 'jpg'}
        filename = picture.filename
        extension = filename.split(".")[-1]
        if extension in ALLOWED_EXT:
            picture.save(f"./{picture.filename}")
            text = request.values['content']
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
        else:
            logging.basicConfig(level=logging.INFO)
            logging.info("Загруженный файл - не картинка")
            return f"Тип файлов {extension} не поддерживается"
    else:
        logging.basicConfig(level=logging.ERROR)
        logging.error("ошибка при загрузке файла")
        return f"Ошибка при загрузке файла"

app.route("/search/?s=поиск")
def page_tag():
    s = request.args.get("s").lower()
    data = functions.search_posts(s)
    return render_template("post_list.html", s=s, data=data)


app.run()

