import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

cred = credentials.Certificate("tetrisscores-firebase-adminsdk-2adoz-8c0c7e839a.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def addScoreToFireBase(data):
    doc_ref = db.collection('Scores').document()
    doc_ref.set(data)



def getHighestScore():
    # Consulta para obter o maior score
    query = db.collection('Scores').order_by("Score", direction=firestore.Query.DESCENDING).limit(1)

    # Obter resultados da consulta
    results = query.get()

    # Verificar se há resultados
    if results:
        # Iterar sobre os resultados (deve haver apenas um, pois limitamos a 1)
        for doc in results:
            # Retornar o maior score
            return doc.to_dict()["Score"]
    else:
        return None

