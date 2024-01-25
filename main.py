# Importing the create_app function from the 'website' module
from website import create_app

# Creating the Flask application using the create_app function
app = create_app()

# Running the application if the script is executed directly (not imported as a module)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
