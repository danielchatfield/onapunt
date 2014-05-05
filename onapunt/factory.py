"""
    onapunt.factory
    ~~~~~~~~~~~~~~~

    The factory module is based upon the one in the overholt example app:
    https://github.com/mattupstate/overholt/blob/master/overholt/factory.py

    The factory pattern gives more control over the creation of the app in
    different contexts (development, production, within a test runner). It also
    makes it trivial to spawn multiple apps within the same process bound to
    different ports.
"""

import os.path

from flask import Flask, Blueprint
from flask.helpers import get_root_path

from .helpers import register_blueprints


def create_app(package_name='onapunt', config=None, **kwargs):
    """Returns a :class:`Flask` application instance configured with common
    flask extensions for the On a Punt Website.

    :param config: a dictionary of settings to override flask.config
    """

    # Use the helper function from flask to determine the directory that
    # contains the flask app package.
    package_path = get_root_path(package_name)

    # By default Flask's template folder is contained within the python package
    # that contains the app. For consistency either the assets should also be
    # contained within the package or they should all be outside.
    #
    # Logically it makes more sense IMO to either have separate folders for;
    # python, css, js, etc. or to have modules where the python, css, js etc.
    # for each module is contained within a single folder. The latter is quite
    # complex to achieve (compilation headaches) and thus I have decided to
    # structure it like this.
    template_folder = os.path.join(os.path.dirname(package_path), 'templates')

    default_kwargs = {
        'instance_relative_config': True,
        'template_folder': template_folder
    }

    # Merge the kwargs with the defaults
    kwargs = dict(default_kwargs.items() + kwargs.items())

    app = Flask(package_name, **kwargs)

    app.config.from_object(package_name + '.settings')
    app.config.from_pyfile('settings.cfg', silent=True)
    app.config.from_object(config)

    # This registers all blueprints found in the child modules to the app
    register_blueprints(app)

    return app


def create_blueprint(*args, **kwargs):
    """Little wrapper around the :class:`Blueprint` class that is here so that
    in the future common configuration can be easily applied to all blueprints
    """
    return Blueprint(*args, **kwargs)
