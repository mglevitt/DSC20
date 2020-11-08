"""
DSC 20 HW 07
NAME: Maxwell Levitt
PID: A15788481
"""

## Question 1.1 ##

def populate_menu_schedule(menu_schedule, recipe_dict):
    """
    Populate the given menu_schedule with recipes based on recipe_dict

    Parameters:
    menu_schedule (tuple): A tuple with five dictionaries representing the menu
    recipe_dict (dict): A dictionary of food recipe

    Returns:
    (None)

    >>> menu_schedule = ( \
            {"Orange Chicken": [], "Broccoli Beef": []}, \
            {"Broccoli Beef": []}, \
            {"Orange Chicken": [], "Spring Roll": []}, \
            {"Fortune Cookie": []}, \
            {"Fortune Cookie": [], "Broccoli Beef": []} \
        )
    >>> recipe_dict = { \
	        "Orange Chicken": ["Orange", "Chicken"], \
	        "Fortune Cookie": ["Fortune", "Cookie", "Paper"], \
	        "Spring Roll": ["Egg"] \
        }
    >>> populate_menu_schedule(menu_schedule, recipe_dict)
    >>> menu_schedule
    ({'Orange Chicken': ['Orange', 'Chicken']}, {}, {'Orange Chicken': \
['Orange', 'Chicken'], 'Spring Roll': ['Egg']}, {'Fortune Cookie': \
['Fortune', 'Cookie', 'Paper']}, {'Orange Chicken': ['Orange', 'Chicken']})
    >>> menu_schedule[0]['Orange Chicken'].append("Hot Sauce")
    >>> menu_schedule[2]['Orange Chicken']
    ['Orange', 'Chicken', 'Hot Sauce']
    >>> menu_schedule[0]['Gyro Plate'] = ['Beef']
    >>> menu_schedule[0]
    {'Orange Chicken': ['Orange', 'Chicken', 'Hot Sauce'], 'Gyro Plate': \
['Beef']}
    >>> menu_schedule[4]
    {'Orange Chicken': ['Orange', 'Chicken', 'Hot Sauce']}
    
    >>> recipe_dict['Spring Roll'].append(['Roll'])
    >>> menu_schedule[2]['Spring Roll']
    ['Egg']
    
    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> menu=({'burger':[],'fries':[]},{'burger':[]},{},{'salad':[],'fries':\
[]},{'salad':[]})
    >>> recipes={'burger':['cow','meat grinder'],'fries':['french','grease'],\
'brownie':['choclate']}
    >>> populate_menu_schedule(menu, recipes)
    >>> menu
    ({'burger': ['cow', 'meat grinder'], 'fries': ['french', 'grease']}, \
{'burger': ['cow', 'meat grinder']}, {}, {'fries': ['french', 'grease']}, {\
'burger': ['cow', 'meat grinder'], 'fries': ['french', 'grease']})
    >>> menu[0]['fries'].append('salt')
    >>> menu[3]['fries']
    ['french', 'grease', 'salt']
    >>> recipes['burger'].append('cheese')
    >>> menu[0]['burger']
    ['cow', 'meat grinder']
    """
    friday=4
    for item in [*menu_schedule[friday]]:
        del menu_schedule[friday][item]
    for item in [*menu_schedule[0]]:
        menu_schedule[friday][item]=[]
    place=0
    for menu in menu_schedule:
        place+=1
        for item in [*menu]:
            if item in recipe_dict:
                for day in menu_schedule[:place]:
                    if item in day:
                        menu[item]=day[item]
                        break
                if menu[item]==[]:
                    menu[item]=[i for i in recipe_dict[item]]
            else:
                del menu[item]

## Question 1.2 ##

