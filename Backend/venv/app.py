from flask import Flask
from flask_cors import CORS
from auth.signup import app as signup_app
from auth.login import app as login_app
app = Flask(__name__)
CORS(app)
app.register_blueprint(signup_app, url_prefix="/api")
app.register_blueprint(login_app, url_prefix="/api")
if __name__ == "__main__":
    app.run(debug=True)