import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # Annetaan StatisticsServicelle stub-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_löytyy_pelaaja(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")

    def test_search_ei_löydä_pelaajaa(self):
        player = self.stats.search("Selänne")
        self.assertIsNone(player)

    def test_team_palauttaa_oikean_joukkueen(self):
        edmonton_players = self.stats.team("EDM")
        self.assertEqual(len(edmonton_players), 3)

    def test_top_palauttaa_parhaat(self):
        top_players = self.stats.top(1)
        # Gretzkyllä eniten pisteitä (35 + 89 = 124)
        self.assertEqual(top_players[0].name, "Gretzky")