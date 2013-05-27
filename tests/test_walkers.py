import unittest

from mock import patch
from expecter import expect
import walkers
from walkers import ArtistWalker

class TestArtistWalkers(unittest.TestCase):
    
    @patch('walkers.subprocess.Popen')
    def it_splits_the_paths(self, Popen):
        Popen.return_value.communicate.return_value = ["/media/satshabad/Black Beauty/Music/SelectedMusic/22-20's\n/media/satshabad/Black Beauty/Music/SelectedMusic/_22_ & Bull Bama\n/media/satshabad/Black Beauty/Music/SelectedMusic/_22_ & group with axes\n/media/satshabad/Black Beauty/Music/SelectedMusic/_22_ & Group With Hoes\n/media/satshabad/Black Beauty/Music/SelectedMusic/3 Doors Down With Soul Children Of Chicago\n/media/satshabad/Black Beauty/Music/SelectedMusic/6 Day Riot\n/media/satshabad/Black Beauty/Music/SelectedMusic/_88_ & Group With Axes\n"]
        artistwalker = ArtistWalker()
        expect(artistwalker.artist_paths) == ["/media/satshabad/Black Beauty/Music/SelectedMusic/22-20's", '/media/satshabad/Black Beauty/Music/SelectedMusic/_22_ & Bull Bama', '/media/satshabad/Black Beauty/Music/SelectedMusic/_22_ & group with axes', '/media/satshabad/Black Beauty/Music/SelectedMusic/_22_ & Group With Hoes', '/media/satshabad/Black Beauty/Music/SelectedMusic/3 Doors Down With Soul Children Of Chicago', '/media/satshabad/Black Beauty/Music/SelectedMusic/6 Day Riot', '/media/satshabad/Black Beauty/Music/SelectedMusic/_88_ & Group With Axes', '']



