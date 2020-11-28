import pdb

from models.guest import Guest
from models.room import Room
from models.weapon import Weapon

import repositories.guest_repository as guest_repository
import repositories.room_repository as room_repository
import repositories.weapon_repository as weapon_repository

room_repository.delete_all()

room = Room('Baldurs Boudoir', 4)
room_repository.save(room)

room_repository.read_all()

pdb.set_trace()exit