# with open("adatok.txt", "r", encoding="UTF-8") as file:
#     file.readline()

    # for i in file:
    #     szelet = i.strip().split(";")
    #     if int(szelet[-1]) > 1:
    #         print(szelet[1])

file = open("adatok.txt")
file.readline()
[print(szelet[1]) for i in file if (szelet := i.strip().split(";")) and int(szelet[-1]) > 1]
file.close()
print()

file2 = open("adatok.txt")
file2.readline()
print(len([i for i in file2 if (szelet := i.strip().split(";")) and (int(szelet[-2]) - int(szelet[-1])) != 3 ]))
file2.close()
print()

file3 = open("adatok.txt")
file3.readline()
[print(i) for i in file3 if (szelet2 := i.strip().split(";")) and szelet2[1] == "Hát Izsák"]
file2.close()
print()