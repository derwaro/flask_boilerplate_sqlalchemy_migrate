# Flask Boilerplate
**containing Flask, Flask-SQLAlchemy and Flask-Migrate**

## Usage:
1. git clone this repo or download zip
2. create virtualenv: `python3 -m venv venv`
3. install dependencies: `pip3 install -r requirements.txt`
4. create models needed in models.py
5. run:
* `flask db init`
* `flask db migrate -m "init"`
* `flask db upgrade`
6. add routes to `main/routes.py` or add new blueprints

  **please note: wtforms it _not_ included!**
