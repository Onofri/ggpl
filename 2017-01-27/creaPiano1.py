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

        interior = OFFSET([0.1, 0.1, 4.5])(interior)  # 3
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


def externalDoor(file_name):
    door = 0
    with open(file_name, 'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=' ', quotechar='|')
        for r in reader:
            l = stringToFloat(r[0])
            row = MKPOL([[[l[0], l[1], 0], [l[2], l[3], 0]], [[1, 2]], 1])
            if door != 0:
                door = STRUCT([door, row])
            else:
                door = row

    return door


def deleteDouble(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    return l


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


def createHouse1(file_name):
    walls = createWalls("wallsExt.lines")

    interior = structure("interior1.lines")
    doors = interiorDoors("doors1.lines")

    floor = createFloor("wallsExt.lines")

    doorExternal = externalDoor("doorExt.lines")
    holeWindow = windowHole("windows1.lines")

    holeWindow = OFFSET([0.03, 0.03, 0])(holeWindow)
    holeWindow = OFFSET([-0.03, -0.03, 1])(holeWindow)
    walls = OFFSET([0.01, 0.01, 4.5])(walls)  # 3
    doorExternal = OFFSET([0.03, 0.03, 0])(doorExternal)
    doorExternal = OFFSET([-0.03, -0.03, 2])(doorExternal)

    walls = DIFFERENCE([walls, holeWindow])
    walls = DIFFERENCE([walls, doorExternal])
    walls = OFFSET([0.2, 0.2, 0.01])(walls)

    doorExternal = externalDoor("doorExt.lines")
    doorExternal = OFFSET([0.1, 0.1, 2.6])(doorExternal)
    doorExternal = TEXTURE("texturePorta.jpg")(doorExternal)

    windows = createWindows("windows1.lines")
    interior = DIFFERENCE([interior, doors])

    doors = TEXTURE(["texturePorteInt.jpg", TRUE, FALSE, 1, 0, 0, 1, 2])(doors)
    walls = TEXTURE(["textureMuro.jpg", True, False, 1, 1, 0, 100, 100])(walls)
    interior = COLOR(Color4f([255 / 255., 228 / 255., 225 / 255., 1]))(interior)
    floor = TEXTURE(["texturePavimento.jpg", TRUE, FALSE, 1, 0, 0, 1, 2])(floor)
    planimetry = STRUCT([walls, interior, floor, windows, doorExternal, doors])
    return planimetry