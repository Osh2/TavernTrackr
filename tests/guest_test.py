import unittest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest('Elron', 'Rogue', 'Elf')


    def test_guest_has_name(self):
        self.assertEqual('Elron', self.guest1.name)