"""
    onapunt.pages
    ~~~~~~~~~~~~~

    This module contains the views for the special pages (home, privacy policy,
    terms of service etc.)
"""

from flask import render_template

from onapunt.factory import create_blueprint

bp = create_blueprint('pages', __name__)


@bp.route('/')
def home():
    return render_template('pages/home_temp.html')

@bp.route('/openssl')
def openssl():
    import _ssl
    return str(_ssl.OPENSSL_VERSION)
