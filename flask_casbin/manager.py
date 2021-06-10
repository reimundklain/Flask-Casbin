# -*- coding: utf-8 -*-

__author__ = "Reimund Klain"
__email__ = "reimund.klain@condevtec.de"

from flask import abort, current_app, request, _request_ctx_stack
import casbin

from .utils import _enforcer_context_processor

class CasbinManager(object):
    """Manages Flask Casbin integration

    :param app: Flask instance
    """

    def __init__(self, app=None):
        self.app = app
        self.policy_callback = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.casbin_manager = self
        app.context_processor(_enforcer_context_processor)

    def policy_loader(self, callback):
        """
        :param callback: The callback for retrieving a policy object.
        :type callback: callable
        """
        self.policy_callback = callback
        return callback

    def _load_policy(self):
        ctx = _request_ctx_stack.top
        if self.policy_callback is None:
            raise Exception(
                "No policy_loader has been installed for this " "CasbinManager."
            )

        ctx.enforcer = casbin.Enforcer(
            current_app.config.get("CASBIN_MODEL_CONF"),
            self.policy_callback(),
        )
