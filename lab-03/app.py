from flask import Flask, render_template, request, make_response
from datetime import datetime
import random
import copy
app = Flask(__name__)
application = app

MENU = [
    {"text": "Заглавие", "url": "/"},
    {"text": "Калькулятор", "url": "/calc"},
    {"text": "Сколькослов", "url": "/wc"}
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

@app.route('/calc')
def calc_page():
    info = ""
    cookies = []
    raw_cookies = request.cookies
    for cookie in raw_cookies:
        if "k60lc-result" in cookie:
            cookies.append(raw_cookies[cookie])
    try:
        l, op, r = [request.args[arg] for arg in request.args]
        l, r = [int(n) for n in (l, r)]
    except:
        l =  op = r = 0
    if op == '+':
        result = l + r
    elif op == '-':
        result = l - r
    elif op == '/':
        try:
            result = l / r
        except ZeroDivisionError:
            result = "inf"
    elif op == '*':
        result = l * r
    else:
        if op != 0:
            info += 'Не понимаю. '
        result = ''
    response = make_response(render_template('calc.html',
                                             title='Калькулятор',
                                             info=info,
                                             result=result,
                                             cookies=cookies,
                                             left=l, right=r, operand=op,
                                             menu_items=menu_with_current(1)))
    if result:
        response.set_cookie(f"k60lc-result-{random.randint(100000, 999999)}",
                   value=f"{l} {op} {r}={result}",
                   path="/")
    return response

@app.route('/wc', methods=['GET', 'POST'])
def wc_page():
    text = request.form.get('words', '')
    result = len(text.split())
    return render_template('wc.html',
                           result=f'Слов: {result}',
                           title='Сколькослов',
                           text=text,
                           menu_items=menu_with_current(2))

if __name__ == '__main__':
    app.run(debug=True)
