from db.run_sql import run_sql
from models.guest import Guest
from models.room import Room


# crud for guests
# create
def save(guest):
    sql = "INSERT INTO guests (name, type, race, room_id) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [guest.name, guest.type, guest.race, guest.room.id]
    results = run_sql(sql, values)
    guest.id = results[0]['id']
    return guest

# read all



# read one
# delete one
# delete all
# update 