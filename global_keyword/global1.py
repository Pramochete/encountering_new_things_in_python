# Global is used to create a global variable and make changes to the variable in a local context

g=2        # Global variable

def know_it():
    print("inside of func: ", g+2 )

know_it()  # Outputs 2
print("outside of func: ", g)