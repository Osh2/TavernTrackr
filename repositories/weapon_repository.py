from db.run_sql import run_sql
from models.weapon import Weapon
from models.guest import Guest
import repositories.guest_repository as guest_repository



def save(weapon):
    sql = "INSERT INTO weapons (name, damage, type, magic, value, owner_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [weapon.name, weapon.damage, weapon.type, weapon.magic, weapon.value, weapon.owner.id]
    results = run_sql(sql, values)
    weapon.id = results[0]['id']
    return weapon 


def read_all():
    weapons = []
    sql = "SELECT * FROM weapons"
    results = run_sql(sql)

    for row in results:
        owner = guest_repository.read(row['owner_id'])
        weapon = Weapon(row['name'], row['damage'], row['type'], row['magic'], row['value'], owner, row['id'])
        weapons.append(weapon)
    return weapons


def read(id):
    weapon = None
    sql = "SELECT * FROM weapons WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        owner = guest_repository.read(result['owner_id'])
        weapon = Weapon(result['name'], result['damage'], result['type'], result['magic'], result['value'], owner, result['id'])
    return weapon


def delete(id):
    sql = "DELETE FROM weapons WHERE id = %s"
    values = [id]
    run_sql(sql,values)


def delete_all():
    sql = "DELETE FROM weapons"
    run_sql(sql)


def update(weapon):
    sql = "UPDATE weapons SET (name, damage, type, magic, value, owner_id) = (%s,%s, %s, %s, %s, %s) WHERE id = %s"
    values = [weapon.name, weapon.damage, weapon.type, weapon.magic, weapon.value, weapon.owner.id, weapon.id]
    print (values)
    run_sql(sql, values)

def read_weapons_by_magic(magic_status):
    weapons = []
    sql = "SELECT * FROM weapons WHERE magic = %s"
    values = [magic_status]
    results = run_sql(sql, values)

    for row in results:
        owner = guest_repository.read(row['owner_id'])
        weapon = Weapon(row['name'], row['damage'], row['type'], row['magic'], row['value'], owner, row['id'])
        weapons.append(weapon)
    return weapons
