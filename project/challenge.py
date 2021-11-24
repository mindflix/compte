from flask import Blueprint, render_template, g
from flask.helpers import flash
from project.db import get_db
from project.auth import login_required

challenge_bp = Blueprint('challenge', __name__)


@challenge_bp.route('/')
@login_required
def challenge():
    return render_template('challenge/index.html')


@challenge_bp.route('/start')
@login_required
def start():
    users = get_db().execute(
        'SELECT id, username'
        ' FROM user'
        ' WHERE id != ?',
        (g.user['id'],)
    ).fetchall()
    return render_template("challenge/start.html", users=users)
