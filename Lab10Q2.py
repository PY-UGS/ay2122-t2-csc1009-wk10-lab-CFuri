

res = input("please enter two numbers with a comma inbetween to get their average")#get user input
splres = res.split(",")#split the input using delimiter ,
out = (float(splres[0]) + float(splres[1]))/2#convert from string to float, add the values and divide by 2
print("average is " + str(out))#print the result