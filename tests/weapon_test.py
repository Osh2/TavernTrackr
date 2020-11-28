import unittest
from models.weapon import Weapon

class TestWeapon(unittest.TestCase):
    def setUp(self):
        self.weapon1 = Weapon('Orc Bane', {'damage': 8, 'type':'short sword', 'magic': True, 'value':250}, 'Elron')

    def test_weapon_has_name(self):
        self.assertEqual('Orc Bane', self.weapon1.name)