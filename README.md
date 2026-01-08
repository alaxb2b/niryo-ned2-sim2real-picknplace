# niryo-ned2-sim2real-picknplace
Projet robotique Niryo Ned2 (Python) : saisie paramètres (Tkinter) → simulation RoboDK → exécution réelle PyNiryo. Démo pick-and-place et “pyramide”, approche sim2real et validation avant déploiement.

Ce dépôt contient un mini-workflow **sim → réel** pour exécuter des mouvements sur un robot **Niryo Ned2** :
1) saisie des paramètres via une **UI Tkinter**,  
2) **simulation** des trajectoires dans **RoboDK**,  
3) **exécution réelle** sur le robot via **PyNiryo**.

Deux modes sont gérés :
- `Pickandplace` : enchaînement de mouvements entre paires de coordonnées,
- `Pyramide` (ou tout autre libellé ≠ Pickandplace) : scénario de construction/déconstruction d’une pyramide autour d’un centre.

---

## Démonstration :
- `assets/demo_simulation.gif` : simulation RoboDK
- `assets/demo_reel.gif` : robot réel
- `assets/ui.png` : capture UI Tkinter
