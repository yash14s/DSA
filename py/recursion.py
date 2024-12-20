'''
Practice recursion
'''

def sum_n(n):
    #Find sum of first n positive integers. 

    def iterative():
        sum = 0
        for i in range(1, n+1):
            sum += i

        return sum
    
    #return iterative()

    def recursive(n):
        if n == 1:
            return 1
        
        sum = n + recursive(n-1)

        return sum
    
    return recursive(n)


print(sum_n(5))