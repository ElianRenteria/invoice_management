from flask import Flask
from views import views
from flask_cors import CORS
from flask_caching import Cache

config = {
    "CACHE_TYPE": "SimpleCache",
    "CACHE_THRESHOLD": 300
}

app = Flask(__name__, template_folder="templates", static_folder="static")
app.register_blueprint(views, url_prefix="/views")
app.config.from_mapping(config)

if __name__ == '__main__':
    app.run(debug=True, port=8000)