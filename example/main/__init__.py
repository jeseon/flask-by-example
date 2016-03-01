from flask import Blueprint

main = Blueprint('main', __name__)

from example.main import views