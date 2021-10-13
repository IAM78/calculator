import math
import sys
print('welcome')

while True:

    print('1:sum(+)')
    print('2:sub(-)')
    print('3:mul(*)')
    print('4:div(/)')
    print('5:log')
    print('6:sin')
    print('7:cos')
    print('8:tan')
    print('9:cot')
    print('exit')

    print('please enter your operation : ')
    op=input()
    if op == 'exit':
            sys.exit(0)    
    a = int(input('enter your first number : '))
    
    b = int(input('enter your second number : ')) 
    if op == '+':
            result = a + b
    elif op == '-':
            result = a - b
    elif op == '*':
            result = a * b
    elif op == '/':
       if b != 0:
         result = a / b
       else:
          result = 'cannot divide by zero'  
    elif op == 'Log' :
            result=math.log10(a)
    elif op == 'Sin' :
            result=math.sin(math.radians(a))
    elif op == 'Cos' :
            result=math.cos(math.radians(a))        
    elif op == 'Tan' :
            result=math.tan(math.radians(a))
    elif op == 'Cot' :
            r=math.tan(math.radians(a))
            result=1/r           
    else:
            result = 'No command found'    
    print(result)        