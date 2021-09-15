import timeit
from kd_strom import KdStrom
from utils import vypocitaj_modus


class Klasifikator:
    """Reprezentuje klasifikator, ktory pomocou funkcie classify vyhodnoti body v pristore"""

    def __init__(self, k, priestor, nahodne_body):
        self.priestor = priestor  # povodne body
        self.k = k  # pocet najblizsich susedov pre klasifikovanie
        self.nahodne_body = nahodne_body  # vygenerovane body
        self.kd = None  # KD strom

    def classify(self, x, y, k):
        """Klasifikuje jeden bod a vrati farbu"""
        point = [x, y]
        najblizsi_susedia = self.kd.najdi_susedov(point, k)
        klasifikovana_farba = vypocitaj_modus(najblizsi_susedia)  # najcastejsia hodnota
        return klasifikovana_farba

    def run(self):
        """Vrati KD strom naplneny klasifikovanymi bodmi"""
        self.kd = KdStrom()
        self.kd.vytvor_pociatocny_priestor(self.priestor)  # povodnych 20b - KD Strom

        start = timeit.default_timer()
        uspech = 0
        for bod in self.nahodne_body:
            klasifikovana_farba = self.classify(bod[0], bod[1], self.k)
            self.kd.insert(bod, klasifikovana_farba)

            if bod.farba == klasifikovana_farba:
                uspech += 1
        cas_trvania = timeit.default_timer() - start

        return {"CAS_TRVANIA": cas_trvania, "USPECH": uspech, "STROM": self.kd.strom, "K": self.k}
