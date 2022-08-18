#!/usr/bin/python3
# Generation Monstre
import random

def genMonstre(Nom):
    PV = random.randint(5, 2)
    Force = random.randint(3, 8)
    Armure = random.randint(0, 5)
    monmonstre = [Nom, PV, Force, Armure]
    return monmonstre