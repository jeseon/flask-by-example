from flask import render_template
from example.main import main
from example.models import CeoNotice

@main.route('/')
def index():
    return render_template('example/index.html', hello='Hello')

@main.route('/notice/<int:id>')
def notice(id):
    return 'Title: ' + CeoNotice.query.filter_by(id=id).first().title
