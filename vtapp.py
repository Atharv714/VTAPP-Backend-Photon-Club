# vtapp.py

from flask import Flask, render_template, request, g
import sqlite3
import os

app = Flask(__name__)

DATABASE = 'event_database.db'
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':

        name = request.form.get('name')
        email = request.form.get('email')
        contact_number = request.form.get('contact_number')
        event = request.form.get('event')
        payment_amount = 70 if event == 'Radium Galla' else 50
        registration_number = request.form.get('registration_number')


        if 'screenshot' in request.files:
            screenshot = request.files['screenshot']


            if screenshot and allowed_file(screenshot.filename):

                filename = os.path.join(app.config['UPLOAD_FOLDER'], screenshot.filename)
                screenshot.save(filename)


                db = get_db()
                cursor = db.cursor()

                screenshot_path = os.path.join(app.config['UPLOAD_FOLDER'], screenshot.filename)

                cursor.execute('''
                    INSERT INTO participants (name, email, contact_number, event, payment_amount, screenshot_path, registration_number)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (name, email, contact_number, event, payment_amount, screenshot_path, registration_number))

                db.commit()

    return render_template('registration_form.html')

if __name__ == '__main__':
    exec(open("create_database.py").read())

    # Run the Flask app
    app.run(debug=True)
