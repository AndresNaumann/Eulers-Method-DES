dslope = 0

def euler(y, target, steps):
    
    for x in range( 0, target * steps):
        
        #print(x/steps, ", ", y)
        dslope = 0.6 * y
        y = y + (dslope/steps)

    print(x/steps + 1/steps, ", ", y)
        
euler(10, 5, 100)
        


        
    
