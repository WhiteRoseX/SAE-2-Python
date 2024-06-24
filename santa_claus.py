from time import time
from math import *
from numpy import *
from random import *

##############
# SAE S01.01 #
##############

def nb_villes(villes):
    """Retourne le nombre de villes"""
    return len(villes)//3


def noms_villes(villes):
    """Retourne un tableau contenant le nom des villes"""
    noms_v = []
    i = 0
    while 3*i < len(villes):
        noms_v.append(villes[3*i])
        i += 1
    return noms_v


def d2r(nb):
    return nb*pi/180


def distance(long1, lat1, long2, lat2):
    """retourne la distance entre les points (long1, lat1) et (long2, lat2)"""
    lat1 = d2r(lat1)
    long1 = d2r(long1)
    lat2 = d2r(lat2)
    long2 = d2r(long2)
    R = 6370.7
    d = R*arccos(sin(lat1)*sin(lat2)+cos(lat1)*cos(lat2)*cos(long2-long1))
    return d


def indexCity(ville, villes):
    """Retourne l'indice dans le tableau villes de la ville de nom ville,
       et -1 si elle n'existe pas
    """
    res = -1
    i = 0
    while 3*i < len(villes) and villes[3*i] != ville:
        i += 1
    if 3*i < len(villes):
        res = 3*i
    return res


def distance_noms(nom1, nom2, villes):
    """Retourne la distance entre les villes nom1 et nom2 
       en fonction de la structure de données villes
    """
    index1 = indexCity(nom1, villes)
    index2 = indexCity(nom2, villes)

    if index1 == -1 or index2 == -1:
        d = -1
    else:
        d = distance(villes[index1+1], villes[index1+2],
                     villes[index2+1], villes[index2+2])
    return d


def lecture_villes(path):
    """Retourne la structure de données villes en fonction des données du fichier path"""
    f_in = open(path, encoding='utf-8', mode='r')
    villes = []
    li = f_in.readline()
    li = li.strip()
    while li != '':
        tab_li = li.split(';')
        villes.append(tab_li[0])
        villes.append(float(tab_li[1]))
        villes.append(float(tab_li[2]))
        li = f_in.readline()
        li = li.strip()
    f_in.close()
    return villes


def long_tour(villes, tournee):
    """Retourne la longueur d'une tournée en fonction de la structure de données villes"""
    long = 0
    i = 0
    while i+1 < len(tournee):
        long += distance_noms(tournee[i], tournee[i+1], villes)
        i += 1
    long += distance_noms(tournee[i], tournee[0], villes)
    return long

##############
# SAE S01.02 #
##############


def dictionary_cities(villes):
    """ Transforme un tableau de villes avec les distances en dictionnaires contenant pour chaque clé un sous dictionnaire avec les autres villes ainsi que leurs distances respectives """
    distances_dico = {}
    n = nb_villes(villes)
    i = 0 
    while i < n:
        city1 = villes[i * 3]
        distances_dico[city1] = {}
        j = 0 
        while j < n: 
            if i != j: 
                city2 = villes[j*3]
                dist = distance_noms(city1, city2, villes)
                distances_dico[city1][city2] = dist
            j += 1
        i += 1 
    return distances_dico


def distance_cities(city1, city2, distances):
    """ Permet de retourner la distance entre deux villes via les clés du dictionnaire"""
    if city1 in distances and city2 in distances[city1]:
        return distances[city1][city2]
    else:
        return -1

def tour_length(tour, distances):
    """ Renvoi la longueur du tour """
    length = 0
    n = len(tour)
    
    for i in range(n - 1):
        length += distance_cities(tour[i], tour[i+1], distances)
    
    length += distance_cities(tour[-1], tour[0], distances)
    return length

def closest_city(city, cities, distances):
    """Renvoi l'index de la ville la plus proche de la ville donné en premier argument """
    min_distance = float('inf')
    closest_index = -1
    
    for i, other_city in enumerate(cities):
        if other_city != city:
            dist = distance_cities(city, other_city, distances)
            if dist != -1 and dist < min_distance:
                min_distance = dist
                closest_index = i
    
    return closest_index

def tour_from_closest_city(start_city, distances):
    """ Retourne un tour classé dans l'orde des villes les plus proches """
    tour = [start_city]
    remaining_cities = list(distances.keys())
    remaining_cities.remove(start_city)
    
    while remaining_cities:
        current_city = tour[-1]
        closest_index = closest_city(current_city, remaining_cities, distances)
        closest_city_name = remaining_cities[closest_index]
        tour.append(closest_city_name)
        remaining_cities.remove(closest_city_name)
    
    return tour

def best_tour_from_closest_city(distances):
    """retourne le meilleur tour parmi ceux obtenus avec l'algorithme précédent en prenant chaque ville comme ville de départ"""
    best_tour = None
    best_length = float('inf')
    
    for start_city in distances.keys():
        tour = tour_from_closest_city(start_city, distances)
        tour_len = tour_length(tour, distances)
        
        if tour_len < best_length:
            best_length = tour_len
            best_tour = tour
    
    return best_tour

def reverse_part_tour(tour, ind_b, ind_e):
    """Permet d'améliorer encore le tour en effectuant plusieurs modifications """
    tour[ind_b:ind_e+1] = reversed(tour[ind_b:ind_e+1])


def inversion_length_diff(tour, distances, ind_b, ind_e):
    """retourne la différence entre la distance du tour passé en paramètre et celui obtenu en inversant la partie du tour entre les ind_b et ind_e """
    original_length = tour_length(tour, distances)
    reversed_tour = tour.copy()
    reverse_part_tour(reversed_tour, ind_b, ind_e)
    reversed_length = tour_length(reversed_tour, distances)
    
    return original_length - reversed_length

def better_inversion(tour, distances):
    """Applique une inversion si il est possible"""
    n = len(tour)
    improvement = False
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            diff = inversion_length_diff(distances, tour, i, j)
            
            if diff > 0:
                improvement = True
                reverse_part_tour(tour, i, j)
    
    return improvement

def best_obtained_with_inversions(tour, distances):
    """Retourne le nombre d'inversions éfféctuées"""
    num_inversions = 0

    while better_inversion(tour, distances):
        num_inversions += 1
    
    return num_inversions