import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

cred = credentials.Certificate("tetrisscores-firebase-adminsdk-2adoz-8c0c7e839a.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def addScoreToFireBase(data):
    
    doc_ref = db.collection('Scores').document()
    doc_ref.set(data)