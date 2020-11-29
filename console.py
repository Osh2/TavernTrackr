import pdb

from models.guest import Guest
from models.room import Room
from models.weapon import Weapon

import repositories.guest_repository as guest_repository
import repositories.room_repository as room_repository
import repositories.weapon_repository as weapon_repository

guest_repository.delete_all()
room_repository.delete_all()


room1 = Room('Baldurs Boudoir', 4)
room_repository.save(room1)
room2 = Room('Frog Suite', 2)
room_repository.save(room2)

guest1 = Guest('Gronk', 'Monk', 'Human', room1)
guest_repository.save(guest1)
guest2 = Guest('Boblin', 'Rogue', 'Goblin', room1)
guest_repository.save(guest2)
guest3 = Guest('Sara', 'Wizard', 'Human', room2)
guest_repository.save(guest3)


pdb.set_trace()