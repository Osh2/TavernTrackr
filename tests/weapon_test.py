import unittest
from models.weapon import Weapon

class TestWeapon(unittest.TestCase):
    def setUp(self):
        self.weapon1 = Weapon('Orc Bane', 8, 'short sword', True, 250, 'Elron')

    def test_weapon_has_name(self):
        self.assertEqual('Orc Bane', self.weapon1.name)

    def test_weapon_has_stats(self):
        self.assertEqual(8, self.weapon1.damage)
        self.assertEqual(250, self.weapon1.value)
        self.assertEqual(True, self.weapon1.magic)
        self.assertEqual('short sword', self.weapon1.type)

    def test_weapon_has_owner(self):
        self.assertEqual('Elron', self.weapon1.owner)