# Import necessary packages and modules
from flask import Flask
from config import Config
from .api.routes import api
from .site.routes import site
from .authentication.routes import auth
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db as root_db, login_manager, ma
from flask_cors import CORS
from helpers import JSONEncoder

# Create a Flask application instance
app = Flask(__name__)

# Allow Cross-Origin Resource Sharing (CORS)
CORS(app)

# Register Blueprints for different routes
app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)

# set JSON encoder to custom JSONEncoder class
app.json_encoder = JSONEncoder

# Load configuration from Config class
app.config.from_object(Config)

# Initialize root database object with app
root_db.init_app(app)

# Initialize the Flask-Login LoginManager object with the app
login_manager.init_app(app)

# Initialize the Flask-Marshmallow Marshmallow object with the app
ma.init_app(app)

# Initialize Flask-Migrate object with the app and root database object
migrate = Migrate(app, root_db)