from db.run_sql import run_sql
from models.guest import Guest
from models.room import Room
from models.weapon import Weapon
import repositories.room_repository as room_repository




def save(guest):
    sql = "INSERT INTO guests (name, type, race, room_id) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [guest.name, guest.type, guest.race, guest.room.id]
    results = run_sql(sql, values)
    guest.id = results[0]['id']
    return guest


def read_all():
    guests = []
    sql = "SELECT * FROM guests"
    results = run_sql(sql)

    for row in results:
        room = room_repository.read(row['room_id'])
        guest = Guest(row['name'], row['type'], row['race'], room, row['id'])
        guests.append(guest)
    return guests

def read(id):
    guest = None
    sql = "SELECT * FROM guests WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        room = room_repository.read(result['room_id'])
        guest = Guest(result['name'], result['type'], result['race'], room, result['id'])
    return guest
 
def read_guests_weapons(id):
    weapons = []
    sql = "SELECT * FROM weapons WHERE owner_id = %s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        weapon = Weapon(row['name'], row['damage'], row['type'], row['magic'], row['value'], row['owner_id'], row['id'])
        weapons.append(weapon)
    return weapons


def delete(id):
    sql = "DELETE FROM guests WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM guests"
    run_sql(sql)


def update(guest):
    sql = "UPDATE guests SET (name, type, race, room_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [guest.name, guest.type, guest.race, guest.room.id, guest.id]
    print(values)
    run_sql(sql, values)