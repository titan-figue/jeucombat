#!/usr/bin/python3
#Gestion degats

def gestionDegats(PVdef, Forceatk, Armuredef):
    if (Forceatk > Armuredef):
        return PVdef-(Forceatk-Armuredef)
    else:
        return PVdef-1