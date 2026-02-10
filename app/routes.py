from flask import render_template, Blueprint

bp = Blueprint("main", __name__)


# when an user request the below 2 urls via these 2 decorators 
@bp.route("/")
    # route func from app module takes in the index() func as argument 
    # and does its little magic trick so that the first ar i.e. /index 
    # spits out output from func index
@bp.route("/index")
# invoke this func 
def index(): 
    # return "hello there, gorgeous!"
    # user = {"username"}
    return render_template('index.html')

