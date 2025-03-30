Animal = str

def zoo(animal: Animal, number: int) -> None:
    print("The zoo has %s %s" % (number, animal))

if __name__ == '__main__':
    zoo('Zebras', 10)