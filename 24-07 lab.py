#Aldığınız kursun adına göre IT alanında meslek sahibi olup olamayacağınızı
# ekrana yazdıran bir kod yazınız.
# course = “clarusway”
# if course == “clarusway”:
#     print(“You got it!“)
# else:
#     print(“Think about it!“)
# Alınan ağırlık değerine göre ağırlığı kaldırıp
# kaldıramayacağınızı ekrana yazdıran bir kod yazınız.
# weight = int(input(“Agirlik giriniz: “))
# if weight > 100:
#     print(“Cok zor kaldiramazsiniz”)
# elif weight > 75:
#     print(“Zorlanabilirsiniz”)
# else:
#     print(“Kolayca yaparsiniz”)
# Girilen sayının pozitif, negatif, ya da 0 olduğunu bulan kodu yazınız
# num = int(input(“Enter a number: “))
# if num < 0:
#     print(“it is negative”)
# elif num > 0:
#     print(“it is positive”)
# else:
#     print(“this is zero”)
# Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayan python
# uygulamasını yapınız.
# Formül: (Kilo / boy uzunluğunun karesi)
# Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
# 0-18.4 => Zayıf
# 18.5-24.9 => Normal
# 25.0-29.9 => Fazla Kilolu
# 30.0-34.9 => Şişman (Obez)Kişinin ad, kilo ve boy bilgilerini alıp
# kilo indekslerini hesaplayan python uygulam
# name = input(“adinizi giriniz: “)
# kilo = float(input(“kilo giriniz: “))
# boy = float(input(“bouynuzu giriniz: “))
# index = kilo / boy**2
# if index >= 0 and index <= 18.4:
#     print(“zayif”)
# elif index >= 18.5 and index <= 24.9:
#     print(“normal”)
# elif index >= 25 and index <= 29.9:
#     print(“fazla kilolu”)
# elif index >= 30 and index <= 34.9:
#     print(“Sisman”)
# else:
#     print(“tekrar kontrol ediniz”)
# Meyvelerden oluşan bir liste oluştur ve for kullanarak ekrana yazdır:
# L = [“elma”, “armut”, “karpuz”]
# for i in L:
#     print(i)
#  0 ile 10 arasındaki sayıları ve karelerini for kullanarak ekrana yazdır.
# for i in range(11):
#     print(i, i**2)
# 1 ile 10 arasında sayıları for kullanarak ekrana yazdır 5 i görünce döngüden çık.
# for i in range (1, 11):
#     if i != 5:
#         print(i)
#     else:
#         continue
# 0 dan 10 a kadar olan tek sayıları for döngüsü kullanarak ekrana yazdır.
# for i in range(11):
#     if(i % 2 == 0):
#         continue
#     print(i)
# While döngüsü kullanarak sonsuz döngü örneği yazınız.
# flag = True
# while True:
#     print(“sonsuz”)
# Girilen sayının faktoriyelini alan kodu for döngüsü kullanarak yazınız.
# num = int(input(” sayi giriniz: “))
# result = 1
# for i in range(1, num+1):
#     result *= i
# print(“Sonuc: “, result)
# for döngüsü kullanarak 1 den 10 a kadar çarpım tablosu oluşturunuz.
# for i in range(1, 11):
#     for k in range(1, 11):
#         print(i, “x” , k, “=”, i*k)
# for döngüsü kullanarak bir sözlüğün elemanlarını ekrana yazdırınız.
# sozluk = {“bir”:1,“iki”:2,“üç“:3,“dört”:4}
# for my_key, my_val in sozluk.items():
#     print(my_key, “:”, my_val)
# Aşağıda verilen listenin tüm elemanlarını while
# döngüsü kullanarak ekrana yazdırınız
# L = [“elma”,“armut”,“karpuz”]
# o = 0
# while o < len(L):
#     print(L[o])
#     o += 1
# 1'den 10' a kadar olan sayıları while kullanarak ekrana yazdırınız.
# i = 1
# k = 11
# while i < k:
#     print(i, end = ” “)
#     i +=1
# Write a Python code that counts how many vowels and
# constants a string has that a user entered
# word = input(“enter a word: “).lower()
# vo=0
# co=0
# for i in  range(len(word)):
#     if word[i] in set(‘aeiou’):
#         vo += 1
#     elif word[i] == ” “:
#         continue
#     else:
#         co += 1
# print(f”vowel count: {vo} and constant count: {co}“)
# def add(a, b):
#     return(a +b)
# add(5, 6)
# def myFun(arg1, arg2, arg3 = “abc”):
#     print(“arg1:“, arg1)
#     print(“arg2:“, arg2)
#     print(“arg3:“, arg3)
# # Now we can use *args or **kwargs to
# # pass arguments to this function :
# args = [“Geeks”, “for”, “Geeks”]
# myFun(*args)
# kwargs = {“arg1" : “Geeks”, “arg2" : “for”, “arg3" : “Geeks”}
# myFun(**kwargs)
# def myFun(*args,**kwargs):
#     print(“args: “, args)
#     print(“kwargs: “, kwargs)
# myFun(‘cla’, ‘rus’, ‘way’, a = “bir”, b = “iki”)
# Define a function with ‘arbitrary numbers of arguments’ method named
# as ‘spec_opr(*numbers)’ . This function sums all of the arguments after
# a process. This process is even numbers should be divided by 2 and odd
#  numbers should be multiplied with 3 first and then added to the total sum.
# def spec_opr(*numbers):
#     total = 0
#     for i in numbers:
#         if i % 2 == 0:
#             total += i / 2
#         else:
#             total += i * 3
#     return int(total)
# print(spec_opr(2, 3, 4, 9))
# Write a Python program to sort a list of tuples using Lambda.
# subject_marks = [(‘English’, 88), (‘Science’, 90), (‘Maths’, 57), (‘Social sciences’, 85)]
# subject_marks.sort(key = lambda x: x[1], reverse = True)
# print(subject_marks)
# Write a Python program to filter a list of integers using Lambda.
# nums = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 9, 10]
# evens = tuple(filter(lambda x: x % 2 == 0, range(1,11)))
# odds = set(filter(lambda x: x % 2 != 0, nums))
# print(evens)
# print(odds)
# Write a Python function that takes a list and returns a
# new list with unique elements of the first list.
def uni(my_list):
    a = []
    for i in my_list:
        if i not in a:
            a.append(i)
    return a
print(uni([1,2,3,4,4,4,5,6,7,8,9,8,8,10])