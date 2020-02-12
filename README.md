Flask-Casbin
============

[![Build Status](https://travis-ci.org/daymien/Flask-Casbin.png?branch=master)](https://travis-ci.org/daymien/Flask-Casbin)


Flask-Casbin is an extension that provide Casbin ACL functionality to your Flask project

Installation
------------

Install Flask-Casbin with `pip`:

    pip install Flask-Casbin

Install Flask-Casbin with `poetry`:

    poetry add Flask-Casbin

Example
-------

This is an example Flask application:

```python
from flask import Flask, abort
from flask_casbin import CasbinManager, IOAdapter, current_enforcer

app = Flask(__name__)

# config
app.config["CASBIN_MODEL_CONF"] = "./model.conf"

acl = CasbinManager(app)

@acl.policy_loader
def load_policy():
    # some readable object for example based on current user
    return IOAdapter(current_user.policy())

@app.route('/data/<id_:int>')
def get_data(id_):
    # curent_user ist global authenticated user
    current_enforcer.enforce(f"user:{current_user.name}", f"data:{id}", "read") or abort(401)
    
    # Get data
    data = db.get_data(id_)
    return { data_id: data.id, data: data.payload }

```

Todo
----

* Decorators for ACL check
* ~Policy adapters~
* ~Dynamic Policy Adapter (Flask-SQLAlchemy)~
* More tests

Resources
---------

- [pypi](https://pypi.python.org/pypi/Flask-Casbin)
- [casbin](https://casbin.org/)
- [pycasbin](https://github.com/casbin/pycasbin)
