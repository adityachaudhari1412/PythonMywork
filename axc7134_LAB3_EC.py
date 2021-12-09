#Aditya Chaudhari
#1001747134
#11/8/2021
#Windows 10
import os
fileName="input_RPN.txt"
#we will create a class to implement the stack

def RPN_evaluate(RPN_expression): #we will create a function to evaluate the RPN expression string
    operator = ["+","-","*","/","%"]
    stack=[] #Stack class object 
    for c in RPN_expression: #this loop will run until each character in the RPN expression is string
        if not((c >='0' and c<='9') or (c>='A' and c<='Z') or (c>='a' and c<='z')): # push to the stack if we get number instead of char
            op1=stack.pop() #we are popping the top element to assign it as operand 1
            op2=stack.pop() #popping second element (topmost element)to assign it as operand 2
            res=eval(op2+c+op1) #inbuilt-function 
            stack.append(str(res)) #we will push result in the form of string
        else:
            stack.append(c)
    return  stack.pop() if stack!=[] else 0 #returning the topmost popped element

            

if(os.path.exists(fileName)): #to check if file exists in the current path  
    f= open(fileName) #open the file
    lines=f.readlines() #lines will be stored in list after reading every line from the  file 
    for line in lines: 
        line=line.strip() #we will remove the unnecessary lines and extra characters  
        result=RPN_evaluate(line)# we will store result after computing the result of RPN string  
        print('RPN expression: '+line+' RPN result: '+str(result)) #print RPN expression string along with the result
    f.close()
else:
    print('File doesn''t exist')
