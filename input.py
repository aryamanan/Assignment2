def Ques1():
    input_string=input("Enter the string: ")
    #Finds the length of the input string.
    print("Part A")
    print("Length os input string",len(input_string))
    
    #Reverses the order of the string in one line code.
    print("Part B")
    print("Reverse of string is","'"+input_string[-1: :-1]+"'")
    
    #Using Slice function stores “a case sensitive” in new string
    print("Part C")
    slicestr=input_string[slice(9,26)]
    print(slicestr)
    
    #Replaces “a case sensitive” with “object oriented”
    print("Part D")
    newstring=input_string.replace("a case sensitive","object oriented")
    print(newstring)
    
    #Finds index of substring “a” in the given input string
    print("Part E")
    print("Index of substring 'a' is",input_string.index('a') )
    
    #Remove the white spaces from the given input string
    print("Part F")
    print(input_string.replace(" ",""))
    
Ques1()

def Ques2():
    #takes inputs from the user
    name=input("Please enter your name: ")
    sid=input("Enter SID: ")
    dep=input("Enter department name: ")
    cgpa=float(input("Enter CGPA: "))
    
    #puts all information in order using string formatting
    print('''
    ''')
    print('''Hey, %s Here!
             My SID is %s
             I am from %s department and my CGPA is %s'''%(name,sid,dep,cgpa))

Ques2()

def Ques3():
    #declaring values
    a=56
    b=10
    
    #performs bitwise operations
    print("Part A")
    print("a&b: ",a&b)
    print(" ")
    print("Part B")
    print("a|b: ",a|b)
    print(" ")
    print("Part C")
    print("a^b: ",a^b)
    print(" ")
    #Left shifts both a and b with 2 bits.
    print("Part D")
    print("a<<2:",a<<2,"and", "b<<2: ",  b<<2)
    print(" ")
    #Right shifts a with 2 bits and b with 4 bits.
    print("Part E")
    print("a>>2:",a>>2, "and b>>4",b>>4)

Ques3()

def Ques4():
   #finds the greatest of three numbers entered by user
    l=[]
    for i in range(3):
        num=float(input("Enter number %s: "%(i+1)))
        l.append(num)

    l.sort(reverse=True)
    print("The greatest value is:",l[0])

Ques4()

def Ques5():
    #takes user input
    inp_string=input("Enter the string: ")
    #conditional to check if “name” is present in the string
    if 'name' in inp_string:
        print("yes")

    else:
        print("no")    

Ques5()

def Ques6():
    #takes in user input value in form of array
    sides=[]
    #tests if one side isn't bigger than the addition of two other
    for i in range(3):
        side=float(input("Enter side %s: "%(i+1)))
        sides.append(side)
    
Ques6()
