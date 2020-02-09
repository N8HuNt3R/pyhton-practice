# user input
# input function
# name=input('type ur name')
# print('fuck u ' + name)
# age = input(" tor boyos lek ")
# print("sali kochi mal " + age + " perfect ")

# int_function
# num1 = int(input('enter ur number '))
# num2 = int(input('enter ur 2nd number '))
# total = num1 + num2
# print("total " + str(total))

# var_diclearation
# name, age = "nur", "44"
# print("hello " + name + " you are a buira ! look at your age " + age + " oh shit ! are you seriuos ? is it " + age)

# two input in same line
# name, age = input('type ur name and age ').split(",")
# print('ur name is ' + name)
# print( 'ur age is ' + age)

# istring formating
# python2
# name = 'nur'
# age = 22
# print("hello " + name + " your age is " + str(age))
# #python 3
# print('hello {} your age is {} '.format(name,age))
# #3.6 best
# print(f"hello {name} your age is {age}")
# #can do oparetion
# print(f"hello {name} your age is {age+3}")

# int get operation#
# num1 = input('type your fucking number :')
# num2 = input('type 2nd fucking number :')
# num3 = input('type 3rd fucking number :')
# #(int(num1) + int(num2) + int(num3)) / 3

# int get in same line
# num1, num2, num3 = input("enter your three fucking numbers using comma: ").split(",")
# print(f"here is your fucking avarage of them {(int(num1) + int(num2) + int(num3)) / 3}")

# string indexing
# my_name = "ilovepython"
# print(my_name[-2])
# print(my_name[2])

# name = input("enter your name : ")
# temp_var = ""
# i = 0
# while i < len(name):
#     if name[i] not in temp_var:
#         temp_var += name[i]
#         print(f"{name[i]} : {name.count(name[i])}")
#     i += 1


# name = input("enter your fucking name : ")

# temp = ""
# i = 0
# while i < len(name):
#     if name[i] not in temp:
#         temp += name[i]
#         print(f"{(name[i])} : {name.count(name[i])}")
#     i += 1

# #function
# def two_num(num1, num2):
#     return num1 + num2
# n = int(input("number 1 :"))
# m = int(input("number 2 :"))
# total = two_num(n,m)
# print(total)

# def odd_even(num):
#     if num%2 == 0:
#         return "even"
#     return "odd"
# print(odd_even(11))

# def is_even(num):
#     return num%2 == 0
# print(is_even(10))

# def greater(x,y):
#     if x<y:
#         return y
#     else:
#         return x
# num1 = int(input("enter your 1st number :"))
# num2 = int(input("enter your 2nd number :"))
# big = greater(num1,num2)
# print(f"{big} is the greater number :")

# def greater(x,y,z):
#     if x>y and x>z:
#         return x
#     elif y>x and y>z:
#         return y
#     else:
#         return z
# num1 = int(input("number 1 "))
# num2 = int(input("number 2 "))
# num3 = int(input("number 3 "))
# bigger = greater(num1,num2,num3)
# print(f"{bigger} is your greater value ")

# #revers function
# def is_palindrom(word):
#     reversed_word = word[::-1]
#     if word == reversed_word:
#         return True
#     else:
#         return False
# print(is_palindrom("madam"))
# print(is_palindrom("nur"))

# #shortcut
# def is_palindrom(word):
#     if word == word[::-1]:
#         return True
#     return False
# print(is_palindrom("madam"))
# print(is_palindrom("nur"))

# supper shortcut
# def is_palindrom(word):
#     return word == word[::-1]
# print(is_palindrom("madam"))
# print(is_palindrom("nur"))

# # #fibonacciseq
# def fibonachi_sec(n):
#     a = 0
#     b = 1
#     if n == 1 :
#         print(a)
#     elif n == 2:
#         print(a, b)
#     else:
#         print(a,b, end = " ")
#         for n in range(n-2):
#             c = a + b
#             a = b
#             b = c
#             print(b , end = " ")
# fibonachi_sec(20)

# #list
# number = [1,2,3,]
# print(number[2])
# word = ["nur","shuvo"]
# mixd = [2,5,"adaf","nur",]
# print(word,mixd)

# mylist = ['fruit', 'brad']
# mylist.append("noodle")
# print(mylist)

# mylist = []
# mylist.append("fuck")
# mylist.append('you')
# print(mylist)

