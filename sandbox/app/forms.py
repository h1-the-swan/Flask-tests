from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class TextEntryForm(Form):
    text = TextAreaField('text', validators=[DataRequired()])
