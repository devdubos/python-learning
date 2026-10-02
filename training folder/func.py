def to_jaden_case(string):
    string1= string.split()
    string1 = [i.capitalize() for i in string1]
    string2 = " ".join(string1)
    return string2
    
def to_camel_case(string):
    words = string.split()
    capitalized_words = [word.capitalize() for word in words]
    return "".join(capitalized_words)

def pig_latin(string):
    words = string.split()
    transformed_words = [word[1:] + word[0] + "ay" for word in words]
    return " ".join(transformed_words)

def filter_list(l):
    result = []
    for i in l:
        if type(i) == int:
            result.append(i)
    return result

def filter_strings(l):
    result = []
    for i in l:
        if type(i) == str: 
            result.append(i)
    return result

def filter_strings(l):
    return [i for i in l if type(i) == str]


def get_even_numbers(l):
    result = []
    for i in l:
        if i % 2 == 0:
            result.append(i)
    return result