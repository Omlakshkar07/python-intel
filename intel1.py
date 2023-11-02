# a="noneeeee"
# print(len(a))
# age=45
# if age>=18:
#     print("you are eligible to vote")
# else:
#     print("you are not eligible to vote")

# score=56
# if score>=75:
#     print("A")
# elif score>=65:
#     print("B")
# elif score>=50:
#     print("C")
# elif score>=30:
#     print("pass")
# else:
#     print("fail")



# is_raining=True
# is_cold=False
# if is_raining:
#     print("bring umberalla")
#     if is_cold:
#         print("bring jacket")
                
# my_set={1,2,3}
# my_set.update({4,5})
# print(my_set)
# x=my_set.union({4,5,6})
# print(x)

# print(my_set)
# my_set.add(4)
# print(my_set)
# my_set.remove(1)
# print(my_set)
# my_set.discard(2)
# print(my_set)
# discard doesn't error while remove gives error if given value is not present in set. 




def find_intersection(set1,set2):
#here we used def function to define the function named find_intersection. we can also define function with any name just we studied in js.   
    intersection=set1.intersection(set2)
    return intersection
set1={"a","b","c"}
set2={"a","e","f"}
intersection=find_intersection(set1,set2)
print(intersection)



    


