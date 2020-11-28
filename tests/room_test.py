import unittest
from models.room import Room
from models.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room('The Pit', 10)


    def test_room_has_name(self):
        self.assertEqual('The Pit', self.room1.name)

    def test_room_has_capacity(self):
        self.assertEqual(10, self.room1.capacity)

    def test_room_has_guests(self):
        self.guest1 = Guest('Cliff', 'Fighter', 'Dwarf', self.room1.name)
        self.room1.check_in_guest(self.guest1)
        self.assertEqual(1, len(self.room1.guests))
        self.assertEqual('The Pit', self.guest1.room)

    