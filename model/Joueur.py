# Joueur.py

from model.Bateau import type_bateau, construireBateau, getCoordonneesBateau, peutPlacerBateau, sontVoisinsBateau, \
    reinitialiserBateau
from model.Constantes import *

#
# Un joueur est représenté par un dictionnaire contenant les couples (clé, valeur) suivants :
#  const.JOUEUR_NOM : Nom du joueur de type str
#  const.JOUEUR_LISTE_BATEAUX : Liste des bateaux du joueur
#  const.JOUEUR_GRILLE_TIRS : Grille des tirs sur les bateaux adverses
#  const.JOUEUR_GRILLE_ADVERSAIRE : une grille des tirs de l'adversaire pour tester la fonction de tir
#  de l'adversaire.
#
from model.Coordonnees import type_coordonnees
from model.Grille import *


def type_joueur(joueur: dict) -> bool:
    """
    Retourne <code>True</code> si la liste semble correspondre à un joueur,
    <code>false</code> sinon.

    :param joueur: Dictionnaire représentant un joueur
    :return: <code>True</code> si le dictionnaire représente un joueur, <code>False</code> sinon.
    """
    return type(joueur) == dict and len(joueur) >= 4 and \
        len([p for p in [ const.JOUEUR_NOM, const.JOUEUR_LISTE_BATEAUX, const.JOUEUR_GRILLE_TIRS] if p not in joueur]) == 0 and \
        type(joueur[const.JOUEUR_NOM]) == str and type(joueur[const.JOUEUR_LISTE_BATEAUX]) == list \
        and type_grille(joueur[const.JOUEUR_GRILLE_TIRS]) \
        and all(type_bateau(v) for v in joueur[const.JOUEUR_LISTE_BATEAUX])

########################################################################################################################
def construireJoueur(nom : str, nomBateaux : list) -> dict :
    bateauxJoueur = []
    for i in nomBateaux :
        a = construireBateau(i)
        bateauxJoueur.append(a)

    joueur = {
        const.JOUEUR_NOM : nom,
        const.JOUEUR_LISTE_BATEAUX : bateauxJoueur,
        const.JOUEUR_GRILLE_TIRS :construireGrille(),
        const.JOUEUR_GRILLE_ADVERSAIRE : construireGrille()
    }
    return joueur
########################################################################################################################
def getNomJoueur(joueur : dict) -> str :
    if not type_joueur(joueur) :
        raise ValueError(f"Le paramètre {joueur} ne correspond pas à un joueur.")
    nomJoueur = joueur.get(const.JOUEUR_NOM)
    return nomJoueur
########################################################################################################################
def getNombreBateauxJoueur(joueur : dict) -> int :
    if not type_joueur(joueur) :
        raise ValueError(f"Le paramètre {joueur} ne correspond pas à un joueur.")
    bateauxJoueur = joueur.get(const.JOUEUR_LISTE_BATEAUX)
    return len(bateauxJoueur)
########################################################################################################################
def getBateauxJoueur(joueur : dict) -> list :
    if not type_joueur(joueur):
        raise ValueError(f"Le paramètre {joueur} ne correspond pas à un joueur.")
    bateauxJoueur = joueur.get(const.JOUEUR_LISTE_BATEAUX)
    print(bateauxJoueur)
    return bateauxJoueur
########################################################################################################################
def getGrilleTirsJoueur(joueur : dict) -> list :
    if not type_joueur(joueur):
        raise ValueError(f"Le paramètre {joueur} ne correspond pas à un joueur.")
    grilleJoueur = joueur.get(const.JOUEUR_GRILLE_TIRS)
    return grilleJoueur

def getGrilleTirsAdversaire(joueur : dict) -> list :
    if not type_joueur(joueur):
        raise ValueError(f"Le paramètre {joueur} ne correspond pas à un joueur.")
    grilleJoueurAdvers = joueur.get(const.JOUEUR_GRILLE_ADVERSAIRE) 
    return grilleJoueurAdvers
########################################################################################################################
"""def placerBateauJoueur (joueur : dict, bateau : dict, first_case : tuple, pos :bool) -> bool :
    if not type_joueur(joueur):
        raise ValueError(f"Le paramètre {joueur} ne correspond pas à un joueur.")
    if not type_bateau(bateau) :
        raise ValueError(f"Le paramètre {bateau} ne correspond pas un bateau.")
    if not type_coordonnees(first_case):
        raise ValueError(f"Le paramètre {first_case} ne correspond pas à des coordonnées.")
    if first_case == None:
        raise ValueError(f"Le paramètre {first_case} ne correspond pas à des coordonnées.")
    if bateau not in joueur[const.JOUEUR_LISTE_BATEAUX] :
        raise RuntimeError (f"Le bateau {bateau} ne fais pas partis des bateaux du joueur. ")

    rep = True
    coordBateau = getCoordonneesBateau(bateau)

    for i in coordBateau:
        if i == None :
            rep = False

    if peutPlacerBateau(bateau,first_case,pos) :
        for i in joueur[const.JOUEUR_LISTE_BATEAUX] :
            if bateau not in joueur[const.JOUEUR_LISTE_BATEAUX]:
                if sontVoisinsBateau(i,bateau) :
                    rep = False
    return rep"""
########################################################################################################################
def reinitialiserBateauxJoueur(joueur : dict) -> None :
    if not type_joueur(joueur):
        raise ValueError(f"Le paramètre {joueur} ne correspond pas à un joueur.")
    for i in joueur[const.JOUEUR_LISTE_BATEAUX]:
        reinitialiserBateau(i)
    return None