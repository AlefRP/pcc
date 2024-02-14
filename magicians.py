# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     # print(magician)
#     print(f"{magician.title()}, that was a great trick!\n")
# print(f"I can't wait to see your next trick, {magician.title()}.\n") # Runs once out of the loop

# print("Thank you, everyone. That was a great magic show!")

# for magician in magicians:
# print(magician) # indentation error - for unecessary indentation

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    # print(magician)
    print(f"{magician.title()}, that was a great trick!\n")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

    print("Thank you, everyone. That was a great magic show!") # Logic error, this will be printed once for each iteration

# Syntax error ':' missing
# for magician in magicians
#     print(magician)