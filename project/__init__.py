from flask import Flask


################
#### config ####
################

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')


####################
#### blueprints ####
####################

from project.users.views import users_blueprint
from project.foods.views import foods_blueprint

# register the blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(foods_blueprint)