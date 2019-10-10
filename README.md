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
from flask import Flask
from flask_casbin import Casbin

app = Flask(__name__)

# config
app.config["CASBIN_MODEL_CONF"] = "./model.conf"
app.config["CASBIN_POLICY_CSV"] = "./policy.csv"

# create acl
acl = Casbin(app)

@app.route('/data/<id_:int>')
def get_data(id_):
    # curent_user ist global authenticated user
    acl.enforce("user:%s" % current_user.name, "data:%d" % id_, "read") or abort(401)

    # Get data
    data = db.get_data(id_)
    return { data_id: data.id, data: data.payload }

```

Todo
----

* Decorators for ACL check
* Policy adapters
* Dynamic Policy Adapter (Flask-SQLAlchemy)
* More tests

Resources
---------

- [pypi](https://pypi.python.org/pypi/Flask-Casbin)
- [casbin](https://casbin.org/)
- [pycasbin](https://github.com/casbin/pycasbin)
