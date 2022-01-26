import pymongo
class database():
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client['Loan_Database']
        self.Eligible = self.db['Eligible_Collection']
        self.Not_eligible = self.db['Not_Eligible_Collection']

    def insert_Ele_records(self, records):
        # inserts eligible data records to the collection.
        self.Eligible.insert_one(records)

    def insert_not_ele_records(self, records):
        # inserts not eligible data records to the related collection in the database
        self.Not_eligible.insert_one(records)

