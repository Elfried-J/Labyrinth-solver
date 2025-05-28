#Jeffrey Kamdem et Iaris Toderasc
from pilefilelib import Pile, File
from graphelib import Graphe, Sommet
class Labyrinthe:
    def __init__(self,matrice,sommet_dep = str((0,0)),sommet_arv = None):
        self._matrice = matrice
        self._graphe = Graphe(False)
        self._sommet_dep = sommet_dep
        if sommet_arv == None:
            sommet_arv = str((len(matrice)-1, len(matrice[0])-1))
        self._sommet_arv = sommet_arv

        for rangee in range(len(matrice)):
            for colonne in range(len(matrice[0])):
                if matrice[rangee][colonne] == 0:
                    self._graphe.ajouteSommet(str((rangee,colonne)))
                    if rangee > 0 and  matrice[rangee-1][colonne] == 0:
                        self._graphe.ajouteArete(str((rangee,colonne)),str((rangee-1,colonne)))
                    if colonne > 0 and matrice[rangee][colonne-1] == 0:
                        self._graphe.ajouteArete(str((rangee, colonne)), str((rangee , colonne-1)))


    def parcours_profondeur_laby(self, G, depart, arrivee,sommetsVisites = []):
        if depart == arrivee:
            pile = Pile()
            pile.empile(depart)
            return pile
        sommetsVisites.append(depart)
        for x in G.sommet(depart).listeVoisins():
            if str(x) not in sommetsVisites:
                pile = self.parcours_profondeur_laby(G, str(x), arrivee, sommetsVisites)
                if not pile.estvide():
                    pile.empile(depart)
                    return pile
        return Pile()
    def solution_dfs(self):
        chemin = self.parcours_profondeur_laby(self._graphe, self._sommet_dep, self._sommet_arv)
        if chemin.estvide():
            print("Il n'y a auncun chemin dans le labyrinthe qui va du debut a la fin")
        else:
            chemin2 = []
            while not chemin.estvide():
                chemin2.append(chemin.depile())
            print("Félicitation ! vous avez réussi à trouver l'arrivée qui est la case :" + self._sommet_arv+ " par le chemin: " + str(chemin2))

    def parcours_largeur_laby(self, G, depart, arrivee):
        pallier = 0
        parcours = [depart]
        precedent = [-1]
        sommetsVisites = [depart]
        pile = Pile()
        if depart == arrivee:
            pile.empile(depart)
            return pile
        while pallier < len(parcours):
            finPallier = len(parcours)
            for x in range(pallier, finPallier):
                for y in self._graphe.sommet(parcours[x]).listeVoisins():
                    sommetVoisin = str(y)
                    if sommetVoisin == arrivee:
                        pile.empile(arrivee)
                        positionParent = x
                        while positionParent >= 0:
                            pile.empile(parcours[positionParent])
                            positionParent = precedent[positionParent]
                        return pile
                    if sommetVoisin not in sommetsVisites:
                        parcours.append(sommetVoisin)
                        precedent.append(x)
                        sommetsVisites.append(sommetVoisin)
            pallier = finPallier
        return pile

    def solution_bfs(self):
        chemin = self.parcours_largeur_laby(self._graphe, self._sommet_dep, self._sommet_arv)
        chemin2 = []
        while not chemin.estvide():
            chemin2.append(chemin.depile())
        print("Félicitation ! vous arrivez à l'arrivée qui est la case: " + self._sommet_arv + " par le chemin: "+ str(chemin2) + ".C'est le chemin le plus court pour parcourir ce labyrinthe et la distance totale est de :" + str(len(chemin2)) + " arretes.")








laby = [
 [0, 0, 1, 1, 0, 1, 1, 1, 1],
 [0, 0, 0, 1, 0, 1, 1, 1, 1],
 [1, 0, 0, 1, 1, 1, 0, 0, 1],
 [0, 0, 0, 0, 0, 0, 0, 1, 0],
 [1, 0, 1, 0, 0, 0, 0, 0, 1],
 [0, 0, 1, 0, 0, 0, 0, 0, 1],
 [1, 0, 1, 0, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, 0, 1, 0, 0, 1],
 [0, 0, 1, 1, 0, 1, 0, 0, 1],
 [1, 1, 0, 1, 0, 0, 0, 1, 1],
 [1, 1, 1, 0, 1, 1, 0, 0, 0]]
# Définir un objet Labyrinthe
lb = Labyrinthe(laby, '(0, 0)', '(10, 8)')

lb.solution_dfs()
lb.solution_bfs()

