#Good cheat sheet: https://rowannicholls.github.io/python/advanced/lists.html and this is good too https://rowannicholls.github.io/python/intro/lists.html

#Extracting subset

#Extract second item in each sublist;
list = [
        ["a",65,34],
        ["min",20,54],
        ["g",54,19]
]

list2 = [i[1] for i in list]
print(list2)

#remove empty rows
list3 = [4,[],[3,6,2],5,[],[4,3]]
list3 = [_ for _ in list3 if _ != []]
print(list3)

#find index using enumerate
#find the positions of B or C
ls = ['A',"B","C","B","D","C"]
print([index for index,value in enumerate(ls) if value == "B" or value == "C"])

#find both values and indexes
ls4 = ['zero','first','second','third','fourth']
print([(i,j) for i,j in enumerate(ls4) if j != "second"])

#find index of last occurence in list 

ls = [5,3,4,5,2,1]
# print(ls.index(max(ls[-1:])))
print(len(ls) -1 - ls[::-1].index(max(ls)))

# changing strings to integers:
galaxies = [["1","345667"],["2","486846"],["3","34546"],["4","457457"],["5","4758"]]
for index in range(len(galaxies)):
    for galaxy in range(2):
        galaxies[index][galaxy] = int(galaxies[index][galaxy])

#Finding the minimum value in set index position of nested lists
#the [1] is the index position of the value you want to target
velocities = [_[1] for _ in galaxies]
print(min(velocities))
