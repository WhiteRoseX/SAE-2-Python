from santa_claus import * 
"""## test algo de tri 

tableau = [1,9,3,4,7,2,75,47,31,19]

def algo_tri_selectif(array):
    
    n = len(array) - 1

    i = 0 

    while i < n - 1: 
        
        minimum_index = i

        j = i+1

        while j < n: 

            if array[minimum_index] > array[j]:

                temporaire = array[minimum_index]

                array[minimum_index] = array[j]  

                array[j] = temporaire  
            
            j += 1
        
        i += 1


algo_tri_selectif(tableau)

print(tableau)"""

def algo_tri_selectif(array):
    n = len(array)

    i = 0

    while i < n - 1:
        minimum_index = i
        j = i + 1
        while j < n:
            if array[minimum_index] > array[j]:
                # Échanger les éléments si l'élément actuel est plus petit que l'élément minimum trouvé jusqu'à présent
                array[minimum_index], array[j] = array[j], array[minimum_index]
            j += 1
        i += 1

# Test de la fonction
tableau = [1, 9, 3, 4, 7, 2, 75, 47, 31, 19]
algo_tri_selectif(tableau)
print(tableau)

# ----------------------------------------------------------------------------------------------------------------------------------




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


def distance_cities(city1, city2, dico):
    if city1 and city2 in dico:
        return dico[city1][city2]
    else: 
        return -1 
    
def tour_length(tour, distances): 
    tour_len = 0
    i = 0 
    while i < len(tour) - 1 :
        city1 = tour[i] 
        city2 = tour[i+1] 
        tour_len += distance_cities(city1, city2, distances)
        i += 1  
    tour_len += distance_cities(tour[-1], tour[0], distances)
    return tour_len

def closest_city(city, cities, distances):
    min_distance = float('inf')
    closest_index = -1
    i = 0
    
    while i < len(cities):
        other_city = cities[i]
        if other_city != city:
            dist = distance_cities(city, other_city, distances)
            if dist != -1 and dist < min_distance:
                min_distance = dist
                closest_index = i
        i += 1
    
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


    



tableau = ["Paris",2.33, 48.86, "Lyon", 4.85, 45.75, "Marseille", 5.40, 43.30, "Lille", 3.06, 50.63]
resultat = dictionary_cities(tableau)
print(resultat)
tour = ["Paris", "Lyon", "Marseille", "Lille"]
d = tour_length(tour, resultat)
print(d)
r = closest_city("Paris",["Marseille", "Lyon"],resultat)
print(r)
l = tour_from_closest_city(tour, resultat)
print(l)