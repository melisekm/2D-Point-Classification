import gc
import matplotlib.pyplot as plt
import utils
import os

def plot_2d(strom, k, uspech, vzorka, cas_trvania):
    print("Plotujem..")
    zoznam = utils.strom_na_list(strom)
    plt.figure(figsize=(7, 6))

    for bod in zoznam:
        if bod.farba == utils.RED:
            plt.plot(bod[0], bod[1], "ro")
        elif bod.farba == utils.GREEN:
            plt.plot(bod[0], bod[1], "go")
        elif bod.farba == utils.BLUE:
            plt.plot(bod[0], bod[1], "bo")
        elif bod.farba == utils.PURPLE:
            plt.plot(bod[0], bod[1], "mo")

    # pre vacsie bodky dopln argument: markersize=22
    # zaplni celu plochu aj pri 4k bodov

    uspesnost = uspech / vzorka * 100
    plt.title(f"Uspesnost: {uspech}/{vzorka} - {uspesnost:.3f}%\n{cas_trvania:.3f} sec\nk={k}")
    plt.axis([-5000, 5000, -5000, 5000])
    print(f"Ukladam ilustraciu k={k}")
    try:
        os.mkdir("vysledky")
    except:
        pass
    plt.savefig("vysledky/" + str(k) + ".png")
    print(f"k={k} HOTOVO")

    plt.cla()  # vymaz osy
    plt.clf()  # vymaz figure
    plt.close("all")  # vymaz figure
    gc.collect()  # zavolaj garbage collector na vsetko co nema referenciu IMPORTANT
