from flask import Blueprint, render_template, request, current_app
import logging

from main.utils import PostsHandeler

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
logging.basicConfig(handlers=[logging.FileHandler(filename='basic.log', encoding='utf-8', mode='a+')], level=logging.INFO)


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search')
def search_page():
    substr = request.args.get('s', '')
    logging.info(f'Поиск: {substr}')
    post_handler = PostsHandeler(current_app.config['POST_PATH'])
    posts = post_handler.search_post(substr)

    return render_template('post_list.html', posts=posts, substr=substr)
