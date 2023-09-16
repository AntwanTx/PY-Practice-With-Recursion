# Write code for algorithm 5 below

def pal_check(string):
    # base case:
    if len(string) == 1 or len(string) == 0:
        return True
    
    # recursive case:
    else:
        return string[0] == string[-1] and pal_check(string[1:-1])
            



print(pal_check("tacocat"))