### Programme Simulation

##Importations des bibliothèques nécessaires

from robodk.robolink import *
from robodk.robomath import *
from tkinter import *
import ast

#Fonction auxiliaire pour trouver le fichier avec son titre
nomfichier = "Niryo-Ned2.robot"
repertoire = os.getcwd()
def find_file(filename):
    for root, dirs, files in os.walk(repertoire):
        if filename in files:
            return os.path.join(root, filename)
    return None
robot_file_path = find_file(nomfichier)
##Fonctions auxiliaires
# #Programme de mouvement à une coordonnée donnée
def mouvrobodk(X):
    x = X[0]
    y = X[1]
    z = X[2]
    objet = Ned2robodk.AddTarget("Position souhaitée")
    Ned2robodk.ShowRoboDK()
    obj = Pose(x, y, z, -180.0, 0.0, 180.0)
    robot.MoveJ(obj)

def pickandplacerobodk(X,Y):
    mouvrobodk(X)
    mouvrobodk(Y)
    mouvrobodk(Homerobodk)

def pyramiderobodk(l,o):
  lunpy = []
  c = 0
  for i in l:
    mouvrobodk(i)
    mouvrobodk(Home)
    new_place_pose = [o[0],o[1],o[2]*c*Hauteur]
    lunpy.append(new_place_pose)
    mouvrobodk(new_place_pose)
    mouvrobodk(Home)
    c = c + 1
  for i in lunpy:
    mouvrobodk(lunpy[c-1])
    mouvrobodk(Home)
    mouvrobodk(l[c-1])
    mouvrobodk(Home)
    c = c - 1

def simu(P,l,centrep):
    longueur = len(l)
    if P == "Pickandplace":
        c = 0
        while c+1 < longueur:
            pickandplacerobodk(l[c],l[c+1])
    else:
        pyramiderobodk(l,centrep)

def lecturefichier():
    with open(find_file("Données pour Niryo.txt"), "r") as fichier:
        contenu = fichier.read()
    # Séparer les données
    Programme, Hauteur_string, Coordonnees_string, Centre_string = contenu.split("|")
    # Convertir les coordonnées en liste de listes de réels
    Coordonnees = [list(map(float, paire.strip("[]").split(','))) for paire in Coordonnees_string.split()]
    Hauteur = float(Hauteur_string)
    Centre = ast.literal_eval(Centre_string)
    return Programme,Coordonnees, Hauteur, Centre

##Ouverture de la fenêtre Robodk
Ned2robodk = Robolink()
Ned2robodk.ShowRoboDK()

#Ajout du robot Ned2 et de sa position Home
Ned2robodk.AddFile(robot_file_path)
robot = Ned2robodk.Item('', ITEM_TYPE_ROBOT)
Homerobodk = robot.Pose()

Programme = lecturefichier()[0]
Coordonnees = lecturefichier()[1]
Hauteur = lecturefichier()[2]
Centre = lecturefichier()[3]
simu(Programme,Coordonnees, Centre)


mouvrobodk(Homerobodk)




