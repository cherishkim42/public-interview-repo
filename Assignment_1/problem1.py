'''
Given an array "input_array" of n numbers and a target value "target_value", find two numbers whose sum equals "target_value".

Example: a=[5, 3, 6, 8, 2, 4, 7], t=10 ⇒ [3, 7] or [6, 4] or [8, 2]
'''

from hashtable import HashTable


def brute_force(input_array, target_value):
    """
    Manually check ALL PAIRS in the input array and see if they add up to the number. Returns matching numbers, or "None" if no matching numbers are found in the input array.
    Time complexity: O(n^2) -- [worst case]
    Space complexity: O(1) -- [we don't make any auxiliary data structures]
    """ 
    for i in range(len(input_array)):
        for j in range(i+1, len(input_array)): #i+1 b/c values @ prior indices were already checked
            if (input_array[i] + input_array[j] == target_value):
                return (input_array[i], input_array[j])
    
def hash_it(input_array, target_value):
    """
    Make a hash table contain all elements in the array. Check, for ea. element input_array[i], whether there's an element input_array[j] where input_array[j] = target_value - input_array[i].
    Time complexity: O(n)
    Space complexity: O(n)
    """
    return("hi")

if __name__ == "__main__":
    print("solution 1: ", brute_force([5, 3, 6, 8, 2, 4, 7], 10))
    print("solution 2: ", hash_it([5, 3, 6, 8, 2, 4, 7], 10))