import pymysql
from backend.app import app
from backend.db_config import mysql
from flask import jsonify
from flask import request
from backend.rooms import rooms
from backend.clients import clients
from backend.incomes import incomes


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


def init_database():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        # create if not exists rooms table
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS rooms ("
            "id INT AUTO_INCREMENT PRIMARY KEY, "
            "number INT NOT NULL, "
            "persons INT NOT NULL, "
            "floor INT NOT NULL, "
            "has_tv BOOL NOT NULL, "
            "has_fridge BOOL NOT NULL, "
            "has_phone BOOL NOT NULL, "
            "price INT NOT NULL, "
            "price_with_breakfast INT NOT NULL,"
            "INDEX num(number)) ENGINE=INNODB"
        )
        # create if not exists clients table
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS clients ("
            "id INT AUTO_INCREMENT PRIMARY KEY, "
            "first_name TEXT NOT NULL, "
            "last_name TEXT NOT NULL, "
            "room_number INT NOT NULL, "
            "arrival DATE NOT NULL, "
            "departure DATE NOT NULL, "
            "is_paid BOOL NOT NULL, "
            "with_breakfast BOOL NOT NULL, "
            "INDEX room_num (room_number), "
            "FOREIGN KEY (room_number) REFERENCES rooms(number) "
            "ON DELETE CASCADE) ENGINE=INNODB"
        )
        return
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


app.register_blueprint(rooms)
app.register_blueprint(clients)
app.register_blueprint(incomes)


@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    return response


if __name__ == "__main__":
    init_database()
    app.run()
