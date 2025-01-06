import re
from collections import Counter
import numpy as np

def check_page_updates(page_rules, page_updates):
    correct_updates = 0
    
    # Parse page rules into a list of tuples (before, after)
    rules = []
    for rule in page_rules:
        before, after = rule.split('|')
        rules.append((before, after))
    
        # Check each page update list
    for page_update in page_updates:
        is_correct = True  # Assume the update is correct initially
        
        # Create a dictionary to store the indices of each page in the page_update
        page_indices = {page: idx for idx, page in enumerate(page_update)}
        
        # For each rule, check if the order of pages is respected
        for before, after in rules:
            if before in page_indices and after in page_indices:
                # Check if 'before' appears before 'after' in the update
                if page_indices[before] > page_indices[after]:
                    is_correct = False
                    break
        
        if is_correct:
            correct_updates += int(page_update[int(len(page_update) / 2)])
    
    return correct_updates


def check_page_updates_and_sort(page_rules, page_updates):
    correct_updates = 0
    
    # Parse page rules into a list of tuples (before, after)
    rules = []
    for rule in page_rules:
        before, after = rule.split('|')
        rules.append((before, after))
    
        # Check each page update list
    for page_update in page_updates:
        correct_order = False  # Correct order of this page update
        
        # Create a dictionary to store the indices of each page in the page_update
        page_indices = {page: idx for idx, page in enumerate(page_update)}
        
        # For each rule, check if the order of pages is respected
        while True:
            incorrect_pages_count = 0
            for before, after in rules:
                if before in page_indices and after in page_indices:
                    # Check if 'before' appears before 'after' in the update
                    if page_indices[before] > page_indices[after]:
                        #swap the indices
                        page_indices[before], page_indices[after] = page_indices[after], page_indices[before]
                        correct_order = True
                        incorrect_pages_count += 1
                        break
            if incorrect_pages_count == 0:
                break

        if correct_order:
            # Sort the page update list using the swapped dictionary
            sorted_page_update = sorted(page_update, key=lambda x: page_indices[x])
            correct_updates += int(sorted_page_update[int(len(sorted_page_update) / 2)])
        else:
            continue
    
    return correct_updates

with open('Input2024_5.txt', 'r') as file:
#with open('test.txt', 'r') as file:
    lst = file.read().strip().split("\n")
    index = lst.index("") 
    page_rules, page_updates = lst[:index], [page_update.split(',') for page_update in lst[index + 1:]]

    #sum = check_page_updates(page_rules, page_updates)
    
    sum = check_page_updates_and_sort(page_rules, page_updates)

    print(sum)
