friends = ["Gaurav", "Kritika", "Sachin", "Batra", "Taya", "Taya"]
print("List friends: " + str(friends))

friends.sort()
print("Sorted friends: " + str(friends))   # sort does not work on complex list while reverse does

numbers = [1, 2, 3, 4, 5]
print("List numbers: " + str(numbers))

friends.extend(numbers)
print("Extend numbers to friends: " + str(friends))

friends.reverse()
print("Reverse sort friends: " + str(friends))


friends.append("Me")
print("Append Me to friends: " + str(friends))

friends.insert(0, "Alok")
print("Insert Alok at the beginning of friends: " + str(friends))

friends.remove("Me")
print("Remove Me from friends: " + str(friends))

friends.pop()
print("Pop last element from friends" + str(friends))

print("Index of Taya: " + str(friends.index("Taya")))
print("Count of Taya: " + str(friends.count("Taya")))

friends2 = friends.copy()

print("Copy for friends, friends2: ", str(friends2))

friends.clear()
print("Cleared friends list: " + str(friends))

