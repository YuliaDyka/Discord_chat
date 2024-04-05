from flask import make_response
from flask_restful import Resource

from utils.db_writer import write_csv_to_db

class CSVGeneratorController(Resource):
    def get(self):
        write_csv_to_db()

        return make_response("CSV writed to database", 200)