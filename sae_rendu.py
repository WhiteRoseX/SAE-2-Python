from santa_claus import *


def dictionary_cities(villes):
    
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
    if city1 in distances and city2 in distances[city1]:
        return distances[city1][city2]
    else:
        return -1

def tour_length(tour, distances):
    length = 0
    n = len(tour)
    
    for i in range(n - 1):
        length += distance_cities(tour[i], tour[i+1], distances)
    
    length += distance_cities(tour[-1], tour[0], distances)
    return length

def closest_city(city, cities, distances):
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
    tour[ind_b:ind_e+1] = reversed(tour[ind_b:ind_e+1])

def inversion_length_diff(distances, tour, ind_b, ind_e):
    original_length = tour_length(tour, distances)
    reversed_tour = tour.copy()
    reverse_part_tour(reversed_tour, ind_b, ind_e)
    reversed_length = tour_length(reversed_tour, distances)
    
    return original_length - reversed_length


def better_inversion(tour, distances):
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
    num_inversions = 0

    while better_inversion(tour, distances):
        num_inversions += 1
    
    return num_inversions


tableau = ["Paris",2.33, 48.86, "Lyon", 4.85, 45.75, "Marseille", 5.40, 43.30, "Lille", 3.06, 50.63]
resultat = dictionary_cities(tableau)

tourr = ["Paris", "Lyon", "Marseille", "Lille"]
tour2 = ["Marseille", "Paris", "Lyon", "Lille"]
## res = distance_cities("Paris", "Marseille", resultat)
## longueur = tour_length(tourr, resultat)
## print(res)
## print(longueur)
##res = closest_city("Paris", ["Marseille", "Lyon"], resultat)
## print(res)
res = tour_from_closest_city("Marseille", resultat)
print(res)

##res = best_tour_from_closest_city(resultat)
## print(res)
"""
tour_test = ["Agen", "Belfort", "Cahors", "Dijon", "Épinay", "Fréjus", "Grenoble", "Hyères"]
reverse_part_tour(tour_test, 2, 5)
print(tour_test)
"""
##res = better_inversion(tour2, resultat)
#res = inversion_length_diff(resultat, tour2, 1, 2)
##print(res)

print(tour2)
s = best_obtained_with_inversions(tour2, resultat)
print(tour2)
print(s)
    
def test_dictionnaire_cities():
    assert dictionary_cities(resultat)=={'Paris': {'Lyon': 394.5056834297657, 'Marseille': 661.8616554466852, 'Lille': 203.67224282542662}, 'Lyon': {'Paris': 394.5056834297657, 'Marseille': 275.87965367431525, 'Lille': 558.5472363339435}, 'Marseille': {'Paris': 661.8616554466852, 'Lyon': 275.87965367431525, 'Lille': 834.0220261600157}, 'Lille': {'Paris': 203.67224282542662, 'Lyon': 558.5472363339435, 'Marseille': 834.0220261600157}}
    assert dictionary_cities(resultat)=={'Paris': {'Lyon': 394.5056834297657, 'Clermont-Ferrand': 348.1917463926894, 'Bordeaux': 499.33539949226133,}, 'Lyon': {'Paris': 394.5056834297657, 'Clermont-Ferrand': 137.3197723283378, 'Bordeaux': 436.0446433181221}, 'Clermont-Ferrand': {'Paris' : 348.1917463926894, 'Lyon': 137.3197723283378, 'Bordeaux': 303.9643815204919}, 'Bordeaux': {'Paris': 499.33539949226133, 'Lyon': 436.0446433181221, 'Clermont-Ferrand': 303.9643815204919}}
    print("Test Ok")

test_dictionnaire_cities()