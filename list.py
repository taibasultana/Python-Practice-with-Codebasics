#Calculate how many members are in the Avengers team?

# avengers  = ["Iron Man", "Captain America", "Black Widow", "Hulk", "Thor", "Hawkeye"]
# print (len(avengers))

#iron Man made Spider-Man a new member of the Avengers, add him to your list.

# avengers  = ["Iron Man", "Captain America", "Black Widow", "Hulk", "Thor", "Hawkeye"]
# avengers.insert(1,"Spider Man")
# print(avengers)

#Captain America is the leader of the Avengers,
# you need to add him before Iron Man, so remove him from the list and add him before Iron Man.

# avengers  = ["Iron Man", "Captain America", "Black Widow", "Hulk", "Thor", "Hawkeye"]
# avengers.remove("Captain America")
# print(avengers)
# avengers.insert(0,"Captain America")
# print(avengers)

#You don’t like Thor and Hulk together because they get angry easily and fight with each other.
#So you have to separate them from each other. To separate them, either move “Black Widow” or “Hawkeye” in between them.

# avengers  = ["Iron Man", "Captain America", "Black Widow", "Hulk", "Thor", "Hawkeye"]
# avengers.sort()
# print(avengers)

#After Avengers: End Game the original six avengers are retired,
# now you need to remove them from your list and add new superheroes like Doctor Strange, Vision, Wanda, Kate Bishop, and Ant-Man.

avengers  = ["Iron Man", "Captain America", "Black Widow", "Hulk", "Thor", "Hawkeye"]
avengers.remove("Iron Man")
avengers.remove("Captain America")
avengers.remove("Black Widow")
avengers.remove( "Hulk")
avengers.remove("Thor")
avengers.remove("Hawkeye")
print(avengers)
avengers.insert(0,"Doctor Strange")
avengers.insert(1,"Vision")
avengers.insert(2,"Wanda")
avengers.insert(3,"Kate Bishop")
avengers.insert(4,"Ant-Man")
print(avengers)



#As “Captain America” is also retired and now currently, no one is the leader,
#so sort the list in alphabetical order. Whoever will come at the 0th index will become the Leader.

avengers.sort()
print(avengers)