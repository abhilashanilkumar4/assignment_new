def reverse_string(string):

    B = []
    for char in string:
        B.append(char)
    
    reversed_string = ""
    while B:
        reversed_string += B.pop()
    
    return reversed_string

string = "hello, world!"
print(reverse_string(string)) 
