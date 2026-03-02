from flask import render_template, Blueprint
from backend.app import db

bp = Blueprint("routes", __name__)
@bp.errorhandler(404)
def not_found(error): 
    # return render_template("notFound.html"), 404
    return {"error": "resource not found"}, 404

@bp.errorhandler(500)
def db_error(error): 
    db.session.rollback()
    # return render_template("dbError.html"), 500
    return {"error": "no data"}, 500



