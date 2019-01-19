from flask import Blueprint, request, jsonify
from backend.db_config import mysql
import pymysql

clients = Blueprint('clients', __name__)


@clients.route('/clients', methods=['GET'])
def get_clients():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM clients")
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


@clients.route('/clients/<id>', methods=['GET'])
def get_client(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM clients where id=%s", id)
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


@clients.route('/clients', methods=['PUT'])
def add_client():
    try:
        _json = request.json
        first_name = _json['first_name']
        last_name = _json['last_name']
        room_number = _json['room_number']
        arrival = _json['arrival']
        departure = _json['departure']
        is_paid = _json['is_paid']
        with_breakfast = _json['with_breakfast']
        sql = "INSERT INTO clients (first_name, last_name, room_number, arrival, departure, is_paid, with_breakfast) " \
              "VALUES(%s, %s, %s, %s, %s, %s, %s)"
        data = (first_name, last_name, room_number, arrival, departure, is_paid, with_breakfast)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        resp = jsonify('Client added successfully!')
        resp.status_code = 200
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@clients.route('/clients', methods=['POST'])
def update_client():
    try:
        _json = request.json
        id = _json['id']
        first_name = _json['first_name']
        last_name = _json['last_name']
        room_number = _json['room_number']
        arrival = _json['arrival']
        departure = _json['departure']
        is_paid = _json['is_paid']
        with_breakfast = _json['with_breakfast']
        sql = "UPDATE clients SET first_name=%s, last_name=%s, room_number=%s, arrival=%s, departure=%s, is_paid=%s, \
        with_breakfast=%s WHERE id=%s"
        data = (first_name, last_name, room_number, arrival, departure, is_paid, with_breakfast, id)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        resp = jsonify('Client updated successfully!')
        resp.status_code = 200
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@clients.route('/clients/<id>', methods=['DELETE'])
def delete_client(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clients where id=%s", id)
        conn.commit()
        resp = jsonify('Client deleted successfully!')
        resp.status_code = 200
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
