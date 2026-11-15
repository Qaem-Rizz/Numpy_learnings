"""we can also use operations between two arrays without using numpy, but on large datasets it bevcomes slow"""


list1= [1,2,3]

list2 = [4,5,6]


result =[ x + y for x,y in zip(list1, list2)] #using list comprehension

print(result)