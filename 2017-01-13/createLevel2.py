from pyplasm import *
from larlib import *
import math
import csv
import fpformat


def stringToFloat(str):
    l = str.split(',')
    newList = []
    for c in l:
        elem = float(c) / 20.
        newList.append(elem)
    return newList


def structure(file_name):
    interior = 0
    with open(file_name, 'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=' ', quotechar='|')
        for r in reader:
            l = stringToFloat(r[0])
            row = MKPOL([[[l[0], l[1], 0], [l[2], l[3], 0]], [[1, 2]], 1])
            if interior != 0:
                interior = STRUCT([interior, row])
            else:
                interior = row

        interior = OFFSET([0.1, 0.1, 3])(interior)
    return interior


def windowHole(file_name):
    windows = 0
    with open(file_name, 'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=' ', quotechar='|')
        for r in reader:
            l = stringToFloat(r[0])
            row = MKPOL([[[l[0], l[1], 0], [l[2], l[3], 0]], [[1, 2]], 1])
            if windows != 0:
                windows = STRUCT([windows, row])
            else:
                windows = row

    windows = T(3)(1.3)(windows)
    return windows


def createWindows(file_name):
    windows = 0
    with open(file_name, 'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=' ', quotechar='|')
        for r in reader:
            l = stringToFloat(r[0])
            row = MKPOL([[[l[0], l[1], 0], [l[2], l[3], 0]], [[1, 2]], 1])
            row = OFFSET([0.18, 0.18, 1])(row)
            row = T(3)(1.3)(row)
            row = TEXTURE("vetro.jpg")(row)
            if windows != 0:
                windows = STRUCT([windows, row])
            else:
                windows = row

    return windows


def widthCell(lista):
    newLista = []
    for i in range(len(lista)):
        newLista.append(i + 1)
    return newLista


def interiorDoors(file_name):
    doors = 0
    with open(file_name, 'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=' ', quotechar='|')
        for r in reader:
            l = stringToFloat(r[0])
            row = MKPOL([[[l[0], l[1], 0], [l[2], l[3], 0]], [[1, 2]], 1])
            if doors != 0:
                doors = STRUCT([doors, row])
            else:
                doors = row
        doors = OFFSET([0.15, 0.15, 0])(doors)
        doors = OFFSET([-0.10, 0, 2])(doors)
    return doors


def deleteDouble(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    return l


def holeStair(file_name):
    stair = STRUCT([QUOTE([0])])
    with open(file_name, 'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=' ', quotechar='|')
        for r in reader:
            l = stringToFloat(r[0])
            row = MKPOL([[[l[0], l[1], 0], [l[2], l[3], 0]], [[1, 2]], 1])
            stair = STRUCT([stair, row])
    listaPunti = UKPOL(stair)
    V = listaPunti[0]
    V.remove(V[0])
    EV = listaPunti[1]
    FV = []
    listaVer = []
    hole = STRUCT([QUOTE([0])])
    for i in range(0, len(V)):
        elem = V[i]
        listaVer.append([elem[0], elem[1]])
    for i in range(0, len(listaVer) - 1):
        if listaVer[i + 1] != None:
            hole = STRUCT([hole, POLYLINE([listaVer[i], listaVer[i + 1]])])
        else:
            hole = STRUCT([hole, POLYLINE([listaVer[i], listaVer[0]])])
        i + 2
    hole = SOLIDIFY(hole)
    return hole


def createStair(file_name):
    wallStair = 0
    with open(file_name, 'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=' ', quotechar='|')
        for r in reader:
            l = stringToFloat(r[0])
            row = MKPOL([[[l[0], l[1], 0], [l[2], l[3], 0]], [[1, 2]], 1])
            if wallStair != 0:
                wallStair = STRUCT([wallStair, row])
            else:
                wallStair = row
    wallStair = OFFSET([0.1, 0.1, 1])(wallStair)
    return wallStair


def createFloor(file_name):
    floor = STRUCT([QUOTE([0])])
    with open(file_name, 'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=' ', quotechar='|')
        for r in reader:
            l = stringToFloat(r[0])
            row = MKPOL([[[l[0], l[1], 0], [l[2], l[3], 0]], [[1, 2]], 1])
            floor = STRUCT([floor, row])
    listaPunti = UKPOL(floor)
    V = listaPunti[0]
    V.remove(V[0])
    EV = listaPunti[1]
    FV = []
    listaVer = []
    pav = STRUCT([QUOTE([0])])
    for i in range(0, len(V)):
        elem = V[i]
        listaVer.append([elem[0], elem[1]])
    for i in range(0, len(listaVer) - 1):
        if listaVer[i + 1] is not None:
            pav = STRUCT([pav, POLYLINE([listaVer[i], listaVer[i + 1]])])
        else:
            pav = STRUCT([pav, POLYLINE([listaVer[i], listaVer[0]])])
        i + 2
    pav = SOLIDIFY(pav)
    return pav


def createWalls(file_name):
    planimetry = 0
    with open(file_name, 'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=' ', quotechar='|')
        for r in reader:
            l = stringToFloat(r[0])
            row = MKPOL([[[l[0], l[1], 0], [l[2], l[3], 0]], [[1, 2]], 1])
            if planimetry != 0:
                planimetry = STRUCT([planimetry, row])
            else:
                planimetry = row

    return planimetry


def cleanList(lista):
    newL = []
    for i in lista:
        elem = []
        for j in i:
            a = int(j)
            elem.append(a)
        newL.append(elem)
    noDop = deleteDouble(newL)
    return noDop


def creaPlanimetry2(file_name):
    walls = createWalls("wallsExt.lines")

    interior = structure("interior2.lines")
    doors = interiorDoors("doors2.lines")

    floor = createFloor("wallsExt.lines")

    interior = DIFFERENCE([interior, doors])

    stair = holeStair("stair.lines")
    floor = DIFFERENCE([floor, stair])
    wallStair = createStair("wallStair.lines")
    buchiFin = windowHole("windows2.lines")

    buchiFin = OFFSET([0.03, 0.03, 0])(buchiFin)
    buchiFin = OFFSET([-0.03, -0.03, 1])(buchiFin)
    walls = OFFSET([0.01, 0.01, 3])(walls)

    walls = DIFFERENCE([walls, buchiFin])
    walls = OFFSET([0.2, 0.2, 0.01])(walls)

    windows = createWindows("windows2.lines")

    interior = COLOR(Color4f([255 / 255., 228 / 255., 225 / 255., 1]))(interior)
    walls = TEXTURE(["textureMuro.jpg", True, False, 1, 1, 0, 100, 100])(walls)
    floor = TEXTURE(["texturePavimento.jpg", TRUE, FALSE, 1, 0, 0, 1, 2])(floor)
    doors = TEXTURE(["texturePorteInt.jpg", TRUE, FALSE, 1, 0, 0, 1, 2])(doors)
    planimetry2 = STRUCT([walls, interior, floor, wallStair, finestre, doors])
    planimetry2 = T(3)(3)(planimetry2)
    return planimetry2