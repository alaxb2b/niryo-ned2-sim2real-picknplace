# niryo-ned2-sim2real-pickplace

**Projet robotique Niryo Ned2 (Python) — saisie de paramètres (Tkinter) → simulation RoboDK → exécution réelle PyNiryo. Démo pick-and-place et pyramide, approche sim2real avec validation en simulation avant déploiement.**

**Cours :** EA Systèmes Avancés — Projet de qualification fonctionnelle d'une plateforme robotique collaborative  
**Institution :** INSA Centre Val de Loire  
**Étudiants :** Alae Zerrouq, Adam Aoubiza  
**Encadrant :** Vincent Idasiak

---

## Objectif

Ce dépôt propose un workflow complet **simulation → réel** pour exécuter des mouvements sur un robot Niryo Ned2 :

1. Saisie des paramètres via une interface utilisateur Tkinter
2. Simulation des trajectoires dans RoboDK
3. Exécution réelle sur le robot via PyNiryo

Deux modes sont pris en charge :

- `Pickandplace` : enchaînement de mouvements entre paires de coordonnées
- `Pyramide` : construction et déconstruction d'une pyramide d'objets autour d'un centre

---

## Structure du projet

```
├── scripts/
│   ├── ui_parametres.py        # Interface Tkinter — saisie des paramètres
│   ├── simulation_robodk.py    # Simulation des trajectoires dans RoboDK
│   ├── execution_robot.py      # Exécution réelle sur le robot Niryo Ned2
│   └── demo_pyramide.py        # Script de démonstration du mode pyramide
├── docs/
│   └── Rapport-Final.pdf       # Rapport complet du projet
├── assets/                     # GIFs et captures d'écran (à compléter)
└── README.md
```

---

## Prérequis

### Simulation (RoboDK)
- RoboDK installé + API Python RoboDK (fournie avec RoboDK)
- Fichier robot Niryo Ned2 (`.robot`) téléchargé depuis la bibliothèque RoboDK

### Exécution réelle (Niryo)
- Robot Niryo Ned2 accessible sur le réseau (IP par défaut : `10.10.10.10`)
- PyNiryo installé : `pip3 install pyniryo`
- NiryoStudio ouvert et connecté au robot
- Zone de travail dégagée + opérateur prêt à l'arrêt d'urgence

---

## Guide d'utilisation

### Étape 1 — Saisir les paramètres (UI)

Lance l'interface Tkinter, remplis les champs (programme, coordonnées, hauteur, centre), puis clique sur **Valider** et ferme la fenêtre.

```bash
python scripts/ui_parametres.py
```

Exemple de saisie :
- Programme : `Pickandplace` ou `Pyramide`
- Coordonnées : `[300,200,300] [200,200,200]`
- Hauteur : `0`
- Centre (pour le mode Pyramide) : `[300,200,300]`

---

### Étape 2 — Simuler dans RoboDK

Lance la simulation pour visualiser les trajectoires avant tout déploiement réel.

```bash
python scripts/simulation_robodk.py
```

RoboDK s'ouvre et le robot Ned2 effectue les mouvements demandés en simulation.

---

### Étape 3 — Exécuter sur le robot réel

Une fois la simulation validée, lance l'exécution réelle avec NiryoStudio ouvert en parallèle.

```bash
python scripts/execution_robot.py
```

> ⚠️ **Sécurité** : une personne doit rester à proximité du bouton d'arrêt d'urgence pendant toute l'exécution. Dégager la zone de travail avant de lancer le script.

---

## Sécurité

Ce projet a été développé avec une attention particulière aux mesures de sécurité liées à l'utilisation d'un bras robotique collaboratif. La fiche de sécurité complète du Niryo Ned2 est incluse dans ce dépôt (`docs/FicheDeSecurite.pdf`).

---

## Rapport

Le rapport complet du projet est disponible ici : [`docs/Rapport-Final.pdf`](./docs/Rapport-Final-S7_Projet-EA-SA_Niryo-Ned2.pdf)
