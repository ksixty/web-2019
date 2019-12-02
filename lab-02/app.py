from flask import Flask, render_template, request
from datetime import datetime
import copy
app = Flask(__name__)
application = app

MENU = [
    {"text": "Заглавие", "url": "/"},
    {"text": "GET-запросы", "url": "/get?foo=bar&baz=123"},
    {"text": "Печенье", "url": "/cookies"},
    {"text": "POST-запросы", "url": "/post"}
]

def menu_with_current(index):
    menu = copy.deepcopy(MENU)
    menu[index]['current'] = True
    return menu

@app.route('/')
def index():
    return render_template('index.html',
                           title='Заглавие',
                           menu_items=menu_with_current(0))

@app.route('/get')
def get_page():
    return render_template('get.html',
                           title='GET-запросы',
                           menu_items=menu_with_current(1),
                           args=request.args)

@app.route('/cookies')
def cookies_page():
    return render_template('cookies.html',
                           title='Печенье',
                           menu_items=menu_with_current(2),
                           cookies=request.cookies)

@app.route('/post', methods=['GET', 'POST'])
def post_page():
    return render_template('post.html',
                           title='POST-запросы',
                           menu_items=menu_with_current(3),
                           left=request.form.get('left', 'В левой пусто'),
                           right=request.form.get('right', 'В правой пусто'))

if __name__ == '__main__':
    app.run(debug=True)
