from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '76ba76024a1a2a047ad011fb74cd9f4e'

posts = [
    {
        'author': 'Purva Anjarlekar',
        'title': 'Blog Post 1',
        'content': 'First post ever',
        'date_posted': '27th November 2019'
    },

    {
        'author': 'Abhay Ubhale',
        'title': 'Blog Post 2',
        'content': 'Second post',
        'date_posted': '29th November 2019'
    },
]

@app.route('/')
def home():
    return render_template('home.html', posts= posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)
    