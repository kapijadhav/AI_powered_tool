from flask import Flask

def create_app():
    """
        Creates and configures the Flask application instance.

        Returns:
            Flask: The Flask application instance.
    """
    app = Flask(__name__)
    from .views import main
    app.register_blueprint(main)
    return app