# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import itertools
import numpy as np
import math
import random  
# pick 3 random



## creates all the possible combinations for 9 people 

numPeople = 9
numGroups = math.floor(numPeople / 2)


people = np.arange(numPeople).tolist()

numInGroup = 2
if (numPeople % 2) != 0:
    numInGroup = 3 #actually pick 3 for an odd number of people

finalGroup = []

 
class GroupGenerator:  
   def __init__(self, num_people, num_in_group):  
      self.num_people = num_people  
      self.num_in_group = num_in_group  
      self.people = np.arange(num_people).tolist()  
      self.all_groups = []  
  
   def generate_groups(self):  
      self._generate_groups(self.people, [])  
  
   def _generate_groups(self, people, current_groups):  
      if len(current_groups) == self.num_people // self.num_in_group:  
        self.all_groups.append(current_groups)  
        return  
  
      for group in itertools.combinations(people, self.num_in_group):  
        remaining_people = [person for person in people if person not in group]  
        self._generate_groups(remaining_people, current_groups + [group])  
  
   def get_all_groups(self):  
      return self.all_groups  
  
# Example usage:  
num_people = 9  
num_in_group = 2  
generator = GroupGenerator(num_people, num_in_group)  
generator.generate_groups()  
all_groups = generator.get_all_groups()  
print(all_groups)

"""
# solving three person issue
all_group1_combos = list(itertools.combinations(people, numInGroup))
all_groups = []
for j in range(len(all_group1_combos)):
    listGroups = [] #start with an empty list

    if all_group1_combos[j] in finalGroup:
        continue

    group1 = all_group1_combos[j] # add the starter choice and then base loop off remaining

    #if there is only one group this loop would not implement
    #while len(listGroups) < numGroups:
    #if group1 in finalGroup:
        
     #   continue
        
    # remove chosen people from selection
    i = 0 #iteration variable
    while i < numInGroup:
        people.remove(group1[i])
        i += 1
        
    numInGroup = 2 # update after first group, can keep setting equal to 2
    # set up next group choice
    
    all_pick2_combos = list(itertools.combinations(people, numInGroup))
    for k in range(len(all_pick2_combos)):
    #if len(all_pick_combos) > 0: # important if looping
        if all_pick2_combos[k] in finalGroup:
            continue
        group2 = all_pick2_combos[k]

        
        # remove chosen people from selection
        i = 0 #iteration variable
        while i < numInGroup:
            people.remove(group2[i])
            i += 1        
        
        all_pick3_combos = list(itertools.combinations(people, numInGroup))
        for l in range(len(all_pick3_combos)):
        #if len(all_pick_combos) > 0: # important if looping
            if all_pick3_combos[l] in finalGroup:
                #print("Skipping a group3 loop")
                continue
            group3 = all_pick3_combos[l]     
            # remove chosen people from selection
            i = 0 #iteration variable
            while i < numInGroup:
                people.remove(group3[i])
                i += 1   

            all_pick4_combos = list(itertools.combinations(people, numInGroup))
            for m in range(len(all_pick4_combos)):
            #if len(all_pick_combos) > 0: # important if looping
                
                if all_pick4_combos[m] in finalGroup:
                    #print("Not Skipping a group4 loop")
                    continue
                group4 = all_pick4_combos[m]
                finalGroup = [group1, group2, group3, group4]
                all_groups.append(finalGroup)
                # remove chosen people from selection (not really needed on final list)
                i = 0 #iteration variable
                while i < numInGroup:
                    people.remove(group4[i])
                    i += 1                   
            
                # add chosen people back in before next loop
                i = 0
                while i < numInGroup:
                    people.append(group4[i])
                    i += 1  
            # add chosen people back in before next loop
            i = 0
            while i < numInGroup:
                people.append(group3[i])
                i += 1         
        # add chosen people back in before next loop
        i = 0
        while i < numInGroup:
            people.append(group2[i])
            i += 1  
    # add chosen people back in before next loop

    people = np.arange(numPeople).tolist()
    if (numPeople % 2) != 0:
        numInGroup = 3 #actually pick 3 for an odd number of people
    all_group1_combos = list(itertools.combinations(people, numInGroup))

    
"""



# create an ordered list out of allGroups options

ordered = []

# scan through all groups for the next item in ordered
for ind, group in enumerate(all_groups):
    if group in ordered: #unnecessary check?
        continue
    else:
        if len(ordered)>0:  # condition to check list exists for index
            #check no tuples equal to each other
            if ((group[0] == ordered[-1][0]) |
            (group[1] in ordered[-1]) |
            (group[2] in ordered[-1]) |
            (group[3] in ordered[-1])): 
                #check group of 3 members are all different
                continue
        ordered.append(group)
for item in ordered:
    print(item)

"""   
def generate_grouplist(all_groups):
   # Shuffle the pairings to create a random order  
   random.shuffle(pairings)  
    
   # Initialize the ordered list of pairings  
   ordered_pairings = []  
    
   # Add the first pairing to the ordered list  
   ordered_pairings.append(pairings[0])  
    
   # Remove the first pairing from the list of pairings  
   pairings.remove(pairings[0])  
    
   # While there are still pairings left  
   while pairings:  
      # Initialize a flag to indicate if a valid pairing is found  
      valid_pairing_found = False  
       
      # Iterate over the remaining pairings  
      for pairing in pairings:  
        # Check if the current pairing does not have any individuals in common with the last pairing in the ordered list  
        if not set(pairing).intersection(set(ordered_pairings[-1])):  
           # Add the current pairing to the ordered list  
           ordered_pairings.append(pairing)  
            
           # Remove the current pairing from the list of pairings  
           pairings.remove(pairing)  
            
           # Set the flag to True  
           valid_pairing_found = True  
            
           # Break the loop as a valid pairing is found  
           break  
       
      # If no valid pairing is found, shuffle the pairings and try again  
      if not valid_pairing_found:  
        random.shuffle(pairings)  
    
   return ordered_pairings  
"""
"""
# Get the list of individuals from the user  
individuals = input("Enter the names of the individuals separated by commas: ")  
 
# Split the input string into a list of individuals  
individuals = [individual.strip() for individual in individuals.split(",")]  
 
# Generate the ordered list of pairings  
ordered_pairings = generate_pairings(individuals)  
 
# Print the ordered list of pairings  
for i, pairing in enumerate(ordered_pairings):  
   print(f"Pairing {i+1}: {pairing[0]} and {pairing[1]}")  
"""
        
   

