colors = ["red","green","blue"]
print(colors)
print(colors[1]) #green

fruits = ["apple","banana","orange","kiwi","mango"]
#for-each loop
for item in fruits:
	print(item)
print("")

#for loop
for index in range(len(fruits)):
	print(fruits[index])
print("")

lastfruit = fruits[len(fruits)-1]
print(lastfruit)
input()