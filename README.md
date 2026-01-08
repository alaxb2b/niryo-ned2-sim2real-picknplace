# niryo-ned2-sim2real-picknplace

Projet robotique Niryo Ned2 (Python) : saisie de paramètres (Tkinter) → simulation RoboDK → exécution réelle PyNiryo. Démo pick-and-place et “pyramide”, approche sim2real et validation en simulation avant déploiement.

---

## Objectif

Ce dépôt propose un workflow **simulation → réel** pour exécuter des mouvements sur un robot **Niryo Ned2** :

1) saisie des paramètres via une **UI Tkinter**  
2) **simulation** des trajectoires dans **RoboDK**  
3) **exécution réelle** sur le robot via **PyNiryo**

Deux modes sont gérés :
- `Pickandplace` : enchaînement de mouvements entre paires de coordonnées
- `Pyramide` : construction/déconstruction autour d’un centre (mode utilisé quand `Programme != "Pickandplace"`)

---

## Démonstration

- `assets/demo_simulation.gif` : simulation RoboDK  
- `assets/demo_reel.gif` : robot réel  
- `assets/ui.png` : capture UI Tkinter  

---

## Prérequis

### Simulation (RoboDK)
- RoboDK installé + API Python RoboDK disponible (fournie avec RoboDK)
- Robot/station configuré (ex. robot Niryo Ned2 dans RoboDK)

### Exécution réelle (Niryo)
- Robot Niryo Ned2 accessible sur le réseau (IP à renseigner dans le script)
- PyNiryo installé
- Zone de travail dégagée + arrêt d’urgence prêt

---

## Guide d’utilisation

### 1) Générer les paramètres (UI)
Lance l’interface Tkinter, remplis les champs, puis génère le fichier de paramètres.

```bash
python scripts/ui_parametres.py
