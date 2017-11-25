import sqlite3

from flask import g

from backend.config import CONFIG

conf = CONFIG['dev']


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(conf.DATABASE)
    return db
