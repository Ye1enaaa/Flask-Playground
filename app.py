from flask import Flask, request, jsonify
from myTable import db, MyTable
from myTable import db, CalculateGrams
import MySQLdb
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Create the tables
with app.app_context():
    db.create_all()

# @app.route('/')
# def hello():
#     return 'Hello, Flask!'
@app.route('/post', methods=['POST'])
def create():
    name = request.json.get('name'),
    email = request.json.get('email')

    new_record = MyTable(name=name, email = email)
    db.session.add(new_record)
    db.session.commit()

    return jsonify({'message':'Success'}), 201

@app.route('/calcu', methods=['POST'])
def calcu():
    grams = request.json.get('grams')

    record = CalculateGrams(grams= grams * 2)
    db.session.add(record)
    db.session.commit()

    return jsonify({'messsage':'Success'}), 201

@app.route('/mytable-data', methods=['GET'])
def getAllData():
    records = MyTable.query.all()

    result = []
    for record in records:
        result.append({
            'id': record.id,
            'name': record.name,
            'email': record.email
        })
    return jsonify({'data': result})

if __name__ == '__main__':
    app.run(debug=True)