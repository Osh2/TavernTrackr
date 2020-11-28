from db.run_sql import run_sql
from models.room import Room


def save(room):
    sql = "INSERT INTO rooms (name, capacity) VALUES (%s, %s) RETURNING id"
    values = [room.name, room.capacity] 
    results = run_sql(sql, values)

    room.id=results[0]['id']
    return room 



def read_all():
    rooms = []
    sql = "SELECT * FROM rooms"
    results = run_sql(sql)

    for row in results:
        room = Room(row['name'], row['capacity'], row['id'])
        rooms.append(room)
    return rooms 


def read(id):
    sql = "SELECT * FROM rooms WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    room = Room(result['name'], result['capacity'], result['id'])
    return room 



def delete(id):
    sql = "DELETE FROM rooms WHERE id = %s"
    values = [id]
    run_sql(sql, values)



def delete_all():
    sql = "DELETE FROM rooms"
    run_sql(sql)



def update(room):
    sql = "UPDATE rooms SET (name, capacity) = (%s, %s) WHERE id = %s"
    values = [room.name, room.capacity, room.id]
    run_sql(sql, values)