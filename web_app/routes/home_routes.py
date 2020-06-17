from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def hello():
    return f"Hello World! {x}"

@home_routes.route("/about")
def about():
    return "About me"