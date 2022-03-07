from flask import Flask
from routes import routes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Setup routes
routes.initialize(app)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
