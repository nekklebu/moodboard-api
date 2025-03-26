from flask import Flask
from moodboard.vibe_engine import gen_vibe

def create_app():
    app = Flask(__name__)

    @app.route("/vibe")
    def vibe():
        return gen_vibe()

    return app
