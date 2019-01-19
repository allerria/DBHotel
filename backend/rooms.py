from flask import Blueprint, request, jsonify
from backend.db_config import mysql
import pymysql

rooms = Blueprint('rooms', __name__)


@rooms.route('/rooms')
def get_rooms():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM rooms")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@rooms.route('/rooms_available')
def get_rooms_available():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM rooms WHERE number NOT IN (SELECT room_number FROM clients "
                       "where CURDATE() BETWEEN arrival AND DEPARTURE)")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@rooms.route('/rooms/<id>')
def get_room(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM rooms WHERE id=%s", id)
        rows = cursor.fetchone()
        resp = jsonify(rows)
        resp.status_code = 200
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@rooms.route('/rooms', methods=['PUT'])
def add_room():
    try:
        _json = request.json
        number = _json['number']
        persons = _json['persons']
        floor = _json['floor']
        has_tv = _json['has_tv']
        has_fridge = _json['has_fridge']
        has_phone = _json['has_phone']
        price = _json['price']
        price_with_breakfast = _json['price_with_breakfast']
        sql = "INSERT INTO rooms (number, persons, floor, has_tv, has_fridge, has_phone, price, price_with_breakfast) " \
              "VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
        data = (number, persons, floor, has_tv, has_fridge, has_phone, price, price_with_breakfast)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        resp = jsonify('Room added successfully!')
        resp.status_code = 200
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@rooms.route('/rooms', methods=['POST'])
def update_room():
    try:
        _json = request.json
        id = _json['id']
        number = _json['number']
        persons = _json['persons']
        floor = _json['floor']
        has_tv = _json['has_tv']
        has_fridge = _json['has_fridge']
        has_phone = _json['has_phone']
        price = _json['price']
        price_with_breakfast = _json['price_with_breakfast']
        sql = "UPDATE rooms SET number=%s, persons=%s, floor=%s, has_tv=%s, has_fridge=%s, has_phone=%s, price=%s, " \
              "price_with_breakfast=%s WHERE id=%s"
        data = (number, persons, floor, has_tv, has_fridge, has_phone, price, price_with_breakfast, id)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        resp = jsonify('Room updated successfully!')
        resp.status_code = 200
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@rooms.route('/rooms/<id>', methods=['DELETE'])
def delete_room(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM rooms WHERE id=%s", id)
        conn.commit()
        resp = jsonify('Room deleted successfully!')
        resp.status_code = 200
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
