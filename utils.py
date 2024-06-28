from database import database

def get_next_sequence_value(sequence_name):
    sequence_document = database.get_database().get_collection('counters').find_one_and_update(
        {'_id': sequence_name},
        {'$inc': {'sequence_value': 1}},
        return_document=True,
        upsert=True
    )
    return sequence_document['sequence_value']

def decrement_sequence_value(sequence_name):
    sequence_document = database.get_database().get_collection('counters').find_one_and_update(
        {'_id': sequence_name},
        {'$inc': {'sequence_value': -1}},
        return_document=True,
        upsert=True
    )
    return sequence_document['sequence_value']
