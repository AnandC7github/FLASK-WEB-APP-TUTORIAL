# Importing Flask class from the Flask module
from flask import Flask

# Function to create and configure the Flask application
def create_app():
    # Creating an instance of the Flask class with the name of the package or module
    app = Flask(__name__)
    
    # Setting a secret key for the application (used for session management and security)
    app.config['SECRET_KEY'] = 'Anand'
    
    # Returning the configured app instance
    return app
