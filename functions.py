import math, numpy as np,pandas as pd,matplotlib.pyplot as plt

def verhouding(uitrekking, afstand, dwiel):
    ass = [6, 8, 10]
    for i in ass:
        r = uitrekking / (i * math.pi)
        rwiel = dwiel * math.pi
        g = afstand / rwiel
        v = g / r
        print(g, "omwentellingen wiel")
        print(r, "omwentellingen as")
        print(v, str(i), "mm as")
    print("\n")
    return v

def assen(verhouding, uitrekking, afstand, dwiel):
    rwiel=dwiel*np.pi
    g=afstand/rwiel
    r=g/verhouding
    asdiameter=uitrekking/(math.pi*r)
    print(asdiameter)
    return asdiameter