import copy
import random
import utils


class Generator:
    """Generuje unikatne nahodne body s cyklicky opakujucimi sa triedami"""

    def __init__(self, pocet):
        self.pocet = pocet

    def nahodne_body(self, priestor):
        """Vrati zoznam x unikatnych bodov"""
        res = copy.deepcopy(priestor)
        zoznam = []
        farba = 0
        for _ in range(self.pocet):
            suradnice = self.vygeneruj_suradnice(farba)  # suradnice pre bod
            while res.search_point(suradnice) is True:  # kontrola ci je unikatny
                suradnice = self.vygeneruj_suradnice(farba)
            res.insert(suradnice, farba)  # vlozenie do stromu
            zoznam.append(utils.Point(suradnice, farba))  # do finalneho zoznamu
            farba += 1
            if farba == 4:  # cyklenie cez farby
                farba = 0
        return zoznam

    def vygeneruj_suradnice(self, farba):
        """Vrati suradnice pre bod na zaklade pravdepodobnosti"""
        nahoda = random.randint(1, 100)
        if nahoda > 99:
            x = random.randint(-5000, 5000)
            y = random.randint(-5000, 5000)
        else:
            if farba == utils.RED:
                x = random.randint(-5000, 500)
                y = random.randint(-5000, 500)
            elif farba == utils.GREEN:
                x = random.randint(-500, 5000)
                y = random.randint(-5000, 500)
            elif farba == utils.BLUE:
                x = random.randint(-5000, 500)
                y = random.randint(-500, 5000)
            elif farba == utils.PURPLE:
                x = random.randint(-500, 5000)
                y = random.randint(-500, 5000)
        return [x, y]
