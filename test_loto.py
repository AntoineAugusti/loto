# -*- coding: utf-8 -*-
import unittest

from loto import Loto


class TestLoto(unittest.TestCase):
    def test_constructeur_valide(self):
        Loto(boules=[29, 25, 2, 39, 20], numero_chance=7)

        with self.assertRaises(ValueError):
            Loto(boules=[], numero_chance=7)

        with self.assertRaises(ValueError):
            Loto(boules=[29, 25, 2, 39], numero_chance=7)

        with self.assertRaises(ValueError):
            Loto(boules=[29, 25, 2, 39, 50], numero_chance=7)

        with self.assertRaises(ValueError):
            Loto(boules=[29, 25, 2, 39, 49], numero_chance=0)

    def test_rang(self):
        loto = Loto(boules=[29, 25, 2, 39, 20], numero_chance=7)

        self.assertEquals(
            (1, True),
            loto.rang(boules=[29, 25, 2, 39, 20], numero_chance=7)
        )

        self.assertEquals(
            (2, False),
            loto.rang(boules=[29, 25, 2, 39, 20], numero_chance=2)
        )

        self.assertEquals(
            (3, False),
            loto.rang(boules=[29, 25, 3, 39, 20], numero_chance=6)
        )

        self.assertEquals(
            (4, False),
            loto.rang(boules=[29, 25, 3, 40, 20], numero_chance=6)
        )

        self.assertEquals(
            (5, False),
            loto.rang(boules=[25, 2, 3, 40, 5], numero_chance=2)
        )

        self.assertEquals(
            (6, False),
            loto.rang(boules=[25, 3, 4, 40, 5], numero_chance=2)
        )

        self.assertEquals(
            (6, True),
            loto.rang(boules=[24, 3, 2, 40, 5], numero_chance=7)
        )

        self.assertEquals(
            (None, False),
            loto.rang(boules=[24, 3, 1, 40, 5], numero_chance=2)
        )

    def test_gains_tirage(self):
        gains = {
            1: 7000000,
            2: 485170.5,
            3: 1294.2,
            4: 11.5,
            5: 5.4,
            6: 2,
        }

        loto = Loto(boules=[29, 25, 2, 39, 20], numero_chance=7, gains=gains)

        self.assertEquals(
            gains[1],
            loto.gains_tirage(boules=[29, 25, 2, 39, 20], numero_chance=7)
        )

        self.assertEquals(
            gains[2],
            loto.gains_tirage(boules=[29, 25, 2, 39, 20], numero_chance=2)
        )

        self.assertEquals(
            gains[3],
            loto.gains_tirage(boules=[29, 25, 3, 39, 20], numero_chance=6)
        )

        self.assertEquals(
            gains[3] + gains[6],
            loto.gains_tirage(boules=[29, 25, 3, 39, 20], numero_chance=7)
        )

        self.assertEquals(
            gains[4],
            loto.gains_tirage(boules=[29, 25, 3, 40, 20], numero_chance=6)
        )

        self.assertEquals(
            gains[4] + gains[6],
            loto.gains_tirage(boules=[29, 25, 3, 40, 20], numero_chance=7)
        )

        self.assertEquals(
            gains[5],
            loto.gains_tirage(boules=[25, 2, 3, 40, 5], numero_chance=2)
        )

        self.assertEquals(
            gains[5] + gains[6],
            loto.gains_tirage(boules=[25, 2, 3, 40, 5], numero_chance=7)
        )

        self.assertEquals(
            gains[6],
            loto.gains_tirage(boules=[25, 3, 4, 40, 5], numero_chance=2)
        )

        self.assertEquals(
            gains[6],
            loto.gains_tirage(boules=[24, 3, 2, 40, 5], numero_chance=7)
        )

        self.assertEquals(
            0,
            loto.gains_tirage(boules=[24, 3, 1, 40, 5], numero_chance=2)
        )
