from flask import Flask, render_template, url_for
app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
    