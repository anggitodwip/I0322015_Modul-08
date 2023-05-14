import math as mt

def VolumeKubus(rusuk:float):
    return rusuk ** 3

def LPKubus(rusuk:float):
    return (rusuk ** 2) * 6

def VolumeBalok(panjang:float, lebar:float, tinggi:float):
    return panjang * lebar * tinggi

def LPBalok(panjang:float, lebar:float, tinggi:float):
    return 2 * ((panjang * lebar) + (lebar * tinggi) + (panjang * tinggi)) 

def VolumeTabung(diameter:float, tinggi:float):
    return mt.pi * (diameter ** 2) / 4 * tinggi

def LPTabung(diameter:float, tinggi:float):
    return 2 * (mt.pi * (diameter ** 2) / 4) + mt.pi * diameter * tinggi

def VolumeBola(diameter:float):
    return 4/3 * mt.pi * (diameter**3) / 8

def LPBola(diameter:float):
    return 4 * mt.pi * (diameter**2) / 4






