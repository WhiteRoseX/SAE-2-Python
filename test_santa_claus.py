from santa_claus import *
from math import*
#Question 1:
ville = ["Paris",2.33,48.86, "Lyon",4.85,45.75, "Clermont-Ferrand",3.08,45.77, "Bordeaux",-0.57, 44.83]
villes = ["Paris",2.33,48.86, "Lyon",4.85,45.75, "Marseille",5.40,43.30, "Lille",3.06,50.63]

def test_dictionnaire_cities():
    assert dictionary_cities(villes)=={'Paris': {'Lyon': 394.5056834297657, 'Marseille': 661.8616554466852, 'Lille': 203.67224282542662}, 'Lyon': {'Paris': 394.5056834297657, 'Marseille': 275.87965367431525, 'Lille': 558.5472363339435}, 'Marseille': {'Paris': 661.8616554466852, 'Lyon': 275.87965367431525, 'Lille': 834.0220261600157}, 'Lille': {'Paris': 203.67224282542662, 'Lyon': 558.5472363339435, 'Marseille': 834.0220261600157}}
    assert dictionary_cities(villes)=={'Paris': {'Lyon': 394.5056834297657, 'Clermont-Ferrand': 348.1917463926894, 'Bordeaux': 499.33539949226133,}, 'Lyon': {'Paris': 394.5056834297657, 'Clermont-Ferrand': 137.3197723283378, 'Bordeaux': 436.0446433181221}, 'Clermont-Ferrand': {'Paris' : 348.1917463926894, 'Lyon': 137.3197723283378, 'Bordeaux': 303.9643815204919}, 'Bordeaux': {'Paris': 499.33539949226133, 'Lyon': 436.0446433181221, 'Clermont-Ferrand': 303.9643815204919}}
    print("Test Ok")

test_dictionnaire_cities()

#Question 2:
def test_distance_cities():
    assert round(distance_cities("Marseille", "Paris"),13)==661.8616554466852
    assert distance_cities("Porto", "Paris")==-1
    print("Test Ok")
test_distance_cities()


#Question 3:
def test_tour_length():
    assert round(tour_length(["Paris", "Lyon", "Marseille", "Lille" ]),13)==1708.0796060895232
    assert round(tour_length(["Paris", "Lyon"]),13)==789.0113668595314
    print("Test Ok")
test_tour_length()

#Question 5:    
def test_closest_city():
    assert closest_city("")==""
    assert closest_city("Paris",["Lille", "Lyon"])=="Lille"        
    assert closest_city("Paris",["Marseille", "Lyon"])=="Lyon"
    print("Test Ok")
test_closest_city()

#Question 6:
def test_tour_from_closest_city():
    assert tour_from_closest_city("Marseille", dico_dis)==["Marseille", "Lyon", "Paris", "Lille"]
    assert tour_from_closest_city("Paris", dico_dis)==["Paris", "Lille", "Lyon", "Marseille"]
    assert tour_from_closest_city("Paris",789.0113668595314)== 0
    print("Test Ok")
test_tour_from_closest_city()

#Question 7:
def test_best_tour_from_closest_city():
    assert  best_tour_from_closest_city(dico_dis)==["Paris", "Lille", "Lyon", "Marseille"]
    assert  best_tour_from_closest_city(dico_dis)==["Lyon", "Marseille", "Paris", "Lille"]
    print("Test Ok")
test_best_tour_from_closest_city()


#Question 9:
def test_reverse_part_tour():
    assert reverse_part_tour(t, 1, 2)==["Belfort", "Agen", "Cahors", "Dijon", "Épinay",'Fréjus','Grenoble', 'Hyères' ]
    assert reverse_part_tour(t, 1, 5)==['Agen', 'Belfort', 'Fréjus', 'Épinay', 'Dijon', 'Cahors', 'Grenoble', 'Hyères']
    print("Test Ok")
test_reverse_part_tour()

#Question 10:
def test_inversion_length_diff():
    assert round(inversion_length_diff(t, dico_dis, ind_e, ind_b),13)== -740.8569952202271
    assert inversion_length_diff("")==""
    print("Test Ok")
test_inversion_length_diff()

#Question 11:
tab=["Marseille", "Paris", "Lyon", "Lille"]
def test_better_inversion():
    assert better_inversion (t, dico_dis)== True
    print("Test Ok")
test_better_inversion()

#Question 12:

tab=["Marseille", "Paris", "Lyon", "Lille"]
def test_best_obtained_with_inversions():
    assert best_obtained_with_inversions(t, dico_dis)==1
    print("Test Ok")
test_best_obtained_with_inversions()