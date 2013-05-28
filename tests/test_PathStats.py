import unittest
from expecter import expect
import mock

from stuff import PathStats

class TestPathStats(unittest.TestCase):
    
    def it_parses_the_artist_name(self):
        stats = PathStats('/home/satshabad/music/Led Zep')
        expect(stats.artist_name()) == "Led Zep"
