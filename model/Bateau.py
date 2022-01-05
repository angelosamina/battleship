# Bateau.py

#
# - Définit un bateau sous forme de dictionnaire de la façon suivante :
#   const.BATEAU_NOM : Nom du bateau (voir les constantes dans Constantes.py - clés du dictionnaire const.BATEAUX_CASES)
#   const.BATEAU_SEGMENTS - Liste de listes [coordonnées, état] des segments du bateau.
#       Si le bateau n'est pas positionné, les coordonnées valent None et les états valent const.RATE
#   La taille du bateau n'est pas stockée car elle correspond à la taille de la liste des listes [coordonnées, état]
#
from model.Coordonnees import type_coordonnees
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

def est_horizontal_bateau(bateau: dict) -> bool:
    """
    Retourne True si le bateau est horizontal, False si il est vertical.

    :param bateau:
    :return: True si le bateau est horizontal, False si il est vertical
    :raise ValueError si le bateau n'est pas placé ou s'il n'est ni vertical, ni horizontal
    """
    if not estPlaceBateau(bateau):
        raise ValueError("est_horizontal_bateau: Le bateau n'est pas positionné")
    pos = getCoordonneesBateau(bateau)
    res = True
    if len(pos) > 1:
        # Horizontal : le numéro de ligne ne change pas
        res = pos[0][0] == pos[1][0]
        # On vérifie que le bateau est toujours horizontal
        for i in range(1, len(pos)):
            if (res and pos[0][0] != pos[i][0]) or (not res and pos[0][1] != pos[i][1]):
                raise ValueError("est_horizontal_bateau: Le bateau n'est ni horizontal, ni vertical ??")
    return res

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
def getSegmentsBateau (bateau : dict) -> list :
    if not type_bateau(bateau) :
        raise ValueError(f"Le paramètre {bateau} n’est pas un bateau.")
    lst = []
    a = bateau.get(const.BATEAU_SEGMENTS)
    for i in range(len(a)) :
        lst.append(a[i])
    return lst
########################################################################################################################
def getSegmentBateau (bateau : dict, n : object) -> dict :
    i = 0
    b = 0
    # On verifie si c'est un bateau
    if not type_bateau(bateau) :
        raise ValueError(f"Le paramètre {bateau} n’est pas un bateau.")

    # Si n est de type int, on vérifie s'il est bel et bien compris entre 0 et taille
    # du bateau – 1 sinon on lance une erreur puis on récupère le segment
    if type (n) == int:
        if n < 0 or n > getTailleBateau (bateau) -1 :
            raise ValueError(f"le paramètre {n} n’est pas valide")
        a = bateau[const.BATEAU_SEGMENTS]
        segment = a[n]

    # Si n est un tuple, on vérifie s'il est bel et bien de type coordonnée
    # sinon on lance une erreur puis on cherche n dans la liste et on renvoie
    # le segment correspondant

    elif type(n) == tuple:
        if type_coordonnees(n) == True:
            a = bateau[const.BATEAU_SEGMENTS]
            while(i < len(a) and b == 0) :
                if a[i][const.SEGMENT_COORDONNEES] == n :
                    b = 1
                    segment = a[i]
                i += 1
            if b != 1 :
                raise ValueError(f"Le paramettre {type(n)} ne correspond pas")
    else :
        raise ValueError(f"Le type du second paramètre {type(n)} ne correspond pas…")
    return segment

########################################################################################################################
def setSegmentBateau (bateau : dict, n : int, segment : dict ) -> None :
    if not type_bateau(bateau) :
        raise ValueError(f"Le paramètre {bateau} n’est pas un bateau.")

    if n < 0 or n > getTailleBateau (bateau) -1 :
        raise ValueError(f"Le paramètre {n} n'est pas compris entre 0 et la taille du bateau – 1 ")

    if not type_segment(segment) :
        raise ValueError(f"Le paramètre {segment} n’est pas de type Segment.")

    a = bateau[const.BATEAU_SEGMENTS]
    a[n] = segment

    return None

