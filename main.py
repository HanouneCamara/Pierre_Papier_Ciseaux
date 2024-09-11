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
fenetre.geometry("400x300")
fenetre.configure(bg="#F0F0F0")

# Label pour les résultats
resultat = tk.StringVar()
label_resultat = tk.Label(fenetre, textvariable=resultat, font=("Arial", 14), bg="#F0F0F0")
label_resultat.pack(pady=20)

# Label pour le choix de l'ordinateur
label_choix_ordi = tk.Label(fenetre, text="L'ordinateur n'a pas encore choisi.", font=("Arial", 12), bg="#F0F0F0")
label_choix_ordi.pack(pady=10)

# Boutons pour les choix du joueur
bouton_pierre = tk.Button(fenetre, text="Pierre", font=("Arial", 12), command=lambda: jouer('Pierre'))
bouton_pierre.pack(side="left", padx=20, pady=20)

bouton_papier = tk.Button(fenetre, text="Papier", font=("Arial", 12), command=lambda: jouer('Papier'))
bouton_papier.pack(side="left", padx=20, pady=20)

bouton_ciseaux = tk.Button(fenetre, text="Ciseaux", font=("Arial", 12), command=lambda: jouer('Ciseaux'))
bouton_ciseaux.pack(side="left", padx=20, pady=20)

# Lancer la fenêtre
fenetre.mainloop()