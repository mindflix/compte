from flask import Blueprint, render_template, request, flash, redirect, url_for, g
from flask import current_app as app
from project.db import get_db
from project.auth import login_required


counting_bp = Blueprint('counting', __name__)


@counting_bp.route('/')
@login_required
def counting():
    return render_template('counting/index.html', page="counting")
