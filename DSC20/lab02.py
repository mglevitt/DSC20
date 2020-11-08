
# Question 1​

def pass_num(input):
    """
    Return the number of times 'pass' occurs. 
    Stop calculating when you reach a 'stop'.
    >>> pass_num("passpass")
    2
    >>> pass_num("passpasspasspasspassstop")
    5
    >>> pass_num("passtopass")
    1
    >>> pass_num("stoppasspass")
    0
    >>> pass_num("marinaspasport")
    0
    """
    count=0
    strings=input.split('stop')
    string=strings[0]
    count1=len(string.split('pass'))-1
    count2=len(string.split('pas'))-1
    if count1==count2:
        count=count1
    elif count1==count2-1 and (string.split('pas'))[count2]=='':
        count=count2
    return count
    

# Question 2
lst_letters = ["a", "c", "e", "k", "m", "o", "p", "x", "y"]

def common_letters(input):
    """
    Return the number of letters that are the same in the Russian alphabet.
    >>> common_letters("marina")
    3
    >>> common_letters("marina langlois")
    5
    >>> common_letters("dsc20 is fun!")
    1
    >>> common_letters("ace is a ok")
    6
    >>> common_letters("")
    0
    """
    count=0
    for i in lst_letters:
        count+=(len(input.split(i))-1)
    return count
    

# Question 3

def capitalize_letters(names):
    """
    Capitalize the first letter in each element of names. 
    Return the list with capitalized names. 
    >>> capitalize_letters(["marina"])
    ['Marina']
    >>> capitalize_letters(["rob", "marina"])
    ['Rob', 'Marina']
    >>> capitalize_letters(["rOBERT", "mARINA"])
    ['ROBERT', 'MARINA']
    >>> capitalize_letters(["m", "a", "r", "i", "n", "a"])
    ['M', 'A', 'R', 'I', 'N', 'A']
    >>> capitalize_letters([])
    []
    """
    up_names=[]
    for i in names:
        name=i[0].upper()+i[1:len(i)]
        up_names.append(name)
    return up_names
    

# Question 4

def populate_dictionary(countries, capitals):
    """
    Create a dictionary from two lists with countries as the key and 
    capitals as the value. 
    >>> d1 = populate_dictionary(["russia", "france"], ["moscow", "paris"])
    >>> d1['russia'] == 'moscow'
    True
    >>> d1.items()
    dict_items([('russia', 'moscow'), ('france', 'paris')])

    >>> d2 = populate_dictionary(["japan"], ["tokyo"])
    >>> d2['japan'] = 'tokyo'
    >>> d2.items()
    dict_items([('japan', 'tokyo')])

    >>> d3 = populate_dictionary([], [])
    >>> not d3
    True
    """
    dictionary={}
    for i in range(len(countries)):
        temp={countries[i]:capitals[i]}
        dictionary.update(temp)
    return dictionary
def check_what_capital(country, capitals_dict):
    """
    Return the capital of the country if it exists. 
    Else return that the country does not exist. 
    >>> d1 = populate_dictionary(["russia", "france"], ["moscow", "paris"])
    >>> check_what_capital("russia", d1)
    'Capital of country russia: moscow'
    >>> check_what_capital("usa", d1)
    'usa does not exist in the database'

    >>> d2 = populate_dictionary(["japan"], ["tokyo"])
    >>> check_what_capital("japan", d2)
    'Capital of country japan: tokyo'

    >>> d3 = populate_dictionary([], [])
    >>> check_what_capital("france", d3)
    'france does not exist in the database'

    """
    if country in capitals_dict:
        return 'Capital of country '+country+': '+capitals_dict[country]
    else:
        return country+' does not exist in the database'
