#Pair constructor
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

#Gets 1st element
def car(pair):
    #Executes pair and then passes in a lambda function to select the 1st element.
    return pair(lambda a,b: a)

#Gets 2nd element
def cdr(pair):
    #Executes pair and then passes in a lambda function to select the 2nd element.
    return pair(lambda a,b: b)


print(car(cons(3, 4)))
print(cdr(cons(3, 4)))
