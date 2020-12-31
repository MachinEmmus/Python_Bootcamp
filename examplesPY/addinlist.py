#!/usr/bin/python3

mylist = ["Emmus", "Jose", "Diego", "David"]
print(mylist)
mylist.insert(1, "Pai")
print(mylist)
mylist.extend(["Adrian", "Erick", "Tobon"])
print(mylist)
print(mylist.index('Pai'))
mylist.remove("David")
print(mylist)
mylist.pop()
print(mylist)
mylist.append("Emmus")
print(mylist.count("Emmus"))
