from flask import Flask
from flask_cors import CORS
from routes.ticket_routes import ticket_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(ticket_bp)

if __name__ == "__main__":
    app.run(debug=True)