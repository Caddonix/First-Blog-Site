from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


# posts = [
#     {
#         'author': 'Purva Anjarlekar',
#         'title': 'Blog Post 1',
#         'content': 'First post ever',
#         'date_posted': '27th November 2019'
#     },

#     {
#         'author': 'Abhay Ubhale',
#         'title': 'Blog Post 2',
#         'content': 'Second post',
#         'date_posted': '29th November 2019'
#     },
# ]