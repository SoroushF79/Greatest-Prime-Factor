""" Created by Soroush Famili on 4/13/18
    Function GPF finds the Greatest Prime Factor of a number
    less than or equal to the input number.
    Converts the input to an integer and outputs an integer.
    If the input is negative, the input is converted to a positive number.
    Although no one normally considers the prime factors of negative Numbers,
    I nonetheless convert a negative input into a positive one and 
    go from there. Lines for time measurement are included for convenience but are commented out.
    An input of 0 or 1 yields an output of False. I did not take into account non-numeric inputs.
"""

#import time
#t1 = time.time()
def GPF(n):
    n = int(n)
    if( (n == 0) or (n == 1)):
        return(False)
    if(n < 0):  # Check if input is negative. If so, multiply by -1.
        n = n*(-1)
    i = 2
    a = n
    while(i <= int(a*.5)):  # We only need to consider all numbers <= one half the original input
        while(( n % i) == 0):
            b = n           # Preserving the number before redefining it in terms of itself
            n = n/i

        
        i = i + 1
        if(n == 1):
            return(int(b))
 
    return(int(a))


while(True):    
    user = input("This Function finds the Greatest Prime Factor of your input number.\n Input: ")
    answer = GPF(user)
    print("The Greatest Prime Factor of %d is %d." % (int(user), answer))
    #t2 = time.time()
    #print( t2 - t1)
         