from database import database

def get_current_sequence_value(sequence_name):
    sequence_document = database.get_database().get_collection('counters').find_one(
        {'_id': sequence_name}
    )
    if sequence_document:
        return sequence_document['sequence_value']
    else:
        return 0  # Retorna 0 se o contador ainda não existir

def increment_sequence_value(sequence_name):
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
