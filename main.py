import tkinter as tk
import random

# Fonction pour jeu
def jouer(choix_joueur):
    choix_ordi = random.choice(['Pierre', 'Papier', 'Ciseaux'])
    label_choix_ordi.config(text=f"L'ordinateur a choisi : {choix_ordi}")
    
     # Déterminer le gagnant
    if choix_joueur == choix_ordi :
        resultat.set("Égalité !")
    elif (choix_joueur == 'Pierre' and choix_ordi == 'Ciseaux') or \
        (choix_joueur == 'Papier' and choix_ordi == 'Pierre') or \
        (choix_joueur == 'Ciseaux' and choix_ordi == 'Papier'):
        resultat.set("Vous avez gagné ! 🎉")
    else:
        resultat.set("Vous avez perdu ! 😞")

# Interface graphique
fenetre = tk.Tk()
fenetre.title("Pierre-Papier-Ciseaux")
fenetre

# Lancer la fenêtre
fenetre.mainloop()