def first_non_consecutive(arr): 
    for i in range(len(arr) - 1): #Using range to determine the number of times the loop will run; which is the length of the list
        if arr[i] + 1 != arr[i + 1]: #Checking the condition
            return arr[i + 1] #Returning the non-consecutive number

def missing_number(arr):
    for i in range(len(arr) - 1): #Using range to determine the number of times the loop will run; which is the length of the list
        if arr[i] + 1 != arr[i + 1]: #Checking the condition
            return (arr[i + 1] - 1) #Returning the missing number

