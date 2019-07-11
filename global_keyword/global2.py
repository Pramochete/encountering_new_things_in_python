# What if we want to modify global variable from function

g=2        # Global variable

def know_it():
    g=g+2
    print(g)

know_it()  # We get an error "UnboundLocalError: local variable 'g' referenced before assignment"