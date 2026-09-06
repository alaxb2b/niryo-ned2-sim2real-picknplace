# Environnement et format des données

## Composants

| Composant | Prérequis |
|---|---|
| Interface | Python 3, Tkinter et session graphique |
| Simulation | RoboDK, API Python RoboDK et fichier externe `Niryo-Ned2.robot` |
| Robot | PyNiryo, connexion au Ned2, configuration et repères adaptés au poste |

Aucune version exacte de l'environnement d'origine n'est figée dans le dépôt. Le modèle RoboDK et les paramètres d'une station opérationnelle ne sont pas fournis.

## Interface Tkinter

Depuis la racine, lancer `python scripts/ui_parametres.py`. Le formulaire écrit quatre champs séparés par `|` dans `Données pour Niryo.txt` :

```text
Programme|Hauteur|Coordonnees|Centre
```

Exemple de **syntaxe**, destiné à la lecture du format :

```text
Pickandplace|0|[300,200,300] [200,200,200]|[300,200,300]
```

- Les noms prévus sont `Pickandplace` et `Pyramide`, avec cette casse.
- Le lecteur sépare les points par les espaces : ne pas insérer d'espaces à l'intérieur d'un triplet.
- Le centre doit être une liste compatible avec `ast.literal_eval`.
- Le formulaire ne contrôle ni les nombres, ni le nombre de points, ni l'espace de travail.
- Les coordonnées de l'exemple ne sont pas des poses validées pour une cellule réelle.

## Simulation et robot

Le prototype RoboDK recherche le modèle et le fichier de paramètres à partir du répertoire courant. Le prototype PyNiryo contient l'adresse `10.10.10.10` en dur et tente une calibration dès l'exécution de son code de connexion.

Avant de remettre ces composants en service, traiter les points du [statut technique](STATUT_TECHNIQUE.md), notamment les unités, les boucles et les noms de variables. La présence du code ne garantit pas une exécution fonctionnelle. Ne pas importer les modules matériels pour une simple inspection : certains exécutent des actions au niveau global.

Pour le travail sur matériel, se référer à la [fiche de sécurité fournie](FicheDeSecuriteNed2%20%281%29.pdf) et aux procédures du poste.
