from flask import Flask, request, jsonify
from pymongoOps import db_operations_mongodb


app = Flask(__name__)


@app.route('/mongodb/create_db_collection', methods=['POST'])
def create():
    if request.method == "POST":
        db_name = request.json['db_name']
        collection_name = request.json['collection_name']
        record = request.json['record']
        py_mongo_ops = db_operations_mongodb()
        return jsonify(py_mongo_ops.create_database(db_name, collection_name, record))


@app.route('/mongodb/delete_one', methods=['POST'])
def delete():
    if request.method == "POST":
        db_name = request.json['db_name']
        collection_name = request.json['collection_name']
        delete_query = request.json['delete_query']
        py_mongo_ops = db_operations_mongodb()
        return jsonify(py_mongo_ops.delete_record(db_name, collection_name, delete_query))


if __name__ == '__main__':
    app.run()