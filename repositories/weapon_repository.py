from db.run_sql import run_sql
from models.weapon import Weapon
from models.guest import Guest
import repositories.guest_repository as guest_repository


# crud for weapon 
# create
def save(weapon):
    sql = "INSERT INTO weapons (name, damage, type, magic, value, owner_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [weapon.name, weapon.damage, weapon.type, weapon.magic, weapon.value, weapon.owner.id]
    results = run_sql(sql, values)
    weapon.id = results[0]['id']
    return weapon 

# read all
# read one
# delete one
# delete all
# update 