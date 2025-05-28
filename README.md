# Labyrinth-solver
Ce programme Python, réalisé par Jeffrey Kamdem et Iaris Toderasc, est un résolveur de labyrinthe qui permet de trouver un chemin entre un point de départ et un point d’arrivée à l’aide de techniques de parcours de graphe. Le labyrinthe est représenté sous forme de matrice 2D d'entiers, où chaque cellule contient soit un 0 (indiquant un espace libre), soit un 1 (indiquant un mur). L'objectif principal du programme est de déterminer s’il existe un chemin entre le départ et l’arrivée, et de démontrer la différence entre deux algorithmes de recherche fondamentaux : la recherche en profondeur (DFS) et la recherche en largeur (BFS). L’algorithme DFS permet de trouver un chemin possible, tandis que BFS garantit le plus court chemin.

Le programme s’articule autour d’une classe principale nommée Labyrinthe, qui transforme la matrice en un graphe, puis utilise DFS et BFS pour résoudre le labyrinthe. Lors de l’instanciation, la classe scanne la matrice et construit un graphe non orienté en connectant chaque cellule libre (0) à ses voisins accessibles. Elle utilise pour cela la classe Graphe pour gérer la structure globale du graphe, et la classe Sommet pour représenter chaque cellule (ou nœud) du labyrinthe. Deux fonctions principales permettent de résoudre le labyrinthe : solution_dfs() et solution_bfs().

La méthode solution_dfs() fait appel à la fonction parcours_profondeur_laby, une implémentation récursive de l’algorithme de parcours en profondeur. Elle explore le labyrinthe aussi loin que possible avant de revenir en arrière, en utilisant une pile (Pile) pour reconstruire le chemin si l’arrivée est atteinte. Si aucun chemin n’existe, un message d’erreur est affiché.

La méthode solution_bfs() repose sur la fonction parcours_largeur_laby, qui effectue un parcours en largeur à l’aide d’une structure de niveaux. Elle conserve l’information sur les parents de chaque sommet visité pour reconstruire le plus court chemin une fois la destination atteinte. Le chemin final est affiché avec le nombre total d’arêtes parcourues.

Le programme repose sur deux bibliothèques utilitaires personnalisées :

pilefilelib.py : Ce fichier contient deux classes :

Pile, qui implémente une pile (LIFO) avec les méthodes de base empile (ajout), depile (retrait) et estvide (vérifie si la pile est vide).

File, qui implémente une file (FIFO) avec les méthodes enfiler, defiler et estvide. Dans ce projet, seule la pile est utilisée.

graphelib.py : Cette bibliothèque contient :

Graphe, une classe qui modélise un graphe non orienté à l’aide d’un dictionnaire de sommets (Sommet). Elle propose des méthodes comme ajouteSommet pour ajouter un sommet, ajouteArete pour relier deux sommets, et sommet pour accéder à un sommet donné.

Sommet, une classe représentant chaque cellule libre du labyrinthe. Elle stocke son nom et une liste de voisins, et fournit des méthodes pour ajouter ou consulter ses connexions.

En conclusion, ce projet illustre de manière concrète comment des structures abstraites comme les graphes, les piles et les files peuvent être utilisées pour résoudre un problème réel tel que la navigation dans un labyrinthe. En intégrant à la fois une approche par recherche en profondeur et une par recherche en largeur, le programme met en lumière la différence entre trouver un chemin possible et trouver le plus court chemin. Il s’agit d’un excellent exemple d’application des algorithmes et de la programmation orientée objet en Python.
