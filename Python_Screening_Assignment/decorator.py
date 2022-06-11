def calculate(func):  
    def compute(x,y):  
        if(func.__name__ == "divide"):
            print("Checking for Infinite Trap")
            if y == 0:
                print("You cannot divide with 0")
                return
        return func(x,y)  
    return compute 
 
@calculate
def divide(x,y):  
    return x/y
 
@calculate
def sum(x,y):  
    return x+y  
 
sum_result = sum(5,0)  
div_result = divide(8,0)  
print("RESULT: SUM=> ",sum_result," DIVISION=> ",div_result)
