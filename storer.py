import pymongo

class Storer(object):
    def __init__(self, db, collection):
        self.client = pymongo.MongoClient("localhost", 27017)
        self.db = self.client[db]
        self.collection = self.db[collection]

    def save(self, item):
        self.collection.replace_one({"_id": item["_id"]}, item, True)

        """
        if "_id" in item and self.is_exist(item["_id"]):
            self.collection.update_one({"_id": item["_id"]}, item)
        else:
            self.collection.insert_one(item)
        """

    def is_exist(self, _id):
        if self.collection.find_one({"_id": _id}):
            return True
        else:
            return False