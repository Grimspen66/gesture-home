from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('home', __name__)

@bp.route('/<int:id>')
@login_required
def index(id, check_author = True):
    db = get_db()
    appliances = db.execute(
        'SELECT a.user_id, appliance_name'
        'FROM appliances JOIN user u ON a.user_id = u.id'
        'WHERE a.id = ?',
        (id,)
    ).fetchall()
    return render_template('home/index.html', appliances=appliances)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        appliance = request.form['appliance']
        gesture = request.form['gesture']
        error = None

        if not appliance:
            error = 'Appliance is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO settings (user_id, appliance)'
                ' VALUES (?, ?)',
                (g.user['id'], appliance)
            )
            db.commit()
            db.execute(
                'INSERT INTO appliance (user_id, appliance_name, gesture)'
                ' VALUES (?, ?, ?)',
                (g.user['id'], appliance, gesture)
            )
            db.commit()
            return redirect(url_for('home.index'))

    return render_template('home/create.html')