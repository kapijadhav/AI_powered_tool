from flask import Flask
from app.views import main # This imports the 'main' blueprint from app/views.py

def create_app():
    app = Flask(__name__)  # Creates a new Flask application instance
    app.register_blueprint(main) # Registers the 'main' blueprint
    return app

if __name__ == '__main__':
    app = create_app()  # Calls the create_app function to initialize the app
    app.run(debug=True) # Runs the app in debug mode
