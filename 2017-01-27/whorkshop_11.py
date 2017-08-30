from pyplasm import *
from larlib import *
from workshop_10 import *
import csv


def stringToFloat(str):
    l = str.split(',')
    newList = []
    for c in l:
        elem = float(c) / 10.
        newList.append(elem)
    return newList


def creaParcheggio():
    parcheggio = CUBOID([12, 15, 0.0001])
    parcheggio = TEXTURE("texture_parcheggio.jpg")(parcheggio)
    return parcheggio


def creaPanchina():
    supporto = CUBOID([.15, .26, .25])
    panca = CUBOID([2, .3, .08])
    schienale = CUBOID([2, .06, .45])
    supporto2 = CUBOID([.15, .03, .55])
    panchina = STRUCT(
        [T([1, 2])([.3, 0.02])(supporto), T(3)(.25)(panca), T([1, 2])([1.55, 0.02])(supporto), T(3)(0.4)(schienale),
         T([1, 2, 3])([0.3, -0.1, .33])(supporto2), T([1, 2, 3])([1.55, -0.1, .33])(supporto2)])
    panchina = TEXTURE(["textureBase.jpg", True, False, 1, 1, 0, 4, 4])(panchina)
    return panchina


def creaPiazza():
    pavimento = CIRCLE(6)([56, 56])
    pavimento = TEXTURE("texturePiazza.jpg")(pavimento)
    return pavimento


def creaCampoTennis():
    base = CUBOID([10, 13, 0.5])
    pavimento = CUBOID([10, 13])
    campo = CUBOID([9, 12, 0.5])
    campo = T([1, 2])([0.5, 0.5])(campo)
    base = DIFFERENCE([base, campo])
    campo = CUBOID([9, 12, 0.3])
    campo = T([1, 2, 3])([0.5, 0.5, 0.05])(campo)
    campo = TEXTURE("textureTennis.jpg")(campo)
    rete = CUBOID([7.2, 0.07, 0.8])
    rete = T([1, 2, 3])([1.4, 6.463, 0.0])(rete)
    rete = TEXTURE("textureRete.jpg")(rete)
    recinto = CUBOID([14, 17, 2])
    dif = CUBOID([13, 16, 2])
    dif = T([1, 2])([0.5, 0.5])(dif)
    porta = CUBOID([2, 2, 2])
    porta = T(1)(6)(porta)
    recinto = DIFFERENCE([recinto, dif])
    recinto = DIFFERENCE([recinto, porta])
    pavimentoRecinto = CUBOID([14, 17, 0.06])
    pavimentoRecinto = TEXTURE("texture_mattonelle.jpg")(pavimentoRecinto)
    campoTennis = STRUCT([base, campo, rete, pavimento])
    campoTennis = T([1, 2])([2, 2])(campoTennis)
    struttura = STRUCT([recinto, campoTennis, pavimentoRecinto])
    return struttura


def creaCampoCalcetto():
    campo = CUBOID([15, 19.5, 0.5])
    campo = T([1, 2])([0.5, 0.5])(campo)
    campo = TEXTURE("textureCalcetto.jpg")(campo)
    recinto = CUBOID([18, 22.5, 3.5])
    dif = CUBOID([17, 21.5, 3.5])
    dif = T([1, 2])([0.5, 0.5])(dif)
    entrata = CUBOID([2, 2, 2])
    entrata = T(2)(2)(entrata)
    recinto = DIFFERENCE([recinto, dif])
    recinto = DIFFERENCE([recinto, entrata])
    porta = CUBOID([4, .3, 2])
    buco = CUBOID([3.4, .3, 1.7])
    buco = T(1)([0.3])(buco)
    porta = DIFFERENCE([porta, buco])
    porta2 = CUBOID([4, .3, 2])
    buco2 = CUBOID([3.4, .3, 1.7])
    buco2 = T(1)([0.3])(buco2)
    campo = T([1, 2])([1, 1])(campo)
    porta2 = DIFFERENCE([porta2, buco2])
    campoCalcetto = STRUCT([recinto, campo, T([1, 2])([6.5, 1.5])(porta), T([1, 2])([6.5, 20.5])(porta)])
    return campoCalcetto


def creaAlbero():
    tronco = CYLINDER([0.2, 2])(36)
    fogliame = SPHERE(0.7)([36, 36])
    fogliame = STRUCT([T([1, 3])([-0.2, 2])(fogliame), T([1, 3])([0.2, 2])(fogliame), T([3])([2.2])(fogliame)])
    tree = STRUCT([TEXTURE("texture_tronco.jpg")(tronco), TEXTURE("texture_fogliame.jpg")(fogliame)])
    return tree


