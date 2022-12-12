from flask import Blueprint, render_template, request, current_app
import logging

from loader.utils import save_uploaded_picture
from main.utils import PostsHandeler

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename='basic.log', level=logging.INFO)


@loader_blueprint.route('/post')
def create_new_post_page():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def create_new_post_from_user_data_page():
    picture = request.files.get('picture')
    content = request.form.get('content')

    if not picture or not content:
        return 'Данные не получены'
    picture_path = save_uploaded_picture(picture)

    if not picture_path:
        logging.info(f'Файл {picture.filename}- не изображение')
        return 'Файл - не изображение'

    posts_handler = PostsHandeler(current_app.config['POST_PATH'])
    new_post = {'pic': picture_path, 'content': content}
    error = posts_handler.add_post(new_post)
    if error:
        logging.error(f'Ошибка загрузки поста: {error}')
        return 'Ошибка загрузки'

    return render_template('post_uploaded.html', picture_path=picture_path, content=content)
