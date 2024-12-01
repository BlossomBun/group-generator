# -*- coding: utf-8 -*-
"""
Marie-Pierre Kippen
November 29, 2024

Script generates a series of groups (assumed one per month) based on user-input
of names and people per group. Individuals are not paired with the same set of 
individuals two months in a row.

EDIT: DECEMBER 01, 2024 - update to initialize with Hannah's first group.
                        - update to prevent two members from past trio grouping


A better AI-generated description: 
The provided Python script is designed to generate groups of individuals based
on user input, ensuring that no group of individuals is paired together in 
consecutive months. 

1. It begins by importing necessary libraries (itertools for combinations and 
random for shuffling). 

2. The function generate_groups recursively creates combinations of the people 
while considering the preferred size of the groups, adjusting if necessary when
the total number of people is not divisible by the group size.

3. The remove_repeated_groupings function filters out duplicate groups based on 
their member compositions, despite different orders.

4. The generate_grouplist function shuffles the groups and ensures no individual
is in the same combination as in the previous month, utilizing checks for
overlap in memberships. 

5. The print_group_names function formats and prints the groups for each
month. 

6. The script is initiated in the MAIN section, where it captures user input
for names and the desired group size, processes the data through the defined 
functions, and outputs the resulting groups.Hannah, Nick, Ian, Mike, Eileen, Anna-Kate, Spencer, Christian, Rizana

"""

import itertools # Import itertools for combination generation
import random  # Import random for shuffling the groups

# Creates all the possible combinations for the specified number of people
def generate_groups(people, user_num_in_group, current_groups, final_groups):  
    # If there are no remaining people, add the current grouping to the final list
    if len(people) == 0:  
        final_groups.append(current_groups)  
        return  
      
    # Adjust the number in group if the length isn't divisible by user-num
    num_in_group = user_num_in_group
    if len(people) % user_num_in_group != 0:
        num_in_group = user_num_in_group + 1 # add an individual to the group
    
    # Generate all combinations of the specified number of individuals
    all_combos = list(itertools.combinations(people, num_in_group))  
    
    # Iterate through each combination to generate further groups
    for combo in all_combos:  
        remaining_people = [person for person in people if person not in combo]
        # Recursive call
        generate_groups(remaining_people, user_num_in_group, current_groups + [combo], final_groups)  


# Function removes groups made up of the same pairings in a different order
def remove_repeated_groupings(all_groups):
    final_groups = [] # Initialize a list for unique groups
    
    for ind, group in enumerate(all_groups):
        # Add the current group to final_groups
        final_groups.append(group)
        i = 0
        
        # Check if the group is a duplicate by comparing with existing groups
        while i < len(final_groups)-1:          
            if set(group) == (set(final_groups[i])):
                # Remove the current group if it is a duplicate
                final_groups.remove(group)
                
                # Exit the loop if group is removed is found
                break
            i += 1
            
    return final_groups # Return the list of unique groups
       
def find_group_match(list_list_tuples, list_tuples):
    index = 0
    for i, group in enumerate(list_list_tuples):
        if set(list_tuples) == set(group):
            index = i
    return index
        

