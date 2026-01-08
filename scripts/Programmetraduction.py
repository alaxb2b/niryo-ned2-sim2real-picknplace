##Import des bibliothèques de os et tkinter
from tkinter import *
import os

#Programme de création de stockage des données
def creamodif():
    pg = programme.get()
    coord = coordonnees.get()
    Hauteur = hauteur.get()
    Centre = centre.get()
    with open("Données pour Niryo.txt", 'w') as fichier:
        fichier.write(pg + "|" + Hauteur + "|" + coord + "|" + Centre)
        fichier.close()

##Création de la fenêtre pour saisir les données
fenetre = Tk()
fenetre.title("Simulation et exécution d'un programme de mouvements sur le robot Ned2'")
fenetre.resizable(width=False, height=False)
label = Label(fenetre, text="Bonjour, voici les données à entrer :")
label.pack()
label = Label(fenetre, text="Programme à utiliser :")
label.pack()
programme = Entry(fenetre, width=30)
programme.pack()
label = Label(fenetre, text="Coordonnées :")
label.pack()
coordonnees = Entry(fenetre, width=30)
coordonnees.pack()
label = Label(fenetre, text="Hauteur de l'objet' :")
label.pack()
hauteur = Entry(fenetre, width=30)
hauteur.pack()
label = Label(fenetre, text="Centre pour la pyramide :")
label.pack()
centre = Entry(fenetre, width=30)
centre.pack()
label = Label(fenetre, text="Une fois validée, fermer la fenêtre.")
label.pack()
button = Button(fenetre, text="Valider", command=creamodif)
button.pack()
fenetre.mainloop()












