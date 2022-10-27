from flask import Flask, render_template, request
from flask_bcrypt import generate_password_hash
from tester import teamNames

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("teamPage.html")



if __name__ == '__main__':
    app.run(debug=True)