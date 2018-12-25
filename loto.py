# -*- coding: utf-8 -*-
class Loto(object):
    def __init__(self, boules, numero_chance, gains=None):
        super(Loto, self).__init__()
        self.verifier_tirage(boules, numero_chance)

        self.tirage = {'boules': boules, 'numero_chance': numero_chance}
        self.gains = gains

    def gains_tirage(self, boules, numero_chance):
        rang, gagne_numero_change = self.rang(boules, numero_chance)

        if rang in [3, 4, 5] and gagne_numero_change:
            return self.gains[rang] + self.gains[6]
        elif rang is None:
            return 0
        else:
            return self.gains[rang]

    def verifier_tirage(self, boules, numero_chance):
        numero_chance_valide = numero_chance in range(1, 10)
        valide_boules = len(set(boules)) == 5 and all(map(lambda e: e in range(1, 50), boules))

        if not (numero_chance_valide and valide_boules):
            raise ValueError('Tirage invalide')

    def rang(self, boules, numero_chance):
        self.verifier_tirage(boules, numero_chance)

        intersect = set(self.tirage['boules']).intersection(set(boules))
        nombre_numeros = len(intersect)
        numero_chance_valide = numero_chance == self.tirage['numero_chance']

        rang = self.rang_grille(nombre_numeros, numero_chance_valide)

        return rang, numero_chance_valide

    def rang_grille(self, nombre_numeros, numero_chance_valide):
        if nombre_numeros == 5 and numero_chance_valide:
            return 1
        elif nombre_numeros == 5:
            return 2
        elif nombre_numeros == 4:
            return 3
        elif nombre_numeros == 3:
            return 4
        elif nombre_numeros == 2:
            return 5
        elif nombre_numeros == 1 or numero_chance_valide:
            return 6
        else:
            return None
