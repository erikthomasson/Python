'''


Rules:
() + () = ()()                                      => [combine]
((())) + () = ((())())                              => [absorb-right]
() + ((())) = (()(()))                              => [absorb-left]
(())(()) + () = (())(()())                          => [combined-absorb-right]
() + (())(()) = (()())(())                          => [combined-absorb-left]
(())(()) + ((())) = ((())(())(()))                  => [absorb-combined-right]
((())) + (())(()) = ((())(())(()))                  => [absorb-combined-left]
() + (()) + ((())) = (()()) + ((())) = ((()())(())) => [left-associative]

Example: 
(()) + () = () + (()) = (()())

'''
#c= "((123"
def func(a, b):
    #print(c[-2:])
    if(a == "()" and b== "()" ):
        print("1")
        return "()()"

    elif((len(a) > 2) and (b == "()")):
        print("2")
        return  a[:-1] + b + ")"  
    
    elif((a == "()") and (len(b)>2)):
        print("3")
        return "(" + a + b

    else:
        if((a[:3]=="(((" and b[-3:]==")))")or(a[:3]==b[:3] and a[-3:]==b[-3:])):
            return a + b
        elif(a[:3]!="(((" and b[:2]!="()" and a[:2]!=b[:2]):
            return "("+a+b[1:]
        elif(a[-2:]!="()" and b[-3:]!=")))" and a[-3:]!=b[-3:]):
            return a[:-1]+b+")"
        


        
 
print(func("(()()()()())(()(())(()))","(())"))
#(()()()()())(()(())) + (()) + (())

(((((()))))(((())))((()))(())()(()()()()()()()()))(((((()))))(((())))((()))(())())(()()()()()()()())(()()()(())()())(()(((()()())()())()()))((())())(()(()))()())
