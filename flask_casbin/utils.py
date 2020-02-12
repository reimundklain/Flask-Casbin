# -*- coding: utf-8 -*-

__author__ = "Reimund Klain"
__email__ = "reimund.klain@condevtec.de"


from werkzeug.local import LocalProxy
from flask import (  # type: ignore
    _request_ctx_stack,
    current_app,
    after_this_request,
    has_request_context,
)

current_enforcer = LocalProxy(lambda: _get_enforcer())


def _get_enforcer():
    if has_request_context() and not hasattr(_request_ctx_stack.top, "enforcer"):
        current_app.casbin_manager._load_policy()

    return getattr(_request_ctx_stack.top, "enforcer", None)


def _enforcer_context_processor():
    return dict(current_enforcer=_get_enforcer())