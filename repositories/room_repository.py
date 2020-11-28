from db.run_sql import run_sql
from models.room import Room


# crud for room
# create
def save(room):
    sql = "INSERT INTO rooms (name, capacity) VALUES (%s, %s) RETURNING id"
    values = [room.name, room.capacity] 
    results = run_sql(sql, values)

    room.id=results[0]['id']
    return room 


# read all



# read one



# delete one



# delete all



# update 