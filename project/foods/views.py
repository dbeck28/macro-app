from flask import render_template, Blueprint

foods_blueprint = Blueprint('foods', __name__, template_folder='templates')

@foods_blueprint.route('/')
def index():
  return render_template("index.html")