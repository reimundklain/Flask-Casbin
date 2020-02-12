# -*- coding: utf-8 -*-

#import io
#import pytest
#from flask import Flask
#from flask_casbin import CasbinManager, IOAdapter


#@pytest.fixture(scope='module')
#def test_client():
#    config=dict(
#        TESTING=True,
#        CASBIN_MODEL_CONF="./tests/model.conf"
#    )
#    app = Flask(__name__)
#    app.config.update(config)
#    manager = CasbinManager(app)
#
#    @manager.policy_loader
#    def load():
#        with open("./tests/model.conf", "rb") as fd:
#            return IOAdapter(fd)
#
#    test_client = app.test_client()
#    ctx = app.app_context()
#    ctx.push()
#    yield test_client
#    ctx.pop()
