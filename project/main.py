from flask import Blueprint, render_template


# Blueprint Configuration
main_bp = Blueprint('home_bp', __name__,)


@main_bp.route('/')
def index():
    return render_template('index.html')
