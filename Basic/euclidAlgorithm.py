

#Euclid Algorithm

def gcd(a, b):
    #Base case
    if a == 0:
        return b
 
    return gcd(b % a, a)

def gcdExtended(a, b):
 
    # Base case
    if a == 0:
        return b, 0, 1
 
    gcd, x1, y1 = gcdExtended(b % a, a)
 
    # Update x and y using results of recursive
    x = y1 - (b//a) * x1
    y = x1
 
    return gcd, x, y


# Driver code
if __name__ == "__main__":
    print("GCD Basic")
    a = 10
    b = 15
    print("gcd(", a, ",", b, ") = ", gcd(a, b))
    
    a = 35
    b = 10
    print("gcd(", a, ",", b, ") = ", gcd(a, b))
    
    a = 31
    b = 2
    print("gcd(", a, ",", b, ") = ", gcd(a, b))
    
    print("GCD Extended")
    a, b = 35, 15
    g, x, y = gcdExtended(a, b)
    print("gcd(", a, ",", b, ") = ", g)
    print(x,y)
    
    a, b = 31, 2
    g, x, y = gcdExtended(a, b)
    print("gcd(", a, ",", b, ") = ", g)
    print(x,y)