# #insert method
# mylist = ["orrange", "mango"]
# mylist.insert(0, "juice")
# print(mylist)

# # list exr
# def squar_list(l):
#     squar = []
#     for i in l:
#         squar.append(i**4)
#     return squar
# num = list(range(1,10))
# print(squar_list(num))

# #reverse_method
# def reversing_list(l):
#     l.reverse()
#     return l
# num = [1,2,3,4,5,6,7,8]
# print(reversing_list(num))

# def reverse_list(l):
#     return l [::-1]
# num = (1,2,3,4,4)
# print(reverse_list(num))

# def reverse_list(l):
#     rev_list = []
#     for i in range(len(l)):
#         popped_itm = l.pop()
#         rev_list.append(popped_itm)
#     return rev_list
# num = [1,2,3,4,5,6,7,8]
# print(reverse_list(num))

# #importent list fuc
# def reverse_elements(l):
#     elements = []
#     for i in l:
#         elements.append(i[::-1])
#     return elements
# words = ('abcd', "yjkl")
# print(reverse_elements(words))

# def filter_odd_even(l):
#     odd_num = []
#     even_num = []
#     for i in l:
#         if i % 2 == 0:
#             even_num.append(i)
#         else:
#             odd_num.append(i)
#     output = [odd_num, even_num]
#     return output
# nums = [1,2,3,4,5,6,7,8,9,10]
# print(filter_odd_even(nums))

# common finder
# def common_nums(l1, l2):
#     output = []
#     for i in l1:
#         if i in l2:
#             output.append(i)
#     return output
# print(common_nums([1,2,3,3,4,5,], [5,6,75,3,]))

# def common_finder(l1, l2):
#     output = []
#     for i in l1:
#         if i in l2:
#             output.append(i)
#     return output
# print(common_finder([1,2,3,4,5,6,7,], [2,5,7,434,55,5,]))

# #practice
# def sublist_counter(l):
#     count = 0
#     for i in l:
#         if type(i) == list:
#             count += 1
#     return count
# mixed = [1,2,3,4, [2,3,4,4], [2,3,4,5,5], [3,3,4,5]]
# print(sublist_counter(mixed))

# dictionary

# user = {"name" : " nur shuvo" , "age" : 24}
# print(user)

# user1 = dict(name = "nur shuvo", age = 21)
# print(user1['age'])

# user_info = {
#     'name' : "nur shuvo",
#     'age' : 21 ,
#     'fav_song' : ['see you again' ' , ' 'we dont talk anymore'],
# }
# print(user_info['fav_song'])

# user_info2 = {}
# user_info2['name'] = 'nur shuvo'
# user_info2['age'] = 21
# print('your name is : ' + (user_info2['name']))
# print('and your age is : ' + str(user_info2['age']) + " years old")

# fromkeys
# d = dict.fromkeys(['name', 'age'], 'unknown')
# print(d)

# get_method
# d = {'name' : 'nur', 'age' : 'unknown'}
# print(d.get('name'))
# print(d.get('age'))
# if d.get('name'):
#     print('present')
# else:
#     print('not present')

# # ex
# def cube_finder(n):
#     cube = {}
#     for i in range(1,n+1):
#         cube[i] = i**2
#     return cube
# print(cube_finder(5))

# # word_counter
# def word_counter(string):
#     count = {}
#     for char in string:
#         count[char] = string.count(char)
#     return count
# print(word_counter("madafacka"))

# # ex
# user = {}
# name = input("enter your name : ")
# age = input("enter yor age : ")
# fav_movie = input("enter your fav_movies : ").split(',')
# fav_song = input("enter your fav_songs : ").split(',')
# user['name'] = name
# user['age'] = age
# user['fav_movie'] = fav_movie
# user['fav_song'] = fav_song
# for key, value in user.items():
#     print(f"{key} : {value}")

# # set
# s = {'a', 'b', 'c'}
# if 'a' in s:
#     print('pressent')
# else:
#     print('not present')
# for item in s:
#      print(item)

# s1 = {1,2,3,4}
# s2 = {2,3,4,5,6,7,8,8}
# union = s1 | s2
# # same
# print(s1 | s2)
# print(union)
# intersection = s1 & s2
# print(intersection)
# # same
# print(s1 & s2 )

# list comprehension shortcut way to write code

