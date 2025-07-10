# app.py

# First, we imported a class called Flask from the flask library.
# (We can easily clock it as a class because it is in PascalCase!)
from flask import Flask

# Next, we created an object called app, which is an instance of the Flask class.
# We handed the initialiser function the __name__ object,
# which is automatically created by the Python interpreter, and in this case it is equal to the string "__main__".
# The initialiser function for the Flask object happens to require this value when it creates the instance.
app = Flask(__name__)

# Finally, we created a special function, using a decorator.
# The function tells Flask how to respond to a request.
# Our response in this case is a little snippet of HTML. If you inspect the page in your browser, you should see the <p> element.
# If we were constructing a more complex full-stack app, we would respond with a large file containing HTML and maybe JavaScript rather than this little scrap.
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# @app.route("/") = A decorator is a special function that modifies another function.
# We can write our own if we want to, but in this case we are using one that is pre-defined as a method on our app object from the Flask class.
# This decorator in particular takes a function (in this case, our hello_world function), and attaches it to our server, at a specified route, so that it is triggered by requests at that route.

@app.route("/goodbye/")
def goodbye_world():
    return "<p>Goodbye, World!</p>"

@app.route("/coder/")
def coder():
    return "<p>This web app was created in a class at Coder Academy.</p>"
