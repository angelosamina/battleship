# Bateau.py

#
# - Définit un bateau sous forme de dictionnaire de la façon suivante :
#   const.BATEAU_NOM : Nom du bateau (voir les constantes dans Constantes.py - clés du dictionnaire const.BATEAUX_CASES)
#   const.BATEAU_SEGMENTS - Liste de listes [coordonnées, état] des segments du bateau.
#       Si le bateau n'est pas positionné, les coordonnées valent None et les états valent const.RATE
#   La taille du bateau n'est pas stockée car elle correspond à la taille de la liste des listes [coordonnées, état]
#

from model.Segment import type_segment, construireSegment
from model.Constantes import *



def type_bateau(bateau: dict) -> bool:
    """
    Détermine si la liste représente un bateau

    :param bateau: Liste représentant un bateau
    :return: <code>True</code> si la liste contient bien un bateau, <code>False</code> sinon.
    """
    return type(bateau) == dict and \
        all([v in bateau for v in [const.BATEAU_NOM, const.BATEAU_SEGMENTS]]) and \
        type(bateau[const.BATEAU_NOM]) == str and \
        bateau[const.BATEAU_NOM] in const.BATEAUX_CASES and type(bateau[const.BATEAU_SEGMENTS]) == list and \
        len(bateau[const.BATEAU_SEGMENTS]) == const.BATEAUX_CASES[bateau[const.BATEAU_NOM]] and \
        all([type_segment(s) for s in bateau[const.BATEAU_SEGMENTS]])

########################################################################################################################
def construireBateau (nom : str) -> dict :
    if not nom in const.BATEAUX_CASES :
        raise ValueError(f"Le paramètre {nom} n’est pas un nom.")
    lst = []
    for i in range(const.BATEAUX_CASES[nom]) :
        a = construireSegment()
        lst.append(a)
    bateau ={
        const.BATEAU_NOM : nom,
        const.BATEAU_SEGMENTS : lst
    }
    return bateau
########################################################################################################################
def getNomBateau (bateau : dict) -> str :
    if not type_bateau(bateau) :
        raise ValueError(f"Le paramètre {bateau} n’est pas un bateau.")
    nomBateau = bateau.get(const.BATEAU_NOM)
    return nomBateau
########################################################################################################################
def getTailleBateau (bateau : dict) -> list :
    if not type_bateau(bateau) :
        raise ValueError(f"Le paramètre {bateau} n’est pas un bateau.")
    taille = len(bateau.get(const.BATEAU_SEGMENTS))
    return taille
########################################################################################################################


