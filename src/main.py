import concurrent.futures
import timeit
from utils import print_vysledok, load_input
from generator import Generator
from kd_strom import KdStrom
from klasifikator import Klasifikator


def spusti_klasifikator(k, priestor, nahodne_body, vzorka):
    result = Klasifikator(k, priestor, nahodne_body).run()
    print_vysledok(result, vzorka)


if __name__ == "__main__":
    vzorka = 40000  # pocet nahodnych bodov
    priestor_vector = load_input("vstup.txt")  # nacitanie pociatocnych bodov
    kd = KdStrom()  # strom pre unikatnost
    kd.vytvor_pociatocny_priestor(priestor_vector)  # naplnenie stromu
    nahodne_body = Generator(vzorka).nahodne_body(kd)  # zoznam nahodnych bodov zo stromu
    ks = [1, 3, 7, 15]
    print(f"Spustam klasifikatory:{ks}")
    start = timeit.default_timer()

    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        for k in ks:
            executor.submit(spusti_klasifikator, k, priestor_vector, nahodne_body, vzorka)

    print(f"Runtime: {timeit.default_timer() - start}")
