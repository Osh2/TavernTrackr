import unittest
from models.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room('The Pit', 10)


    def test_room_has_name(self):
        self.assertEqual('The Pit', self.room1.name)
