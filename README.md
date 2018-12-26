[![CircleCI build status](https://img.shields.io/circleci/project/github/AntoineAugusti/loto.svg?style=flat-square)](https://circleci.com/gh/AntoineAugusti/loto)
[![Software License](https://img.shields.io/badge/License-MIT-orange.svg?style=flat-square)](https://github.com/AntoineAugusti/loto/blob/master/LICENSE.md)

# Loto de la FDJ
Classe Python permettant de travailler avec les règles du Loto en France du 6 octobre 2008 au 6 mars 2017.

## Utilisation
```py
from loto import Loto, Tirage

# 1- Faire un tirage aléatoire d'une grille de Loto
boules, numero_chance = Tirage.random()
# boules : [5, 25, 1, 49, 3] (par exemple)
# numero_chance : 3 (par exemple)

# 2- Déterminer si on gagne et le rang du gain
loto = Loto(boules=[29, 25, 2, 39, 20], numero_chance=7)

rang = loto.rang(boules=[29, 25, 3, 39, 20], numero_chance=6)
# rang vaut 3 (4 bons numéros)
rang = loto.rang(boules=[24, 3, 1, 40, 5], numero_chance=6)
# rang vaut None, aucun bon numéro et numéro chance non trouvé

# 3- Déterminer le gain d'un tirage
gains = {
    1: 7000000,
    2: 485170.5,
    3: 1294.2,
    4: 11.5,
    5: 5.4,
    6: 2,
}

loto = Loto(boules=[29, 25, 2, 39, 20], numero_chance=7, gains=gains)
gain = loto.gains_tirage(boules=[29, 25, 3, 39, 20], numero_chance=7)
# gain vaut gains[3] + gains[6] : gains du rang 3 et du rang 6 car on a 4 bons numéros et le numéro chance est valide
```

## Licence
MIT
