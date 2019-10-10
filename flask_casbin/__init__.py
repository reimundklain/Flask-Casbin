# -*- coding: utf-8 -*-

__author__ = "Reimund Klain"
__email__ = "reimund.klain@condevtec.de"

import logging
import casbin


log = logging.getLogger()


class Casbin:
    """Manages Flask Casbin integration

    :param app: Flask instance
    """

    def __init__(self, app=None):
        self.app = app
        self.enforcer = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.enforcer = casbin.Enforcer(
            app.config.get("CASBIN_MODEL_CONF"),
            app.config.get("CASBIN_POLICY_CSV"),
            app.debug or app.testing,
        )

        # register extension
        app.extensions = getattr(app, "extensions", {})
        app.extensions["casbin"] = self.enforcer

    def enforce(self, *rval):
        """Delegate to enforcer

        :param rval: (sub, obj, act)
        :return: bool
        """
        return self.enforcer.enforce(*rval)
