# Coordonnees.py

#
# - Définit les coordonnées d'une case
#
#  Une coordonnée est un tuple de deux entiers compris entre 0 (inclus) et const.DIM (exclus)
#  Elle peut aussi être None si elle est non définie
#

from model.Constantes import *


def type_coordonnees(c: tuple) -> bool:
    """
    Détermine si le tuple correspond à des coordonnées
    Les coordonnées sont sous la forme (ligne, colonne).
    Malheureusement, il n'est pas possible de tester si une inversion est faite entre ligne et colonne...

    :param c: coordonnées
    :return: True s'il s'agit bien de coordonnées, False sinon
    """
    return c is None or (type(c) == tuple and len(c) == 2 and 0 <= c[0] < const.DIM and 0 <= c[1] < const.DIM)
########################################################################################################################
def sontVoisins(coord1 : tuple, coord2 : tuple) -> bool :
    if not type_coordonnees(coord1) :
        raise ValueError(f"Le paramètre {coord1}  ne correspond pas à des coordonnées.")
    if (coord1 == None) :
        raise ValueError(f"Le paramètre {coord1}  ne correspond pas à des coordonnées.")

    if not type_coordonnees(coord2) :
        raise ValueError(f"Le paramètre {coord2}  ne correspond pas à des coordonnées.")
    if (coord2 == None) :
        raise ValueError(f"Le paramètre {coord2}  ne correspond pas à des coordonnées.")

    rep = False
    liCoord1 = coord1[0]
    coCoord1 = coord1[1]

# Création d'une liste avec toutes les cases voisines possible autour de la première coordonnée.
    coordVoisins = [
        [liCoord1 - 1, coCoord1 - 1],
        [liCoord1 - 1, coCoord1],
        [liCoord1 - 1, coCoord1 + 1],
        [liCoord1, coCoord1 - 1],
        [liCoord1, coCoord1],
        [liCoord1, coCoord1 + 1],
        [liCoord1 + 1, coCoord1 - 1],
        [liCoord1 + 1, coCoord1],
        [liCoord1 + 1, coCoord1 + 1]
    ]
    coord2List = list(coord2)
# S'assurer que la deuxième coordonnée est différente de la première et n'est pas présentes dans
# la liste des cases voisines de la première coordonnée.
    if coord1 != coord2 and coord2List in coordVoisins :
        rep = True
    return rep



