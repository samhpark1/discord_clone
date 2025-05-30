import firebase_admin
from firebase_admin import credentials, firestore
import os

class NoSQLManager:
    def __init__(self, cred_path=None):
        cred_path = cred_path or os.getenv("FIREBASE_CREDENTIALS")
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def get_collection(self, name):
        return self.db.collection(name)

    def add_document(self, collection, data):
        return self.db.collection(collection).add(data)