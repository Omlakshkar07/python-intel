# def myfunc():
#     x=10   #x is lobal variable
#     print(x)
# myfunc()    

# x=10 #x is global variable
# def myfunc():
#     print(x)
# myfunc()     

#if u can modify the a global variable from within a function you cann use he global keyword  


#modify global
x=10 #global variable
def modify_global():
    global x    # non-local scope variable . by using global keyword
    x=20
modify_global()
print(x)


