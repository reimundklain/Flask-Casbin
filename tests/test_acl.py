# -*- coding: utf-8 -*-

__author__ = "Reimund Klain"
__email__ = "reimund.klain@condevtec.de"

import io
import unittest
from flask import Flask
from flask_casbin import CasbinManager, IOAdapter, current_enforcer



class StaticTestCase(unittest.TestCase):
    def test_static_loads_policy(self):
        app = Flask(__name__)
        app.config.update(CASBIN_MODEL_CONF="./model.conf")
        app.static_url_path = '/static'
        app.secret_key = 'this is a temp key'
        cm = CasbinManager()
        cm.init_app(app)

        @cm.policy_loader
        def load():
            with open("./policy.csv", "rb") as fd:
                return IOAdapter(io.BytesIO(fd.read()))

        with app.test_client() as c:
            c.get('/static')
            self.assertIsNotNone(current_enforcer)
            assert current_enforcer.enforce("user:alice", "data:1", "read") is True