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
        data = (
            to_date, from_date, from_date, to_date, from_date, to_date, to_date, from_date, from_date, to_date,
            from_date, to_date)
        cursor.execute(
            "SELECT SUM(price * (SELECT SUM(DATEDIFF(LEAST(departure, %s), GREATEST(%s, arrival)) + 1) FROM clients "
            "WHERE (arrival BETWEEN %s AND %s OR departure BETWEEN %s AND %s) AND room_number = number AND is_paid = 1 "
            "AND with_breakfast = 0)) as no_breakfast,SUM(price_with_breakfast * (SELECT SUM(DATEDIFF(LEAST(departure,"
            " %s), GREATEST(%s, arrival)) + 1) FROM clients WHERE (arrival BETWEEN %s AND %s OR departure BETWEEN %s "
            "AND %s) AND room_number = number AND is_paid = 1 AND with_breakfast = 1)) as with_breakfast "
            "FROM rooms;", data)
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
