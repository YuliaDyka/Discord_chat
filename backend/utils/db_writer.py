import csv

from models import User, Chat, UserHasChat, Message, AbstractModel
from .csv_generator import CSVGenerator


def write_csv_to_db():
    generator = CSVGenerator()
    generator.generate_csv()

    Model: AbstractModel
    for Model in [User, Chat, UserHasChat, Message]:
        with open(f"backend/csv_files/{Model.__tablename__}.csv", 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                obj = Model(**row)
                obj._save()
