import unittest
from models.weapon import Weapon

class TestWeapon(unittest.TestCase):
    def setUp(self):
        self.weapon1 = Weapon('Orc Bane', {'damage': 8, 'type':'short sword', 'magic': True, 'value':250}, 'Elron')

    def test_weapon_has_name(self):
        self.assertEqual('Orc Bane', self.weapon1.name)

    def test_weapon_has_stats(self):
        self.assertEqual(8, self.weapon1.stats['damage'])
        self.assertEqual(250, self.weapon1.stats['value'])
        self.assertEqual(True, self.weapon1.stats['magic'])
        self.assertEqual('short sword', self.weapon1.stats['type'])