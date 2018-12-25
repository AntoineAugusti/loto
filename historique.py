# Faire un tirage aléatoire d'une grille de Loto
# Voir combien on aurait payé et gagné sur toute la période
from collections import defaultdict
import csv

from loto import Loto, Tirage

PRIX_GRILLE = 2

lotos = []
for row in csv.DictReader(open('loto.csv')):
    boules = list(map(int, row['boules'].split(',')))
    numero_chance = int(row['numero_chance'])
    gains = {}
    for i in range(1, 7):
        gains[i] = float(row['rapport_du_rang' + str(i)])
    lotos.append(Loto(boules, numero_chance, gains))

perso_boules, perso_numero_chance = Tirage.random()

historique_gains = []
depense = 0
rangs = defaultdict(int)

for loto in lotos:
    rang, _ = loto.rang(perso_boules, perso_numero_chance)

    historique_gains.append(loto.gains_tirage(perso_boules, perso_numero_chance))
    rangs[rang] += 1
    depense += PRIX_GRILLE

print('On joue : ', perso_boules, perso_numero_chance)
print('Résultat : ', depense, sum(historique_gains), max(historique_gains), rangs)
