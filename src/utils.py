import math
from collections import deque
from plot import plot_2d

RED = 0
GREEN = 1
BLUE = 2
PURPLE = 3


class Point(list):
    """Reprezentuje jeden vrchol v KD strome"""

    def __init__(self, bod, farba):
        self.left = None
        self.right = None
        self.farba = farba
        list.__init__(self, [bod[0], bod[1]])


class Vzdialenost:
    """Reprezentuje vzdialenost bodu v zozname najblizsich susedov"""

    def __init__(self, bod, distance):
        self.bod = bod
        self.distance = distance

    def __lt__(self, other):
        """custom comparator pre porovnanie objektu"""
        return self.distance < other.distance


def load_input(vstup):
    """nactanie predefinovanych bodov zo suboru (definovane na mieru)"""
    res = []
    farba = 0
    with open(vstup, "r") as file:
        for line in file:
            # skonvertuje riadok zo suboru na zoznam cisel oddelenych ciarkov.x->0, y->1
            line = list(map(int, line.strip().split(",")))
            for i in range(0, len(line), 2):
                res.append(Point([line[i], line[i + 1]], farba))
            farba += 1
    return res


def euclidian_d(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def return_b_list(tree, templist, queue):
    """In order prechod stromom a priebezne ukladanie do zoznamu"""
    if tree is None:
        return
    queue.append(tree)
    while len(queue) != 0:
        node = queue.popleft()
        if node is not None:
            templist.append(node)
            queue.append(node.left)
            queue.append(node.right)


def strom_na_list(strom):
    templist = []
    queue = deque()
    return_b_list(strom, templist, queue)
    return templist


def vypocitaj_modus(susedia):
    """najcastejsie vyskytujuca sa trieda zo styroch"""
    pocty = [0, 0, 0, 0]
    for sused in susedia:
        pocty[sused.bod.farba] += 1
    return pocty.index(max(pocty))


def print_uspesnost(k, uspech, vzorka, cas_trvania):
    print(f"k = {k}")
    print(f"Uspech:{uspech}/{vzorka}")
    print(f"Cas trvania:{cas_trvania}")
    uspesnost = uspech / vzorka * 100
    print(f"Uspesnost: {uspesnost}%")


def print_vysledok(result, vzorka):
    """vypis na stdout a vykreslenie do ./vysledky/k.png"""
    print_uspesnost(result["K"], result["USPECH"], vzorka, result["CAS_TRVANIA"])
    plot_2d(result["STROM"], result["K"], result["USPECH"], vzorka, result["CAS_TRVANIA"])
