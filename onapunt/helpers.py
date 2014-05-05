"""
    onapunt.helpers
    ~~~~~~~~~~~~~~~
"""

import importlib
import pkgutil

from flask import Blueprint

from . import tracking


def register_blueprints(app):
    """Register all Blueprint instances on the specified Flask application from
    all modules under the app package.
    """

    package_path = app.root_path
    package_name = app.import_name

    tracking.info(package_path)

    for _, name, _ in pkgutil.iter_modules([package_name]):
        import_name = '%s.%s' % (package_name, name)

        m = importlib.import_module(import_name)
        for item in dir(m):
            item = getattr(m, item)
            if isinstance(item, Blueprint):
                app.register_blueprint(item)
                tracking.info("Registered `%s` blueprint onto `%s` app" %
                             (item.name, app.import_name))
