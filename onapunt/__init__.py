"""
    onapunt
    ~~~~~~~

    Source code for the onapunt.com website.
"""

from flask import render_template
from .factory import create_app

app = create_app(__name__)
