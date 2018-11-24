from flask import Flask
from view.User import user_api

app = Flask(__name__)

app.register_blueprint(user_api)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()