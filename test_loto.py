# -*- coding: utf-8 -*-
import unittest

from loto import Loto, Tirage


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

    def test_gains(self):
        boules = Tirage.random_boules()
        numero_chance = Tirage.random_numero_chance()

        valid_values = [
            {1: 7000000, 2: 485170.5, 3: 1294.2, 4: 11.5, 5: 5.4, 6: 2},
            {1: 0, 2: 485170.5, 3: 1294.2, 4: 11.5, 5: 5.4, 6: 2},
            {1: 0, 2: 0, 3: 1294.2, 4: 11.5, 5: 5.4, 6: 2},
        ]

        for gains in valid_values:
            Loto(boules=boules, numero_chance=numero_chance, gains=gains)

        invalid_values = [
            {1: 7000000, 2: 485170.5, 3: 1294.2, 4: 11.5, 5: 5.4, 6: 0},
            {1: 0, 2: 485170.5, 3: 1294.2, 4: 11.5, 5: 5.4, 6: -2},
            {1: 0, 2: 0, 3: 1294.2, 4: 11.5, 5: 5.4, 6: 6},
        ]

        for gains in invalid_values:
            with self.assertRaises(ValueError):
                Loto(boules=boules, numero_chance=numero_chance, gains=gains)

    def test_rang(self):
        loto = Loto(boules=[29, 25, 2, 39, 20], numero_chance=7)

        tests = [
            ((1, True), {"boules": [29, 25, 2, 39, 20], "numero_chance": 7}),
            ((2, False), {"boules": [29, 25, 2, 39, 20], "numero_chance": 2}),
            ((3, False), {"boules": [29, 25, 3, 39, 20], "numero_chance": 6}),
            ((4, False), {"boules": [29, 25, 3, 40, 20], "numero_chance": 6}),
            ((5, False), {"boules": [25, 2, 3, 40, 5], "numero_chance": 2}),
            ((6, False), {"boules": [25, 3, 4, 40, 5], "numero_chance": 2}),
            ((6, True), {"boules": [24, 3, 2, 40, 5], "numero_chance": 7}),
            ((None, False), {"boules": [24, 3, 1, 40, 5], "numero_chance": 2}),
        ]

        for expected, args in tests:
            self.assertEquals(expected, loto.rang(**args))

    def test_gains_tirage(self):
        gains = {1: 7000000, 2: 485170.5, 3: 1294.2, 4: 11.5, 5: 5.4, 6: 2}

        loto = Loto(boules=[29, 25, 2, 39, 20], numero_chance=7, gains=gains)

        tests = [
            (gains[1], {"boules": [29, 25, 2, 39, 20], "numero_chance": 7}),
            (gains[2], {"boules": [29, 25, 2, 39, 20], "numero_chance": 2}),
            (gains[3], {"boules": [29, 25, 3, 39, 20], "numero_chance": 6}),
            (gains[3] + gains[6], {"boules": [29, 25, 3, 39, 20], "numero_chance": 7}),
            (gains[4], {"boules": [29, 25, 3, 40, 20], "numero_chance": 6}),
            (gains[4] + gains[6], {"boules": [29, 25, 3, 40, 20], "numero_chance": 7}),
            (gains[5], {"boules": [25, 2, 3, 40, 5], "numero_chance": 2}),
            (gains[5] + gains[6], {"boules": [25, 2, 3, 40, 5], "numero_chance": 7}),
            (gains[6], {"boules": [25, 3, 4, 40, 5], "numero_chance": 2}),
            (gains[6], {"boules": [24, 3, 2, 40, 5], "numero_chance": 7}),
            (0, {"boules": [24, 3, 1, 40, 5], "numero_chance": 2}),
        ]

        for expected, args in tests:
            self.assertEquals(expected, loto.gains_tirage(**args))


class TestTirage(unittest.TestCase):
    def test_est_valide(self):
        self.assertTrue(Tirage.est_valide([3, 5, 10, 13, 15], 3))
        self.assertTrue(Tirage.est_valide([1, 5, 10, 13, 49], 3))

        self.assertFalse(Tirage.est_valide([3, 3, 10, 13, 15], 3))
        self.assertFalse(Tirage.est_valide([1, 3, 10, 13, 50], 3))

    def test_random(self):
        set_numeros_chance = set()
        set_numeros = set()

        for _ in range(1, 1000):
            boules, numero_chance = Tirage.random()
            set_numeros_chance.add(numero_chance)
            set_numeros = set_numeros.union(set(boules))
            self.assertTrue(Tirage.est_valide(boules, numero_chance))

        self.assertEquals(set_numeros_chance, set(range(1, 11)))
        self.assertEquals(set_numeros, set(range(1, 50)))
