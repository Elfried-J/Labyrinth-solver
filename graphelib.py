class Graphe:
    def __init__(self, oriente=False):
        self._sommets = {}
        self._oriente = oriente

    def ajouteSommet(self, nom):
        if nom not in self._sommets:
            self._sommets[nom] = Sommet(nom)

    def ajouteArete(self, s1, s2):
        self._sommets[s1].ajouteVoisin(s2)
        if not self._oriente:
            self._sommets[s2].ajouteVoisin(s1)

    def sommet(self, nom):
        return self._sommets[nom]

    def listeSommets(self):
        return list(self._sommets.keys())
class Sommet:
    def __init__(self, nom):
        self._nom = nom
        self._voisins = []

    def ajouteVoisin(self, voisin):
        if voisin not in self._voisins:
            self._voisins.append(voisin)

    def listeVoisins(self):
        return self._voisins
