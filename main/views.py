from flask import Blueprint, send_from_directory, request
main_blueprint = Blueprint('main_blueprint', __name__)

@main_blueprint.route('/uploads/picture')
def show_img():
    picture = request.files.get("picture")
    return picture