# list = []
# for i in range(1,11):
#     list.append(i**2)
# print(list)

# # shortcut

# list2 = [i**2 for i in range(1,11)]
# print(list2)

# # ex

# negative = []
# for i in range(11,11):
#     negative.append(-i)
#     print(negative)
# # same
# negative2 = [-i for i in range(1,11)]
# print(negative2)

# exmpl

# names = ['shahajat', 'nurani', 'shuvo']
# list = []
# for name in names:
#     list.append(name[3])
# print(list)

# # same
# names2 = ['shahajat', 'nurani', 'shuvo']
# list2 = [name[3] for name in names]
# print(list2)

# #exrcs

# def revers_str(l):
#     newlist = []
#     for name in l:
#         newlist.append(name[::-1])
#         return newlist
# print(revers_str(['ndgfgfehefliehfgfnfewhfg']))

# # same
# # shortcut

# def rever_strings(l):
#     return[name[::-1] for name in l]
# print(rever_strings(['qwe', 'vbei']))

# list_comprehension_exercise
# def num_to_sring(l):
#     return [str(i) for i in l if (type(i) == int or type(i) == float)]
# print(num_to_sring([True, False, [1,2,3], 2,3,34,4,5,5]))

# mixed = [i**2 if (i%2==0) else -i for i in range(11,23)]
# print(mixed)

# newlist = []
# for i in range(4):
#     newlist.append([1,2,3,4])
# print(newlist)

# # shortcode
# new_list = [[i for i in  range(1,5)] for j in range(4)]
# print(new_list)

# dictionary comprehension

# num_squars = {f"squars of {num}":num**2 for num in range(1,11)}
# for k,v in num_squars.items():
#     print(f"{k} : {v}")
# name = "shahajat nurani shuvo"
# word_counter = {f"alphabet of  name {char}":name.count(char) for char in name}
# for k,v in word_counter.items():
#     print(f"{k} : {v}")


# mixed = [i**2 if (i%2==0) else -i for i in range(11,23)]
# print(mixed)

    # num_squars = {f"squars of {num}":num**2 for num in range(1,11)}
    # for k,v in num_squars.items():
    #     print(f"{k} : {v}")
# def word_counter():
#     name = "LI CHAO"
#     word_counter = {f"alphabet of  name {char}":name.count(char) for char in name}
#     for k,v in word_counter.items():
#         print(f"{k} : {v}")


# # arg into py
# def all_total(*args):
#     print(args)
#     print(type(args))
# all_total(1,2,3,4,5,6,7,8)

# exmpl
# def all_total(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
# print(all_total(1,2,3,4,5,6,7))

# lambda function

# add = lambda a,b : a+b
# print(add(3,3))

# def is_even(a):
#     return a % 2 == 0
# print(is_even(7))

# is_even2 = lambda a : a % 2 == 0
# print(is_even2(8))

# last_char = lambda a: a [-1]
# print(last_char("shuvo"))

# def func(s):
#     return len(s) > 6
# func = lambda s: True if len(s) > 6 else False
# print(func("ugf"))

# enumerate function

# names = ['abc', 'abcde', 'shuvo']
#  pos = 0
#  for name in names:
#      print(f"{pos} -----> {name}")
#      pos += 1

# for pos, name in enumerate(names):
#     print(f"{pos} --------> {name}")

# names = ['abc', 'abcde', 'shuvo']
# def find_pos(l, target):
#     for pos, name in enumerate(l):
#         if name== target:
#             return pos
#     return -1
# print(find_pos(names, 'abcnk'))

# map function

# numbers = [1,2,3,4,5,6]

# def square(a):
#     return a**2

# print(map(square, numbers))

# square = list(map(lambda a:a**2, numbers))
# print(square)

# # list com

# square_new = [i**2 for i in numbers]
# print(square_new)

# new_list2 = []
# for num in numbers:
#     new_list2.append(square(num))
# print(new_list2)

# filter function

# def is_even(a):
#     return a%2 == 0

# numbers = [1,2,3,4,5,6,7,8,9,10]
# evens = tuple(filter(lambda a: a%2 == 0, numbers))
# print(evens)

# numbers = [1,2,3,4,5,6,7,8,9,10]
# evens = [i for i in numbers if i%2 == 0]
# print(evens)

# iterator vs iterable

# zip function

