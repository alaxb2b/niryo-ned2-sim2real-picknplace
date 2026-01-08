### Programme Execution

##Importations des bibliothèques nécessaires

##Connexion au robot Niryo, calibration automatique et création de la pose Home
Robot = NiryoRobot("10.10.10.10")
Robot.calibrate_auto()
Robot.set_arm_max_velocity(100)
Home = Robot.get_pose()

##Fonction auxiliaire
def pickpandplaceniryo(X,Y):
    x1 = X[0]
    y1 = X[1]
    z1 = X[2]
    x2 = Y[0]/1000
    y2 = Y[1]/1000
    z2 = Y[2]/1000
    xn = PoseObject(x  = x1, y = y1,z = z1, roll = 0, pitch = 1.57, yaw = 0)
    yn = PoseObject(x  = x2, y = y2,z = z2, roll = 0, pitch = 1.57, yaw = 0)
    Robot.update_tool()
    Robot.release_with_tool()
    Robot.move_pose(xn)
    Robot.grasp_with_tool()
    Robot.move_pose(yn)
    Robot.release_with_tool()
    Robot.move_pose(Home)

def pyramideniryo(l,o):
  lunpy = []
  robot.update_tool()
  c = 0
  op = PoseObject(x  = o[0]/1000, y = o[1]/1000,z = o[2]/1000, roll = 0, pitch = 1.57, yaw = 0)
  for i in l:
    p = PoseObject(x  = i[0]/1000, y = i[1]/1000,z = i[2]/1000, roll = 0, pitch = 1.57, yaw = 0)
    Robot.release_with_tool()
    Robot.move_pose(i)
    Robot.grasp_with_tool()
    Robot.move_pose(Home)
    new_place_pose = o.copy_with_offsets(z_offset=0.01 * c)
    lunpy.append(new_place_pose)
    Robot.move_pose(new_place_pose)
    Robot.release_with_tool()
    Robot.move_pose(Home)
    c = c + 1
  for i in lunpy:
    Robot.release_with_tool()
    Robot.move_pose(lunpy[c-1])
    Robot.grasp_with_tool()
    Robot.move_pose(Home)
    Robot.move_pose(l[c-1])
    Robot.release_with_tool()
    Robot.move_pose(Home)
    c = c - 1

def execution(P,l,centrep):
    longueur = len(l)
    if P == "Pickandplace":
        c = 0
        while c+1 < longueur:
            pickpandplaceniryo(l[c],l[c+1])
    else:
        pyramideniryo(l,centrep)


def lecturefichier():
    with open("Données pour Niryo.txt", "r") as fichier:
        contenu = fichier.read()
    # Séparer les données
    Programme, Hauteur_string, Coordonnees_string, Centre_string = contenu.split("|")
    # Convertir les coordonnées en liste de listes de réels
    Coordonnees = [list(map(float, paire.strip("[]").split(','))) for paire in Coordonnees_string.split()]
    Hauteur = float(Hauteur_string)### Programme Execution

##Importations des bibliothèques nécessaires

##Connexion au robot Niryo, calibration automatique et création de la pose Home
Robot = NiryoRobot("10.10.10.10")
Robot.calibrate_auto()
Robot.set_arm_max_velocity(100)
Home = Robot.get_pose()

##Fonction auxiliaire
def pickpandplaceniryo(X,Y):
    x1 = X[0]
    y1 = X[1]
    z1 = X[2]
    x2 = Y[0]/1000
    y2 = Y[1]/1000
    z2 = Y[2]/1000
    xn = PoseObject(x  = x1, y = y1,z = z1, roll = 0, pitch = 1.57, yaw = 0)
    yn = PoseObject(x  = x2, y = y2,z = z2, roll = 0, pitch = 1.57, yaw = 0)
    Robot.update_tool()
    Robot.release_with_tool()
    Robot.move_pose(xn)
    Robot.grasp_with_tool()
    Robot.move_pose(yn)
    Robot.release_with_tool()
    Robot.move_pose(Home)

def pyramideniryo(l,o):
  lunpy = []
  robot.update_tool()
  c = 0
  op = PoseObject(x  = o[0]/1000, y = o[1]/1000,z = o[2]/1000, roll = 0, pitch = 1.57, yaw = 0)
  for i in l:
    p = PoseObject(x  = i[0]/1000, y = i[1]/1000,z = i[2]/1000, roll = 0, pitch = 1.57, yaw = 0)
    Robot.release_with_tool()
    Robot.move_pose(i)
    Robot.grasp_with_tool()
    Robot.move_pose(Home)
    new_place_pose = o.copy_with_offsets(z_offset=0.01 * c)
    lunpy.append(new_place_pose)
    Robot.move_pose(new_place_pose)
    Robot.release_with_tool()
    Robot.move_pose(Home)
    c = c + 1
  for i in lunpy:
    Robot.release_with_tool()
    Robot.move_pose(lunpy[c-1])
    Robot.grasp_with_tool()
    Robot.move_pose(Home)
    Robot.move_pose(l[c-1])
    Robot.release_with_tool()
    Robot.move_pose(Home)
    c = c - 1

def execution(P,l,centrep):
    longueur = len(l)
    if P == "Pickandplace":
        c = 0
        while c+1 < longueur:
            pickpandplaceniryo(l[c],l[c+1])
    else:
        pyramideniryo(l,centrep)


def lecturefichier():
    with open("Données pour Niryo.txt", "r") as fichier:
        contenu = fichier.read()
    # Séparer les données
    Programme, Hauteur_string, Coordonnees_string, Centre_string = contenu.split("|")
    # Convertir les coordonnées en liste de listes de réels
    Coordonnees = [list(map(float, paire.strip("[]").split(','))) for paire in Coordonnees_string.split()]
    Hauteur = float(Hauteur_string)
    Centre = ast.literal_eval(Centre_string)
    return Programme,Coordonnees, Hauteur, Centre

##Execution réelle
Programme = lecturefichier()[0]
Coordonnees = lecturefichier()[1]
Hauteur = lecturefichier()[2]
Centre = lecturefichier()[3]
execution(Programme, Coordonnees,Centre)

    Centre = ast.literal_eval(Centre_string)
    return Programme,Coordonnees, Hauteur, Centre

##Execution réelle
Programme = lecturefichier()[0]
Coordonnees = lecturefichier()[1]
Hauteur = lecturefichier()[2]
Centre = lecturefichier()[3]
execution(Programme, Coordonnees,Centre)
