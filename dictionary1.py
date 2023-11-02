#question 1
# dic={'x':10,
#      'y':20,
#      'z':30
# }
# for key,value in dic.items():
#     print(f"{key}={value}")

# #question 2
# num=input("enter the number:")
# squares={num:num**2 for num in range(1,num)}
# print(squares)

# #question 3
# squares={num:num**2 for num in range(1,16)}
# print(squares)

# #question 4
# sum=0
# my_dic={'data1':100,'data2':-54,'data3':247}
# for value in my_dic.values():
#    sum+=value
# print(sum)   






#question 5
# color_dict={ 'red':'#FF0000',
#             'green':'#000000',
#             'black':'#000000',
#             'white':'#FFFFFF' }
# print(sorted(color_dict.keys()))\


#question 6
num=int(input("enter the number"))
d={1:10,2:10,3:30,4:40,5:50,6:60}
if (num in d.values()):
    print("present")
else:
    print("absent")    

