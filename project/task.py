from flask import Blueprint, render_template, request, flash, redirect, url_for, g, abort
from project.db import get_db
from project.auth import login_required


task_bp = Blueprint('task', __name__)


@task_bp.route('/')
@login_required
def task():
    db = get_db()
    tasks = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM task p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('task/index.html', page='task', tasks=tasks)


@task_bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():

    create = True

    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO task (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('task'))

    return render_template('task/update.html', create=create)


@task_bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):

    create = False

    task = get_post(id)

    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE task SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('task'))

    return render_template('task/update.html', task=task, create=create)


@task_bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM task WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('task'))


def get_post(id, check_author=True):
    task = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM task p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if task is None:
        abort(404, f"Task id {id} doesn't exist.")

    if check_author and task['author_id'] != g.user['id']:
        abort(403)

    return task
