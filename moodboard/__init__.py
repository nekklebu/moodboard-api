from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/vibe")
    def vibe():
        return {
                "quote": "You are a moonlight bloom in a concrete world.",
                "color": "#A3D9FF",
                "song": "https://open.spotify.com/track/4VqPOruhp5EdPBeR92t6lQ",
                "suggestion": "Open your window. Listen to the city breathe.",
                "mood": "Quiet Spark"
                }

    return app
