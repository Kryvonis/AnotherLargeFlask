from datetime import datetime
from flask import redirect, render_template, sessions, url_for
from app import main


@main.route('/', methods=['GET', 'POST'])
def index():
    # form = NameForm()
    # if form.validate_on_submit():
    #
    # return redirect(url_for('.index'))
    return render_template('index.html')
