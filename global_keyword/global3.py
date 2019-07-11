'''We got UnboundLocalError: local variable 'g' referenced before assignment in global2.py
   
because we can only access the global variable from function not modify.
'''

g=2        # Global variable

def know_it():
    global g
    g=g+2
    print("Inside function: ",g)

know_it() 
print ("Outside function: ", g)