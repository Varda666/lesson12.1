from flask import Blueprint, render_template, request
loader_blueprint = Blueprint('loader_blueprint', __name__)

@loader_blueprint.route('/uploads')
def form_for_load_img():
    form_content = """
        <form action="/uploads" method="post" enctype="multipart/form-data">
            <input type="file" name="picture">
            <input type="submit" value="Отправить">
        </form>
        """
    return form_content

