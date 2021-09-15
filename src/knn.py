import math
from utils import euclidian_d, Vzdialenost


class KNN:
    """Reprezentuje hladanie k najblizsich susedov v strome pre bod"""

    def __init__(self, k):
        self.susedia = []
        self.k = k

    def check_distance(self, leaf, point):
        """
        Porovna vzdialenost dvoch bodov,
        ak je vzdialenost lepsia ako k ty najblizsi sused, vlozi ho do zoznamu
        """
        distance = euclidian_d(leaf, point)
        if len(self.susedia) < self.k:  # ak sa v zozname este nenachadza k prvkov
            self.susedia.append(Vzdialenost(leaf, distance))
            self.susedia.sort()
        elif distance < self.susedia[-1].distance:  # ak je lepsia distnace nez kty najblizsia
            self.susedia.append(Vzdialenost(leaf, distance))
            self.susedia.sort()
            self.susedia.pop()

    def search(self, root, point, hlbka):
        if root is None:
            return
        self.check_distance(root, point)  # skontroluje ci netreba pridat bod do zoznamu
        dim = hlbka % 2
        if len(self.susedia) < self.k or point[dim] < root[dim]:
            self.search(root.left, point, hlbka + 1)
            if len(self.susedia) < self.k or math.fabs(root[dim] - point[dim]) <= self.susedia[-1].distance:
                self.search(root.right, point, hlbka + 1)  # v opacnej vetve moze byt blizsi bod
        else:
            self.search(root.right, point, hlbka + 1)
            if len(self.susedia) < self.k or math.fabs(root[dim] - point[dim]) <= self.susedia[-1].distance:
                self.search(root.left, point, hlbka + 1)

    # tie LEN(susedia) tam musia byt inak by sa mohlo stat ze sa vynorime z rekurzie skor nez mame k susedov
