from flask import Blueprint, render_template, request, flash, redirect, url_for, g
from flask import current_app as app
from project.db import get_db
from project.auth import login_required


# Blueprint Configuration
home_bp = Blueprint('home_bp', __name__,)


@home_bp.route('/')
def index():
    return render_template('index.html', page="index")