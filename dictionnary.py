# dic={}
# student={
#     "Name":"Om",
#     "age":"18",
#     "course":"Btech"
# }
# # print(student)
# # Name=student["Name"]
# # age=student["age"]
# student["age"]=21 
# for key,value in student.items():
#     print(f"{key}:{value}")

# num=0
# squares={num:num**2 for num in range(1,6)}
# print(squares)

# cubes={num:num**3 for num in range(1,6)}
# print(cubes)


# #student={
#      "Name":"Om",
#      "age":"18",
#      "course":"Btech"
# }
# # del student["age"]
# # print(student)

# # student["passing year"]=2027
# # print(student)
# #


dic={
    0:10,
    1:20
}
dic[2]=30
print(dic)

#question=2
dic1={
    1:10,
    2:20,

}
dic2={
    3:30,
    4:40
}

dic3={
    5:50,
    6:60,
}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)



