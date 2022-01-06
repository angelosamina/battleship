# model/Manuel.py
#
from model.Joueur import type_joueur, getNomJoueur
from view import window


def placerBateauxManuel (joueur : dict) -> None :
    if not type_joueur(joueur):
        raise ValueError(f"Le paramètre {joueur} ne correspond pas à un joueur.")

    nomJoueur = getNomJoueur(joueur)

    window.afficher(joueur)
    window.display_message(f"{nomJoueur} : Placer vos bateaux")
    window.placer_bateaux()

    return None
########################################################################################################################
def choisirCaseTirManuel(joueur : dict) -> tuple :
    if not type_joueur(joueur):
        raise ValueError(f"Le paramètre {joueur} ne correspond pas à un joueur.")

    nomJoueur = getNomJoueur(joueur)

    window.afficher(joueur)
    window.display_message(f"{nomJoueur} : Choisissez la case où vous voulez tirer." )
    window.set_action(f"Choisissez la case de tir (bouton gauche")
    a = window.get_clicked_cell(2)
    return a
