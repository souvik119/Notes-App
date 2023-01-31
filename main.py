# reason we can do that is because of __init__.py website is a package
from website import create_app

app = create_app()

# only run the webserver if main.py is run directly
if __name__ == '__main__':
    # everytime a change is made, re-run the server because debug is True
    # should turn it off for prod env
    app.run(debug=True)