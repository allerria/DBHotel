from flask import Blueprint, request, jsonify
import simplejson
import flask
from backend.db_config import mysql
import pymysql

incomes = Blueprint('incomes', __name__)
flask.json = simplejson


@incomes.route('/incomes', methods=['GET'])
def get_incomes():
    try:
        from_date = request.args.get('from')
        to_date = request.args.get('to')
        print(from_date, to_date)
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT SUM(price * (SELECT SUM(DATEDIFF(IF(departure <= %s, departure, %s), departure())) FROM clients WHERE CAST(%s AS DATE) BETWEEN arrival AND departure AND room_number = number AND is_paid = 1)) as daily_incomes FROM rooms;", from_date)
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
