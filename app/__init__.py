from flask import Flask, render_template
from flask_migrate import Migrate
from flask_cors import CORS

from .controllers.UserController import userRoutes as userBlueprint
from .controllers.AuthController import authRoutes as authBlueprint
from .controllers.OrgController import orgRoutes as orgBlueprint

from .configs import configs
from .models import db, bcrypt
from .websocket import socketio

# Creating flask api
app = Flask(__name__, template_folder='templates')

# Set api configs
app.config.from_object(configs['development'])

#Init bcrypt
bcrypt.init_app(app)

#Set Cors
CORS(app)

# Init DB
db.init_app(app)
migrate = Migrate(app=app, db=db)

#Init websocket
socketio.init_app(app)

# Init Routes
app.register_blueprint(userBlueprint, url_prefix='/api/v1/users')
app.register_blueprint(authBlueprint, url_prefix='/api/v1/auth')
app.register_blueprint(orgBlueprint, url_prefix='/api/v1/orgs')

@app.route('/admin', methods=['GET'])
def index():
  return render_template("index.html", title = 'Websocket Admin')

@app.route('/manager', methods=['GET'])
def index2():
  return render_template("index2.html", title = 'Websocket Manager')