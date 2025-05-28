class Pile:
    def __init__(self):
        self._contenu = []

    def empile(self, valeur):
        self._contenu.append(valeur)

    def depile(self):
        if self.estvide():
            raise IndexError("Pile vide")
        return self._contenu.pop()

    def estvide(self):
        return len(self._contenu) == 0
class File:
    def __init__(self):
        self._contenu = []

    def enfiler(self, valeur):
        self._contenu.append(valeur)

    def defiler(self):
        if self.estvide():
            raise IndexError("File vide")
        return self._contenu.pop(0)

    def estvide(self):
        return len(self._contenu) == 0
