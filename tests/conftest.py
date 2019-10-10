# -*- coding: utf-8 -*-

import pytest
from flask import Flask
from flask_casbin import Casbin


@pytest.fixture(scope='session')
def app(request):
    config=dict(
        TESTING=True,
    )
    app = Flask(__name__)
    app.config.update(config)
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()
    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope='session')
def acl(app):
    app.config.update(dict(
        CASBIN_MODEL_CONF="./tests/model.conf",
        CASBIN_POLICY_CSV="./tests/policy.csv",
    ))
    return Casbin(app)

