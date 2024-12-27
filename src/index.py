# edits still last mental breakdowns: 0 (help me lmao)
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def schoolname():
    try:
        with open('/var/schoolname', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return "Cet établissement n'a aucun nom ! Vous pouvez changer le nom de cet établissement dans '<répertoire d'installation de 16.5\\var\\schoolname>'"

@app.route('/')
def index():
    return render_template('index.html', schoolname=schoolname())


def start_app():
    print("Welcome to 16.5!")
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__':
    start_app()
