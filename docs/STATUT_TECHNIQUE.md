# État du code et reproductibilité

Cette synthèse provient de l'inspection des sources présentes dans le dépôt. Aucun mouvement matériel ni simulation RoboDK n'a été lancé lors de la mise à jour documentaire.

| Fichier | État constaté |
|---|---|
| `ui_parametres.py` | Formulaire et écriture du fichier implémentés ; aucune validation de saisie |
| `simulation_robodk.py` | Prototype avec variables incohérentes et boucle incomplète |
| `execution_robot.py` | Code dupliqué, indentation invalide et imports absents |
| `demo_pyramide.py` | Noms de fonction et de robot incohérents ; arguments non définis au point d'appel |

## Points à corriger avant reproduction

1. **Boucles pick-and-place :** le compteur `c` n'est pas incrémenté dans les boucles de simulation et d'exécution.
2. **Simulation :** `Home` et `Homerobodk` sont utilisés de manière incohérente ; une pose RoboDK est également passée à une fonction prévue pour un triplet. L'import de `os` devrait être explicite.
3. **Exécution :** le fichier contient une duplication du programme et des lignes indentées hors bloc ; `NiryoRobot`, `PoseObject` et `ast` ne sont pas importés explicitement.
4. **Unités :** dans le pick-and-place réel, seule la destination est divisée par 1000. Il faut établir une convention unique et explicite pour les entrées et les poses.
5. **Empilement :** confusion entre listes et objets de pose, entre `robot` et `Robot`, et formules de hauteur différentes entre simulation et réel.
6. **Démonstration :** la fonction définie est `pyramideniryo`, mais l'appel utilise `pyramide` ; les poses sont définies à l'intérieur de la fonction.
7. **Cycle de vie :** isoler l'exécution matérielle dans une entrée explicite et garantir la fermeture de la connexion en cas d'erreur.

## Portée de la mise à jour

Documentation, index et présentation du dépôt. Les quatre fichiers Python et les deux PDF sont conservés sans modification. Le fichier vide `assets/test` a été retiré ; aucun média de démonstration n'était présent.
