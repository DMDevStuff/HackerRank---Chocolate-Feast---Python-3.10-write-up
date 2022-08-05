##    https://www.hackerrank.com/challenges/chocolate-feast/problem
##
##    See above link for problem description.

##### ##### ##### #####

#   changed variable names

#   n = money
#   c = cost
#   m = wrappers_needed

##### ##### ##### #####

#   O(n)
#   n is the ratio of starting money to the number of wrappers needed for a free candy

#   Idea:
#       Iterate and check with book keeping.
#       At first we buy candy, then we can keep getting free candy as long
#       as the number of candy wrappers we have is more than the number needed
#       to get free candy.  So we simply check if we have enough wrappers -
#       if we do - we trade in as many as we can for free candy, save the wrappers
#       from the free candy we have just gotten and check again.  All the while we
#       keep track of the total number of candies we have gotten.

#   Algo:
#       1. Initiate a variable to keep track of the total number of candies.
#           Set it equal to money // cost => O(1)
#       2. Initiate a variable to keep track of the current number of wrappers
#           we have.  Set it equal to total candies => O(1)
#       3. Initiate a while loop that iterates until the current number of wrappers
#           we have is less than the number of wrappers needed for a free candy => O(n)
#               A. Initiate a variable to store the number of candies recieved at this
#                   step.  Set it equal to current_wrapper_count // wrappers_needed => O(1)
#               B. Add the candies recieved at this step to the total number of
#                   candies we have => O(1)
#               C. Set the current_wrapper_count equal to:
#                   (current_wrapper_count % wrappers_needed) => O(1)
#               D. Add the candies recieved at this step to the
#                   current_wrapper_count => O(1)
#       4. Return total_candies => O(1)

def chocolateFeast(money, cost, wrappers_needed):
    
    total_candies = money // cost
    current_wrapper_count = total_candies
    
    while current_wrapper_count >= wrappers_needed:
        
        candies_acquired = current_wrapper_count // wrappers_needed
        total_candies += candies_acquired
        current_wrapper_count = current_wrapper_count % wrappers_needed
        current_wrapper_count += candies_acquired
        
    return total_candies
