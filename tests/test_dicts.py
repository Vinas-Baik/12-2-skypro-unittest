import unittest
from utils import dicts


class TestArrs(unittest.TestCase):

    def test_get_val(self):
        self.assertEqual(dicts.get_val({"665932": "Baikalsk"}, "665932"), "Baikalsk")
        self.assertEqual(dicts.get_val({"665932": "Baikalsk"}, "665932", "git_unitest"), "Baikalsk")
        self.assertEqual(dicts.get_val({}, "665932", "git"), "git")
        self.assertEqual(dicts.get_val({}, "665932"), "git")
        self.assertEqual(dicts.get_val({}, "665932", "Irkutsk"), "Irkutsk")


