"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request
from src.mbta_helper import find_stop_near
app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/', methods=['GET', 'POST'])
@app.route('/destination', methods=['GET', 'POST'])
def find():
    if request.method == 'POST':
        place_name = request.form['place']
        stop, distance = find_stop_near(place_name)

        if stop:
            return render_template('Form Result.html', nearest_station = stop, distance = distance)
        else:
            return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
