from bottle import post, request
from datastore import things


@post("/things")
def add_thing(db):
    new_thing = request.json
    if not new_thing:
        return {"error": "Invalid input"}
    things.add_new_thing(db, new_thing)
    return {"message": "Thing added successfully"}
