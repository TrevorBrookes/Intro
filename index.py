import time

# print('Hello World!')


# this a comment - the code here is not run


# animalList = ['cow', 'chicken', 'zebra', 'monkey', 'whale']

# for animal in animalList:
#     print(animal)


# # make this loop only print 'Hello World' 5 times
# myBoolean = False
# counter = 0
# while myBoolean == False:
#     print('Hello World')
#     counter += 1 # this is the same as counter = counter + 1

#     if counter == 5:
#         myBoolean = True


# for i in animalList:
#     print(i)




# def print_family_names(family):
#     for name in family:
#         if name == 'Jordan':
#             print(name + ' - Favourite Son!')
#         else:
#             print(name)


# name = ['Mom', 'Dad', 'Jordan', 'Trevor', 'Dylan']
# print_family_names(name)



def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)



myValue = factorial(4)
print(myValue)