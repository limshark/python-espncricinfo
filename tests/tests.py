import unittest
from espncricinfo.match import Match

class TestMatchMethods(unittest.TestCase):

    def setUp(self):
        id=857713
        print("setup completed", Match)
        self.match = Match(id)

    def test_match_description(self):
        print("test match description",self.match)
        self.assertEqual(self.match.description, 'Caribbean Premier League, 6th Match: St Lucia Zouks v Guyana Amazon Warriors at Gros Islet, Jun 26, 2015')

    def test_match_match_class(self):
        print("test match class",self.match)
        self.assertEqual(self.match.match_class, 'Twenty20')

    def test_toss_winner(self):
        print("test toss winner ",self.match)
        self.assertEqual(self.match.toss_winner, '5153')

if __name__ == '__main__':
    unittest.main()
