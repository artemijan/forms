from flask import request
from flask_restful import Resource, abort

from backend.db import get_db


class Form(Resource):
    def get(self, id=None):
        if id is None:
            abort(400)
        db = get_db()
        cur = db.cursor()
        cur.execute("SELECT content FROM form WHERE id=?", (str(id),))
        rows = cur.fetchall()
        if len(rows) == 0:
            return abort(404)
        return {'payload': rows[0][0]}

    def post(self):
        db = get_db()
        data = request.json
        cur = db.cursor()
        cur.execute("INSERT INTO form (content) VALUES (?)", (data['content'],))
        return {'payload': {'id': cur.lastrowid}}