def generate_grouplist(groups, user_group0):
    # Shuffle the pairings to create a random order  
    random.shuffle(groups)  
     
    # Initialize the ordered list of pairings  
    ordered_groups = []  
    
    # Returns 0 if no match
    index = find_group_match(groups, user_group0)
    
    # Add the first pairing to the ordered list  
    ordered_groups.append(groups[index])    
    
    # Remove the first pairing from the list of pairings  
    groups.remove(groups[index])  

    # Maintain a previous group for comparison in the next iterationin spite of shuffling groups
    prev_group = ordered_groups[0] 
    
    # Count trials in case no valid groups remain
    trials = 0
    
    # While there are still pairings left and not too many trials have occured 
    while groups and trials <= 700:  
        
        # Initialize a flag to indicate if a valid pairing is found  
        valid_group_found = False  
           
        # Iterate over the remaining pairings  
        for group in groups:  
            # Perform four checks  
            #  1. Groups's odd trio does not have any individuals shared with the previous group's trio
            #  2. Group does not have any tuples shared with the previous group in the ordered list 
            #  3. Groups's odd group does not contain any subsets of the previous groups's groups
            #  4. Groups's tuples are not made up of two members from the previous groups's trio
            if (
             not set(group[0][:]).intersection(set(prev_group[0][:]))   #1
               ) and (
             not set(group).intersection(set(prev_group))               #2
               ) and (
             not any (set(x) <= set(group[0]) for x in prev_group[:])   #3
               ) and (
             not any (set(x) <= set(prev_group[0]) for x in group[:])   #4
               ): 
                       
                    # Add the current pairing to the ordered list  
                    ordered_groups.append(group)  
                    
                    # Update the previous group for the next iteration
                    prev_group = group
                    
                    # Remove the current pairing from the list of pairings  
                    groups.remove(group)  
                    
                    # Mark that a valid group has been found
                    valid_group_found = True  
                     
                    # Exit the loop as a valid pairing has been found  
                    break
                
            # Shuffle the remaining groups and increment trial count if no valid group was found
            if not valid_group_found:  
                random.shuffle(groups)  
                trials += 1

    return ordered_groups  # Return the ordered list of groups

def print_group_names(groups):
    # Print the ordered list of pairings  
    for i, group in enumerate(groups):  
        print(f"Group for month {i+1}: ",end = "") 
        for pairing in group:
            print("( ", end = "")
            for person in pairing:
                print(f"{person.capitalize()} ", end = "") # Capitalize names for display
            print(")  ",end= "")
        print() # New line after each group
    return


def create_list_tuples_from_user_input(people_str):
    # Split the input string into a list of individuals  
    group = []
    people_group = [people.strip() for people in people_str.split(",")] 
    
    while people_group:
        code_num_in_group = num_in_group
        
        if len(people_group) % num_in_group != 0:
            code_num_in_group = num_in_group + 1 # add an individual to the group

        subgroup = people_group[0:code_num_in_group]
        people_group = people_group[code_num_in_group:] #check this does what it should
        group.append(tuple(subgroup)) #add subgroup to list of group0 as a tuple
        
    return group
    
def get_user_input_group0():
    user_group0_flag = input("Do you have an initial group? (y/n)  ").strip().lower()

    if user_group0_flag == "y":
        
        print("List the starting groups in the format: Aaa, Bbb, Ccc, ... ")
        print("Match spelling and capitalization with your input values.")
        group0_str = input("The grouping will be created from: ")
        group0 = create_list_tuples_from_user_input(group0_str)
        
        correct_input_flag = "n"
        while correct_input_flag == "n":
            print("Your group has been parsed as:")
            print_group_names([group0])    
            correct_input_flag = input("Is this the grouping you meant? (y/n)   ").strip().lower()
            
            if correct_input_flag == "n":
                print("Okay, let's try again.")
                group0_str = input("The grouping will be created from: ")
                group0 = create_list_tuples_from_user_input(group0_str)
    else:
        group0 = []
        
    return group0

""" MAIN """

# Collect names from user input
people = input("Enter the names of the individuals separated by commas: ")  
 
# Split the input string into a list of individuals  
people = [people.strip() for people in people.split(",")]  

# Get the number of individuals desired in each group from user input
# Note "odd" groupings will be added as needed.
num_in_group = input("Enter the number of desired individuals in each group: ")

# Convert input into an integer
num_in_group = int(num_in_group)

# Ask if user has a starting group. If not, returns an empty list
group0 = get_user_input_group0()

# Initialize empty list to hold all possible unique groups
all_groups = []  

# Generate all possible groups based on the input
generate_groups(people, num_in_group, [], all_groups)  

# Remove any duplicate groupings from all_groups
all_groups = remove_repeated_groupings(all_groups)

# Generate the ordered list of pairings ensuring no duplicates month-to-month
ordered_groups = generate_grouplist(all_groups, group0) 

# Print the names of individuals in each group
print_group_names(ordered_groups)