def dereference_recipes(menu_schedule):
    """
    Dereference all pairs of recipe that refers to the same recipe object

    Parameters:
    menu_schedule (tuple): A tuple with five dictionaries representing the menu
        whose recipes have been already populated

    Returns:
    (None)

    >>> menu_schedule = ( \
            {"Orange Chicken": [], "Broccoli Beef": []}, \
            {}, \
            {}, \
            {}, \
            {"Orange Chicken": [], "Broccoli Beef": []} \
        )
    >>> oc_recipe = ['Orange', 'Chicken']
    >>> bb_recipe = ['Love']
    >>> menu_schedule[0]["Orange Chicken"] = oc_recipe
    >>> menu_schedule[4]["Orange Chicken"] = oc_recipe
    >>> menu_schedule[0]["Broccoli Beef"] = bb_recipe
    >>> menu_schedule[4]["Broccoli Beef"] = bb_recipe
    >>> menu_schedule[4]["Broccoli Beef"].append('Peace')
    >>> dereference_recipes(menu_schedule)
    >>> menu_schedule[4]["Broccoli Beef"].remove('Peace')
    >>> menu_schedule[0]["Broccoli Beef"]
    ['Love', 'Peace']
    
    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> menu=({'burger':[],'fries':[],'salad':[]},{'burger':[]},{},{'salad':[]\
,'fries':[]},{'salad':[],'brownie':[]})
    >>> recipes={'burger':['cow','meat grinder'],'fries':['french','grease'],\
'brownie':['choclate'],'salad':['greens','vegtables']}
    >>> populate_menu_schedule(menu, recipes)
    >>> dereference_recipes(menu)
    >>> menu[0]['salad'].append('red')
    >>> menu[3]['salad']
    ['greens', 'vegtables']
    >>> menu[1]['burger']=['meat']
    >>> menu[0]['burger']
    ['cow', 'meat grinder']
    >>> menu[0]['fries'].pop()
    'grease'
    >>> menu[0]['fries']
    ['french']
    >>> menu[3]['fries']
    ['french', 'grease']
    """
    place=0
    for day in menu_schedule:
        place+=1
        for item in [*day]:
            for menu in menu_schedule[:place]:
                for food in [*menu]:
                    if day[item]==menu[food]:
                        day[item]=[i for i in menu[food]]
        
            


## Question 2 is in hw07_OOP.py ##

## Question 3.1 ##

def create_palindrome_v1(start, end):
    """
    Creates a palindrome of integers starting from start, ending at end
    (in the middle) All inputs are positive integers. No input validation
    required.
    Parameters: start, end (int), positive integers
    Returns: palindrome sequence (str)
    Restrictions. You should use recursion in this question.
    >>> create_palindrome_v1(1, 1)
    '1'
    >>> create_palindrome_v1(3, 5)
    '34543'
    >>> create_palindrome_v1(5, 2)
    '5432345'
    
    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> create_palindrome_v1(9, 1)
    '98765432123456789'
    >>> create_palindrome_v1(11, 7)
    '1110987891011'
    >>> create_palindrome_v1(0, 3)
    '0123210'
    """
    if start>end:
        return str(start)+create_palindrome_v1(start-1,end) +str(start)
    elif start<end:
        return str(start)+create_palindrome_v1(start+1,end)+str(start)
    else:
        return str(start)
    
        


## Question 3.2 ##

def create_palindrome_v2(start1, end1, start2, end2):
    """
    Creates a two level palindrome of integers. The first level (outer level)
    starts from start1 and ends at end1. The second level (inner level) starts
    from start2 and end2. No input validation is required.
    Parameters: start1, end1, start2, end2 (int), positive integers
    Returns: palindrome sequence (str)
    Restrictions. You should use recursion in this question.
    >>> create_palindrome_v2(1, 1, 1, 1)
    '1_1_1'
    >>> create_palindrome_v2(2, 5, 5, 4)
    '2345_545_5432'
    >>> create_palindrome_v2(3, 1, 5, 9)
    '321_567898765_123'
    
    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> create_palindrome_v2(3, 4, 9, 1)
    '34_98765432123456789_43'
    >>> create_palindrome_v2(1, 2, 3, 4)
    '12_343_21'
    >>> create_palindrome_v2(0, 0, 0, 0)
    '0_0_0'
    """
    if start1>end1:
        return str(start1)+create_palindrome_v2(start1-1,end1,start2,end2)+str(start1)
    elif start1<end1:
        return str(start1)+create_palindrome_v2(start1+1,end1,start2,end2)+str(start1)
    else:
        return str(start1)+'_'+create_palindrome_v1(start2,end2)+'_'+str(start1)
