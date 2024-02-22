current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue # skip the rest of the code in this loop and continue with the next iteration of the loop.

    print(current_number)