list1 = ["Harry", "Devraj", "Sourav", "Rishi"]
print(list1[0], list1[1], list1[3])

for items in list1:
    print(items)

list2 = [["Devraj", 22], ["Sourav", 27], ["Rishi", 75]]
for item, number in list2:
    print(item, number)

list3 = [["Devraj", 22], ["Sourav", 27], ["Rishi", 75]]
for item1, number1 in list3:
    print(item1, "and his number is\n", number1)

print("")

print("..............Exercise.............")

username = ["harry", "Devraj", 33, 9, 52, 2, 35, 10, "Suman"]

for names in username:
    if str(username).isnumeric() and names>10:
        print("yo", names)
    else:
        print("vag bsdk")
