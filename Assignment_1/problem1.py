"""
Given an array a of n numbers and a target value t, find two numbers whose sum is t.

Example: a=[5, 3, 6, 8, 2, 4, 7], t=10 ⇒ [3, 7] or [6, 4] or [8, 2]
"""

def brute_force(a, t):
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if (a[i] + a[j] == t):
                return (a[i], a[j])
    
def hash_it(a, t):
    return("hi")

if __name__ == "__main__":
    print("solution 1: ", brute_force([5, 3, 6, 8, 2, 4, 7], 10))
    print("solution 2: ", hash_it([5, 3, 6, 8, 2, 4, 7], 10))