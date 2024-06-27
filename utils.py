from database import database

def get_next_id(collection_name):
    counters = database.get_database().counters
    counter = counters.find_one_and_update(
        {"_id": collection_name},
        {"$inc": {"seq": 1}},
        return_document=True,
        upsert=True
    )
    if counter:
        return counter["seq"]
    else:
        return ("Erro")
