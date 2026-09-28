import random

coins = random.choice(["Heads", "Tails"])
print(coins)


try:
    print(random.choice([]))
except IndexError:
    print("No input in list")


# randint is inclusive on both ends, 1 and 10.
numbers = random.randint(1, 10)
print(numbers)


# cards = random.shuffle(["King", "Queen", "Jack"]) overwrites the list with a None
cards = ["King", "Queen", "Jack"]
random.shuffle(cards)
for card in cards:
    print(card)


number = random.randrange(10)
print(number)


# this program shows the properties of randint and randrange functions. in randint(a, b), both a and b are inclusive. but in randrange(a, b), only a is inclusive.
randrange_results = []
randint_results = []

for _ in range(1000):
    randrange_results.append(random.randrange(10))
    randint_results.append(random.randint(1, 10))

print(10 in randrange_results)
print(10 in randint_results)
print(min(randrange_results), max(randrange_results))
print(min(randint_results), max(randint_results))
