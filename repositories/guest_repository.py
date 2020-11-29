from db.run_sql import run_sql
from models.guest import Guest
from models.room import Room
import repositories.room_repository as room_repository


# crud for guests
# create
def save(guest):
    sql = "INSERT INTO guests (name, type, race, room_id) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [guest.name, guest.type, guest.race, guest.room.id]
    results = run_sql(sql, values)
    guest.id = results[0]['id']
    return guest

# read all
def read_all():
    guests = []
    sql = "SELECT * FROM guests"
    results = run_sql(sql)

    for row in results:
        room = room_repository.read(row['room_id'])
        guest = Guest(row['name'], row['type'], row['race'], room, row['id'])
        guests.append(guest)
    return guests



# read one
# delete one
# delete all
# update 