# user_id = ['user1', 'user2', 'user3']
# names = ['shahajat', 'nurani', 'shuvo']
# print(zip(user_id, names))

# any all function
#
# def my_sum(*args):
#     if all([(type(arg) == int or type(arg) == float) for arg in args]):
#         total = 0
#         for num in args:
#             total += num
#         return total
# print(my_sum(1,2,3,4,5))
# print(my_sum(1,2,3,4,5,6,7,8,9,'nur',['shuvo']))

# Decorators

# from functools import wraps
# import time

# def calculate_time(function):
#     @wraps(function)
#     def wrapper(*args, **kwargs):
#         print(f"executing .... {function.__name__}")
#         t1 = time.time()
#         returned_value = function(*args, **kwargs)
#         t2 = time.time()
#         total_time = t2 - t1
#         print(f"this function took {total_time} seconds")
#         return returned_value
#     return wrapper

# @calculate_time
# def squar_finder(n):
#     return [i**2 for i in range(1,n+1)]

# squar_finder(1000)

# genaretor

# def even_genarator(n):
#     for num in range(1,1+n):
#         if num % 2 ==0:
#             yield(num)

# for num in even_genarator(10):
#     print(num)

# gen_comprihension

# square = (i**2 for i in range(1,11))
# print(next(square))

# generator vs list

# import time
# t1 = time.time()
# l = [i**2 for i in range(1000000)]


# print(f"for list, {time.time() -t1}")


# t1=time.time()
# g = (i**2 for i in range(1000000))

# print(f"for generator, {time.time()-t1}")


# oop started from here## variables

# class Person:
#     count_object = 0

#     def __init__(self, name, age):
#         Person.count_object +=1
#         self.name= name
#         self.age= age

# p1= Person("NurShuvo", 22)
# p2= Person("shahajat", 22)

# print(p1.__dict__)

# class variable ex

# class Person:
#     count_object = 0

#     def __init__(self, name, age):
#         Person.count_object +=1
#         self.name= name
#         self.age= age

# p1= Person("NurShuvo", 22)
# p2= Person("shahajat", 22)

# print(Person.count_object)

# class Employe():
#     def __init__(self, name, age, salery):
#         self.name= name
#         self.age= age
#         self.salery= salery
# employe_1= Employe("Nur Shuvo", 22, 30000 )
# print(employe_1.__dict__)


# name = input("enter your name : ")
# user1 = "nur"
# user2 = "shuvo"
# user3 = "nurani"
# x=name

# while True:

#     if name == user1:
#         print(f"{x} is a programmer " )
#         break
#     else :
#         if name == user2:
#             print(f"{x} is a programmer ")
#             break
#         if name == user3:
#             print(f"{x} is a programmer ")
#             break
#         else:
#             print(f"he is not {x}")
#             break

# print(Person.count_object)

# class Employe:
#     increment = 2
#     def __init__(self, name, age, salery):
#         self.name= name
#         self.age= age
#         self.salery= salery
#         self.increment = 3
#     def increase(self):
#         self.salery = int(self.salery * employe_2.increment)
# employe_1= Employe("Nur Shuvo", 22, 3000)
# employe_2 = Employe("Jack", 24 , 3000)

# print(employe_1.salery)
# print(employe_2.salery)
# employe_1.increase()
# employe_2.increase()
# #print(employe_1.salery)
# print(employe_2.salery)


# from functools import wraps
# import time

# def calculate_time(function):
#     @wraps(function)
#     def wrapper(*args, **kwargs):
#         # print(f"executing .... {function.__name__}")
#         t1 = time.time()
#         returned_value = function(*args, **kwargs)
#         t2 = time.time()
#         total_time = t2 - t1
#         print(f"this function took {total_time} seconds")
#         return returned_value
#     return wrapper

# @calculate_time
# def squar_finder(n):
#     return [i**2 for i in range(1,n+1)]
# squar_finder(100)

# class Animal:
#     def __init__(self,name,sound,accommondation):
#         self.name = name
#         self.sound = sound
#         self.accommondation = accommondation

# animal_1 = Animal("Dog", "Gew Gew", "Dry place like road side, under stair" )
# animal_2 = Animal("cat", "Mew Mew", "dry place like people live , and cats are the most favorite domistice animal to peoples")

# print(animal_2.__dict__)
# print(animal_1.__dict__)







