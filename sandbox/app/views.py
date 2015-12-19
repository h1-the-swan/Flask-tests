from flask import render_template, flash, redirect
from app import app
from .forms import TextEntryForm
from .dump_to_file import dump_to_file

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Index')

@app.route('/TextEntry', methods=['GET', 'POST'])
def TextEntry():
    form = TextEntryForm()
    if form.validate_on_submit():
        dump_to_file(form.text.data)
    return render_template('TextEntry.html',
                           title='TextEntry',
                           form=form)
