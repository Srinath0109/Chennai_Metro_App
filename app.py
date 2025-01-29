from flask import Flask
from routes import metro_routes

app = Flask(__name__)

# Register blueprints (routes)
app.register_blueprint(metro_routes, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
