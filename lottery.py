from random import choice

loterry_digits = (4, 8, 15, 16, 23, 42, 58, 98, 10, 'A', 'C', 'D', 'E', 'F', 'G', 'H')

selected = [choice(loterry_digits) for _ in range(4)]

print(f"Lottery numbers: {selected[0]}, {selected[1]}, {selected[2]}, {selected[3]}")

my_ticket = [4, 8, 15, 16]

# This block of code will run the lottery simulation as many times as it
# takes for me to win. It will print out how many times it took for me to
# win. This is a simple way to simulate how many times I would need to
# play the lottery in order to win.

while True:
    times = 1
    if my_ticket == selected:
        print("You won after " + str(times) + " times!")
        break
    else:
        times += 1