from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def page_form():
    """ Эта вьюшка показывает форму, которая отправляет файлы"""
    form_content = """
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="picture">
        <input type="submit" value="Отправить">
    </form>
    """
    return form_content

@app.route('/upload', methods=['POST'])
def page_upload():
    """ Эта вьюшка обрабатывает форму, вытаскивает из запроса файл и показывает его имя"""
    # Получаем объект картинки из формы
    picture = request.files("picture")
    return f"Загружен файл {picture.filename}"

app.run()
