# # #collection =single "variable" used to store multiple values 
# # #list = [] ordered and changable. Duplicates OK
# # #set = {} unordered and immutab;le, but add/remove OK. NO dublicates
# # #tuple= () orderted and unchangable., Duplicates OK. FASTER 

# # fruits = ['apple' ,  'orange' , 'banana', 'coconut', 'pineapple', 'kiwi', 'strawberry' , 'papya' , 'mango' ,]
# # print (fruits[1:3])

# # # list starts with 0, 0=apple, 4=put of range 

# # print (len(fruits))
# # # #this finds length 

# # print (fruits[::2])
# # # #this gives you every second word 

# # print(fruits[::-1])
# # # #reverses order of list 

# # # for fruit in fruits:
# # #first thing with itteration
# # #DONT NAME VARIABLE ONE LETTER
# # #fruit represent object in list 
# # #itteration is looping throught the whole thing 
# # #will loop through each time 
# # #iteration 1- fruit = apple
# # #itteration 2- fruit = orange 

# # print (dir (fruits))
# # #dir-gives all atributes in a list 

# # # print(help(fruits))
# # #gives you documentation for what it does 

# # len(fruits)
# # # #gives the length of the list

# # print ("apple" in fruits )
# #  #tells you if element is in a list
# #  #boolean 
# # print ("tomato " in fruits)

# # #lists are ordered and changable, duplicates are ok 

# # fruits[0] = "pineapple"
# # #changes the value of the "0" in the list 

# # fruits [2] = "grape"

# # print(fruits)

# # for fruit in fruits:
# #     print(fruit)

# # fruits.append("pineapple")
# # # . append will add something to the end of the list 

# # fruits.remove('grape')
# # # .rempove will remove

# # fruits.insert(0, 'pineapple')
# # #will put that value in the given spot (pineapple in spot 1)

# # fruits.sort()
# # #alphabetical order

# # #fruits.reverse()
# # #reverse order from how you put them in 

# # fruits #??
# # #prints in reverse alhabetical order 

# # fruits.clear()
# # # ??

# # print (fruits.index ('apple'))
# # #finds the location/index

# # for fruit in fruits:
# #     print(fruit)



# cars = ['ford' , 'volvo' , 'BMW']

# cars.append('Honda')
# cars.append('Tesla')
# cars.append('Buick')
# cars.append('cybertruck')
# #print out as an F string 


# cars[-1] = 'austin martin' 
# print(f"The cars in the list are : {cars}")

# #replace 3rd with another car 
# cars[2] = 'suberu'
# print(f"The cars in the list are : {cars}")

# #insert a new car in the second position 
# cars.insert(1, 'Lambo')
# print(f"The cars in the list are : {cars}")

# #remove 3rd element in a list 
# cars.remove('volvo')
# print(f"The cars in the list are : {cars}")

# #check if list contains "ford" 
# ford_in_cars = "ford" in cars
# print (f'it is {ford_in_cars} that ford is in the list of cars ')


# for car in cars:
#     requestCar= input('Enter a car')
#     cars.append(requestCar)
#     print(f'The cars in the list are: {cars}')
#     if len(cars) > 10:
#         print ('you have reached max cars.')
#         break 
 
# for car in cars:
#     print(car)

# #create list of frineds 
# friends= ['Friend A']
# #add 4 new friends by asking the user to enter names 

# for friend in friends:
#      requestFriend= input('Enter a friend')
#      friends.append(requestFriend)
#      print(f'The friends in the list are: {friends}')
#      if len(friends) > 4:
#          print ('you dont need more friends.')
#          break 
    


# #print out list of names 
# print(f'The friends in the list are: {friends}')

# #replace last element with neew friend 
# friends[-1] = "Friend K"

# #print list of friends 
# print(f'The friends in the list are: {friends}')

# #replace 3rd element 
# friends[2] = 'Friend V'

# #print lis tof friend s
# print(f'The friends in the list are: {friends}')

# #add friend in last position 
# friends.insert ='Friend X'

# print(f'The friends in the list are: {friends}')

# fruits = {'apple', 'banana', 'mango', 'cherry', 'watermellon'}
# print (fruits)
# #print(dir(fruits)) #attributes that can be used in sets 
# #print(help(fruits)) #docuumentatons that can be used with sets 
# #print(len*(fruits)) #number of elements in the set 
# #print ('volvo' in fruits) # ceck if element is in a set 
# #add an element to the set 
# print(fruits.add ('orange'))
# print (fruits)
# print(fruits.add('kiwi'))
# print(fruits)
# #add multiple elkments to the se t
# print (fruits.remove ('banana'))
# print(fruits)
# print(fruits.pop())
# # removes last element in a set 
# print (fruits)
# print (fruits.clear()) #clears the set 
# print(fruits) 
# #use sets when storing a collection of items th cant be changed and you dont care about the order of the items.
# #example- a collection of uniqe items
# SS_numbers = {123456789, 987654321, 135798642}

# #revome the last element in this set 
# #print(SS_numbers.pop())

# #add another social security number 
# SS_numbers.add(918273645)
# print(SS_numbers)

##############################################################
#tuploes are i8mmutable and used with ()
# #create my_tuple wiht the following values 
# example_tuple= (1,2,3,4,5,6,7,8,9,10)
# # print(example_tuple)
# # print(example_tuple.count(2)) # counts the amount of tijmes somethibng appears 
# # # print(dir(example_tuple)) #atributes thst can be used with tuples
# # # print(help(example_tuple)) #methods that can be used with tuples
# # print(len(example_tuple)) # number of elements in tuple
# # print(2 in (example_tuple)) # check if element is in a tuple 

# # #useful when you want ot store collection of itms that can not be changed, suc as days of the week or months of the year
# # print(example_tuple.index(6)) #fidn index of a value in a tuple
# # lymeric= "peter piper picked a peck of pickled pepers"
# # #convert string into tuple
# # #split it first 
# # lymric_tuple= tuple(lymeric.split())
# # print(lymric_tuple)
# # #find how mnay times "p" appears in the lymric 
# # print (lymric_tuple.count()) #finds ow many times something appears 

# #loops with tuples 
# for item in example_tuple:
#     print(item) 

#########Dictonary#################
#dictionarys are un ordered, changable, and indexed
    #they are defined using curl brackets 
    #they have keys and values 
    #a collection of {key:value} pairs, no duplicates 
    #keys are unique
    #values can be of any data type 
capitals= {'Kenya':'Nairibi', 
'Uguanda':'Kampala',
'Tanizia':'Dodma',
'Rwanda':'Kigali',
'China':"Bejing", 
'USA': "washington DC"}

print(capitals)
# print(dir(capitals)) #atributes that can be used with dictionarys 
# print(help(capitals)) #methods that can be used with dictionarys 

print(len(capitals)) #number of items in the dictionary 
#if you want ot get the value of a key 
# print(capitals('Kenya'))
# print(capitals.get('Kenya'))
#add an item to the dictionary #2 ways 
# capitals('South Africa') == 'Pretoria'
print(capitals)
#add more countries and their capitals 
capitals.update ({'france':'Paris', 'Germany':'Berlin', 'Italy':'Milan'})
# print(capitals)
# #capitals.clear() #dont run this 
# #loop through dictionary to get the keys 
# for key in capitals: 
#     print (f"these are the {key}")

# #print the values in the dictionary 
# for value in capitals.values():
#     print(value)

#print the key value pairs in the dictionary 
items_all=capitals.items() #key value pairs 
for key, value in items_all:
        print (f"{key} is the capital of {value}")
