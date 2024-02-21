from flask import Flask

app = Flask(__name__, template_folder="../build", static_folder="../build", static_url_path="")

from flask_cors import CORS
CORS(app, resources={r"/*": {"origins": "*"}})
from app import routes