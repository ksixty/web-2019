from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)
application = app

@app.route('/')
@app.route('/<int:place>')
def display_template(place=1):
    date = datetime.now().isoformat()
    menu = [{'text': 'Айн',  'url': '/1'},
            {'text': 'Цвай', 'url': '/2'},
            {'text': 'Драй', 'url': '/3'}]

    if (place - 1) > len(menu):
        return "404", 404
    
    menu[place - 1]['current'] = True
    
    return render_template('lab1.html',
                           title='Лаба 1',
                           date=date,
                           menu_items=menu)

if __name__ == '__main__':
    app.run(debug=True)