def posizioneAlberi():
    tr = lambda x, y: T([1, 2])([x, y])(S([1, 2, 3])([1.5, 1.5, 2])(creaAlbero()))
    xs = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56,
          58, 60, 62, 64, 66, 68, 70]
    ys = [109, 105, 109, 105, 109, 105, 109, 105, 109, 105, 109, 105, 109, 105, 109, 105, 109, 105, 109, 105, 109, 105,
          109, 105, 109, 105, 109, 105, 109, 105, 109, 105, 109, 105, 109]

    xs += [2, 4, 6, 8, 10, 12, 14, 18, 50, 54, 56, 58, 60, 62, 64, 66, 68, 70]
    ys += [101, 97, 101, 97, 101, 97, 101, 101, 101, 101, 97, 101, 97, 101, 97, 101, 97, 101]

    xs += [2, 4, 6, 8, 10, 62, 64, 66, 68, 70]
    ys += [93, 89, 93, 89, 93, 93, 89, 93, 89, 93]

    xs += [2, 4, 6, 66]
    ys += [85, 81, 85, 85]

    xs += [2, 4, 6]
    ys += [77, 73, 77]

    xs += [2, 4, 6]
    ys += [69, 65, 69]

    xs += [2, 4, 6, 8]
    ys += [61, 57, 61, 57]

    xs += [2, 4, 6, 8, 10, 12, 14, 16]
    ys += [53, 49, 53, 49, 53, 49, 53, 49]

    return STRUCT(map(tr, xs, ys))


