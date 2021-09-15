from knn import KNN
from utils import Point


class KdStrom:
    """Reprezentacia K dimenzionalneho stromu"""

    def __init__(self):
        self.strom = None  # samotna reprezentacia stromu
        self.size = 0
        self.tmp_farba = None  # docasna farba pri vkladani.

    def insert_bod(self, root, new_point, hlbka):
        """Vlozenie bodu do stromu"""
        if root is None:  # dostali sme sa tam kam sa ma vlozit, vynaranie
            return Point(new_point, self.tmp_farba)
        dim = hlbka % 2  # splitovacia dimenzia
        if new_point[dim] < root[dim]:
            root.left = self.insert_bod(root.left, new_point, hlbka + 1)
        else:
            root.right = self.insert_bod(root.right, new_point, hlbka + 1)
        return root

    def insert(self, new_point, new_point_farba):
        """Wrapper pre vkladanie novych bodov"""
        self.size += 1
        self.tmp_farba = new_point_farba
        self.strom = self.insert_bod(self.strom, new_point, 0)

    def su_body_rovnake(self, bod1, bod2):
        return bod1[0] == bod2[0] and bod1[1] == bod2[1]

    def search(self, root, new_point, hlbka):
        """Hladanie bodu v strome, return True ak sa bod v strome nachadza"""
        if root is None:
            return False
        if self.su_body_rovnake(root, new_point):
            return True
        dim = hlbka % 2
        if new_point[dim] < root[dim]:
            return self.search(root.left, new_point, hlbka + 1)

        return self.search(root.right, new_point, hlbka + 1)

    def search_point(self, new_point):
        return self.search(self.strom, new_point, 0)

    def najdi_susedov(self, point, k):
        """Inicializacia KNN algoritmu, vrati k najblizsich susedov"""
        knn_algorithm = KNN(k)
        knn_algorithm.search(self.strom, point, 0)
        return knn_algorithm.susedia

    def vytvor_pociatocny_priestor(self, priestor):
        """Vlozi do stromu pociatocnych 20 bodov."""
        for bod in priestor:
            self.insert(bod, bod.farba)
