converter = {"CSC1006":"Mathematics 2", "CSC1007":"Operating Systems","CSC1008":"Data Structures and Algorithms","CSC1009":"Object Oriented Programming","CSC1010":"Computer Networks"}#create a dictionary with the codes as the key
userin = input("Please input subject code")#get user input
print(converter.get(userin))#convert user input to subject name using dictionary
for i in range(102,65,-1):#starting from 102 until 66, decrement by 1 every iteration
    if i % 2 == 1:#if it is an odd number
        print(i)#print it