def provaCurva(file_name):
    curva = STRUCT([QUOTE([0])])
    lista = []
    with open(file_name, 'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=' ', quotechar='|')
        for row in reader:
            l = stringToFloat(row[0])
            c = MAP(BEZIER(S1)([[l[0], l[1]], [l[2], l[3]]]))(INTERVALS(1)(5))
            curva = STRUCT([curva, c])
    curva = OFFSET([2, 2])(curva)
    return curva


def main():
    prato = CUBOID([71, 110, 0.3])
    curva = provaCurva("curve.lines")
    base = CUBOID([71, 110, 0.5])
    base = T(3)(-0.5)(base)
    base = TEXTURE(["texturePrato.jpg", True, False, 1, 1, 0, 4, 4])(base)

    collegamentoParcheggio = CUBOID([12, 4, 0.1])
    collegamentoParcheggio = T([1, 2])([15, 24])(collegamentoParcheggio)
    collegamentoParcheggio = T(3)(0.2)(collegamentoParcheggio)
    collegamentoParcheggio = TEXTURE("textureStrada.jpg")(collegamentoParcheggio)

    prato = TEXTURE(["texturePrato.jpg", True, False, 1, 1, 0, 30, 30])(prato)
    curva = PROD([curva, Q(0.1)])
    curva = T(3)(0.2)(curva)
    curva = TEXTURE(["textureStrada.jpg", True, False, 1, 1, 0, 6, 6])(curva)
    curva = MATERIAL([58.8, 58.8, 58.8, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1])(curva)
    prato = MATERIAL([0, 102, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1])(prato)

    piazza = creaPiazza()
    piazza = T(3)(0.3)(piazza)
    piazza = T([1, 2])([31, 42])(piazza)

    panchina = creaPanchina()
    panchina1 = creaPanchina()
    panchina = R([1, 2])(PI * 1)(panchina)
    panchina1 = R([1, 2])(PI * 1)(panchina1)
    panchine1 = STRUCT([panchina, T(1)(2.5)(panchina1)])
    panchine1 = T([1, 2, 3])([31, 46.5, 0.3])(panchine1)

    panchina2 = creaPanchina()
    panchina5 = creaPanchina()
    panchine2 = STRUCT([panchina2, T(1)(2.5)(panchina5)])
    panchine2 = T([1, 2, 3])([28.75, 38, 0.3])(panchine2)

    panchina3 = creaPanchina()
    panchina4 = creaPanchina()
    panchina3 = R([1, 2])(PI * 1 / 2)(panchina3)
    panchina4 = R([1, 2])(PI * 1 / 2)(panchina4)
    panchine3 = STRUCT([panchina3, T(2)(2.5)(panchina4)])
    panchine3 = T([1, 2, 3])([35.5, 39.75, 0.3])(panchine3)

    panchina6 = creaPanchina()
    panchina7 = creaPanchina()
    panchina6 = R([1, 2])(PI * 3 / 2)(panchina6)
    panchina7 = R([1, 2])(PI * 3 / 2)(panchina7)
    panchine4 = STRUCT([panchina6, T(2)(2.5)(panchina7)])
    panchine4 = T([1, 2, 3])([26.5, 41.9, 0.3])(panchine4)

    parcheggio = creaParcheggio()
    parcheggio = T(3)(0.3)(parcheggio)
    parcheggio = R([1, 2])(PI / 2)(parcheggio)
    parcheggio = T([1, 2])([15, 19])(parcheggio)

    campoTennis = creaCampoTennis()
    campoTennis = T(3)(0.3)(campoTennis)
    campoTennis = R([1, 2])(PI * 3 / 2)(campoTennis)
    campoTennis = T([1, 2])([11, 80])(campoTennis)

    campoCalcetto = creaCampoCalcetto()
    campoCalcetto = T(3)(0.3)(campoCalcetto)
    campoCalcetto = R([1, 2])(PI * 3 / 2)(campoCalcetto)
    campoCalcetto = T([1, 2])([33.3, 92])(campoCalcetto)

    alberi = posizioneAlberi()

    casa = casaUnPiano()
    casa = S([1, 2, 3])([0.3, 0.3, 0.3])(casa)
    casa = T(3)(0.3)(casa)
    casa = R([1, 2])(PI / 2)(casa)
    casa = T([1, 2])([15, 5.5])(casa)

    casa1 = casaDuePiani()
    casa1 = S([1, 2, 3])([0.3, 0.3, 0.3])(casa1)
    casa1 = T(3)(0.3)(casa1)
    casa1 = R([1, 2])(PI / 2)(casa1)
    casa1 = T([1, 2])([30, 5.5])(casa1)

    casa2 = casaDuePiani()
    casa2 = S([1, 2, 3])([0.3, 0.3, 0.3])(casa2)
    casa2 = T(3)(0.3)(casa2)
    casa2 = T([1, 2])([33, 3])(casa2)

    casa7 = casaUnPiano()
    casa7 = S([1, 2, 3])([0.3, 0.3, 0.3])(casa7)
    casa7 = T(3)(0.3)(casa7)
    casa7 = R([1, 2])(PI / 1.4)(casa7)
    casa7 = T([1, 2])([65, 15])(casa7)

    casa3 = casaUnPiano()
    casa3 = S([1, 2, 3])([0.3, 0.3, 0.3])(casa3)
    casa3 = T(3)(0.3)(casa3)
    casa3 = R([1, 2])(PI * 3 / 2)(casa3)
    casa3 = T([1, 2])([42, 37])(casa3)

    casa4 = casaUnPiano()
    casa4 = S([1, 2, 3])([0.3, 0.3, 0.3])(casa4)
    casa4 = T(3)(0.3)(casa4)
    casa4 = R([1, 2])(PI * 2.9 / 2)(casa4)
    casa4 = T([1, 2])([45, 61])(casa4)

    casa5 = casaDuePiani()
    casa5 = S([1, 2, 3])([0.3, 0.3, 0.3])(casa5)
    casa5 = T(3)(0.3)(casa5)
    casa5 = R([1, 2])(PI * 6.7 / 4)(casa5)
    casa5 = T([1, 2])([26, 28])(casa5)

    casa6 = casaUnPiano()
    casa6 = S([1, 2, 3])([0.3, 0.3, 0.3])(casa6)
    casa6 = T(3)(0.3)(casa6)
    casa6 = R([1, 2])(PI / 2.3)(casa6)
    casa6 = T([1, 2])([66, 59])(casa6)

    casa8 = casaDuePiani()
    casa8 = S([1, 2, 3])([0.3, 0.3, 0.3])(casa8)
    casa8 = T(3)(0.3)(casa8)
    casa8 = R([1, 2])(PI * 3 / 2)(casa8)
    casa8 = T([1, 2])([30, 60])(casa8)

    casa9 = casaDuePiani()
    casa9 = S([1, 2, 3])([0.3, 0.3, 0.3])(casa9)
    casa9 = T(3)(0.3)(casa9)
    casa9 = R([1, 2])(PI / 2)(casa9)
    casa9 = T([1, 2])([46.7, 62])(casa9)

    casa10 = casaUnPiano()
    casa10 = S([1, 2, 3])([0.3, 0.3, 0.3])(casa10)
    casa10 = T(3)(0.3)(casa10)
    casa10 = R([1, 2])(PI * 1)(casa10)
    casa10 = T([1, 2])([65.7, 51.5])(casa10)

    casa11 = casaUnPiano()
    casa11 = S([1, 2, 3])([0.3, 0.3, 0.3])(casa11)
    casa11 = T(3)(0.3)(casa11)
    casa11 = R([1, 2])(PI / 2)(casa11)
    casa11 = T([1, 2])([15, 37])(casa11)

    quartiere = STRUCT(
        [curva, collegamentoParcheggio, prato, base, parcheggio, panchine1, panchine2, panchine3, panchine4, piazza,
         campoCalcetto, campoTennis, casa, casa1, casa2, casa3, casa4, casa5, casa6, casa7, casa8, casa9, casa10,
         casa11, alberi])

    VIEW(quartiere)


main()

