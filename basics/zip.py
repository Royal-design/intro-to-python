name1 = ["Ife", "Ola", "Emmanuel", "Ola"]
name2 = ["Ade", "Ola", "Emmanuel", "Ola"]
name3 = ["Bisola", "Ola", "Emmanuel", "Ola"]

zipped = list(zip(name1, name2, name3))
print(zipped)

for a in zipped:
    print(a)