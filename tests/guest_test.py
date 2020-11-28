import unittest
from models.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest('Elron', 'Rogue', 'Elf', 'The Pit')


    def test_guest_has_name(self):
        self.assertEqual('Elron', self.guest1.name)

    def test_guest_has_type(self):
        self.assertEqual('Rogue', self.guest1.type)

    def test_guest_has_race(self):
        self.assertEqual('Elf', self.guest1.race)

    def test_guest_has__room(self):
        self.assertEqual('The Pit', self.guest1.room)