from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)


class Item(db.Model):
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    img = db.Column(db.String(), nullable=False)
    bio = db.Column(db.String(), nullable=True)


abouts = [
    {'id': 1, 'name': 'Richard', 'img': 'https://images.unsplash.com/photo-1621542865781-6eb360f1a7f8?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OXx8ZHB8ZW58MHx8MHx8&auto=format&fit=crop&w=', 'bio': 'He is a...'},
    {'id': 2, 'name': 'Trevor', 'img': 'https://images.unsplash.com/photo-1521119989659-a83eee488004?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=', 'bio': 'He is a...'},
    {'id': 3, 'name': 'Benjamin', 'img': 'https://images.unsplash.com/photo-1531427186611-ecfd6d936c79?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=', 'bio': 'He is a...'}
]


def addprefix(abouts, attribute, prefix, infix="", postfix=""):

    for about in abouts:
        about[attribute] = prefix+"="+infix+about[attribute]+postfix
        print(about[attribute])


@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html')


@app.route('/about')
def about_page():

    for about in abouts:
        about["imglink"] = "src="+about["img"]+"300&h=300"
        about["link"] = "href=/about/"+about["name"].lower()
    # addprefix(abouts, "img", "src")
    # addprefix(abouts, "name", "href", "/about/")
    return render_template('about.html', abouts=abouts)


@app.route('/about/<username>')
def about_user(username):
    print(username)
    for about in abouts:

        about["name"] = about["name"].lower()
        print(about)
        if about["name"] == username:
            print("yes about is", about)
            about["imglink"] = "src="+about["img"]+"300&h=300"
            about["link"] = "href=/about/"+about["name"].lower()
            return render_template('aboutu.html', username=username, about=about)
    # return "i cant"
