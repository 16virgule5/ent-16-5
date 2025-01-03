# edits still last mental breakdowns: 0 (help me lmao)
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def schoolname():
    try:
        with open('./var/schoolname', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return "Le fichier '<répertoire d'installation de 16.5\\var\\schoolname>' n'existe pas."

def get_db_connection():
    conn = sqlite3.connect('users.db')  # Connect to SQLite database
    conn.row_factory = sqlite3.Row  # Allows us to access columns by name
    return conn

@app.route('/')
def hello_world():
    return render_template("login.html", schoolname=schoolname())

@app.route('/loginform', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        name1 = request.form['username']
        pwd = request.form['password']

        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Query to find the user by username
        cursor.execute('SELECT * FROM users WHERE username = ?', (name1,))
        user = cursor.fetchone()

        conn.close()

        # If user is not found or password doesn't match
        if user is None:
            return render_template('login.html', info='Cet utilisateur n\'existe pas.')
        elif user['password'] != pwd:
            return render_template('login.html', info='Mot de passe invalide.')
        else:
            # Login successful, render the home page with username
            return render_template('home.html', name=name1)
    return render_template('login.html', schoolname=schoolname())



def start_app():
    print("Hello ! Welcome to")
    print("""
       *++++++++                 *+++++++++++++                            +++++++++++++++++++++++  
     +++++++++++               *++++++++++++++++++                         *++++++++++++++++++++++  
  ++++++++++++++             ++++++++++++++++++++++                        +++++++++++++++++++++++  
++++++++++++++++            +++++++++*++++++++++++++                       +++++++++++++++++++++++  
++++++++*+++++++           ++++++++*        *++++++++                      +++++++                  
+++++*   +++++++          ++++++++           *+++++++                     *++++++*                  
++*      +++++++          +++++++                                         *++++++                   
         +++++++         *+++++++    +++++++++                            *++++++  ++++++++++       
         +++++++         +++++++  *++++++++++++++                         +++++++++++++++++++++*    
         +++++++         +++++++*++++++++++++++++++                       +++++++++++++++++++++++*  
         +++++++         +++++++++++++++++++++++++++                      ++++++++++++++++++++++++* 
         +++++++         ++++++++++*        +++++++++                     *++++++         *++++++++*
         +++++++         ++++++++*           +++++++++                                      ++++++++
         +++++++         ++++++++             ++++++++                                       +++++++
         +++++++         ++++++++             *+++++++                                       +++++++
         +++++++         *+++++++             ++++++++      ++++++       +++++++             +++++++
         +++++++          ++++++++           ++++++++    +++++++++++     ++++++++           ++++++++
         +++++++           +++++++++*     *+++++++++*   +++++++++++++    *+++++++++      *+++++++++ 
         +++++++            +++++++++++++++++++++++*    ++++++++++++++    ++++++++++++++++++++++++  
         +++++++             +++++++++++++++++++++      +++++++++++++       +++++++++++++++++++++   
         +++++++               *++++++++++++++++        *++++++++++++        *++++++++++++++++*     
         *******                   *++++++*+*             *++++++++              *++++++++*         
""")
    print("an open-source Digital Learning Environment.")
    app.run(host='0.0.0.0', port=5000, debug=True)
    print("Running on ", host, ":", port)

if __name__ == '__main__':
    start_app()
