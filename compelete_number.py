def is_complete(n:int) -> bool :
    """
    Returns whether an int is complete or not
    
    Args:
        n(int) : An int number to see if it's complete or not
        
    Returns:
        bool : whether is complete or not
    """
    
    divisors = []
    
    for i in range(1,(n//2)+1):
        if n % i == 0:
            divisors.append(i)
            
    if sum(divisors) == n:
        return True
    else:
        return False
    

print(is_complete(int(input())))