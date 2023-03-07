import unittest
from bump_version import *

class TestBumpVersion(unittest.TestCase):
    def test_ci_patch(self):
        self.assertEqual(bump_version('1.0.0', 'ci: this is sample message'), '1.0.1')
    def test_chore_patch(self):
        self.assertEqual(bump_version('1.0.1', 'chore: this is another message'), '1.0.2')
    def test_feat_minor(self):
        self.assertEqual(bump_version('1.0.2', 'feat: New shiny feature'), '1.1.0')
    def test_feature_minor(self):
        self.assertEqual(bump_version('3.2.0', 'feat: New shiny feature'), '3.3.0')
    def test_minor_minor(self):
        self.assertEqual(bump_version('1.9.2', 'feat: New shiny feature'), '1.10.0')
    def test_breaking_major(self):
        self.assertEqual(bump_version('1.1.0', 'breaking: This is a breaking change'), '2.0.0')
    def test_major_major(self):
        self.assertEqual(bump_version('2.2.1', 'major: This is a major change'), '3.0.0')
    def test_default(self):
        self.assertEqual(bump_version('4.2.3', 'anything: This is a major change'), '4.2.4')

if __name__ == '__main__':
    unittest.main()