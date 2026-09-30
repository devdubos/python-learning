def to_jaden_case(string):
    string1= string.split()
    string1 = [i.capitalize() for i in string1]
    string2 = " ".join(string1)
    return string2
    