data = {}


play = True
while play:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n$"))
    data[name] = f"${bid}"
    reset = input("Are there any other bids? Type yes or no?\n").lower()
    if reset == "no":
        play = False
    elif reset == "yes":
        print("\n" * 100)
    else:
        print("Wrong input. Giving to next bidder")

val = max(data, key=data.get)

print(f"The winner of the auction is {val} who bidded {data[val]}")