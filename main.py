#from copy import copy
#from tkinter import N
from re import M
import numpy as np
import random
import csv

min_number_of_specimens = 5
max_number_of_specimens = 50
stat = [0, 0, 0, 0] #cod, pollock, haddock, whitting


def generate_species_and_specimens():
    #species = ["cod", "pollock", "haddock", "whitting", "other"]
    options = ["cod", "pollock", "haddock", "whitting"]
    sum = random.randint(min_number_of_specimens, max_number_of_specimens)
    #print(sum)

    arr = np.random.randint(100, size=len(options))
    arr = np.divide(arr, np.sum(arr))
    #print(arr)
    
    specimens = np.around(arr*sum)
    #print(specimens)

    random.shuffle(options)
    #print(options)

    species_order = []
    for (fish, number) in zip(options, specimens):
        for i in range(int(number)):
            species_order.append(fish)
    #print(species_order)

    return specimens, options, species_order
    
    
def generate_mapping(species_order):
    options = ['LT', 'LC', 'LB', 'CT', 'CC', 'CB', 'RT', 'RC', 'RB']
    len_options = len(options)
    diff = len(species_order) - len(options)
    if diff > 0:
        for i in range(diff):
            options.append(options[random.randint(0, len_options-1)])
    if diff < 0:
        for i in range(abs(diff)):
             options.pop(random.randint(0, len(options)-1))
    
    random.shuffle(options)
    #print(options)
    return options


def get_statistics(specimens, species_order):
    species = ["cod", "pollock", "haddock", "whitting"]
    global stat
    for (number, fish) in zip(specimens, species_order):
        idx = species.index(fish)
        stat[idx] += number 


if __name__=="__main__":
    header = ['Image', 'Species', 'Specimens', 'Positions']
    number_of_images = 500
    for i in range(number_of_images):
        specimens, species_order, species_order_long = generate_species_and_specimens()
        mapping =generate_mapping(species_order_long)
        statistics = get_statistics(specimens, species_order)
        
        print(specimens)
        print(species_order)
        print(mapping)
        print("===================")
    print(stat)
    for value in stat:
        temp = value/sum(stat)*100
        print(temp)