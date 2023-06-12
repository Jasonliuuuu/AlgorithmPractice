def countdown(i):
  
    # Base case
    print(i)
    if i <= 1: # End recursion when i is less than or equal to 1
        return
  
    # Recursive case
    else:
        countdown(i-1) # Otherwise call countdown with i-1

countdown(5)
