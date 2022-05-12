# .Using the range function for loop and if/elif/else statements,
# create a program that shows all the numbers 
# between 0 and 100 that are divisible by 5,6,7,9or all of them.
# x=range(100)
x=range(100)
for y in x:
    if y%5==0:
        print(f"{y}is divisibleby 5")
    elif y%6==0:
     print(f"{y} is divisible by 6")
    elif y%7==0:
         print(f"{y}is divisible by 7")
    elif y%9==0:
         print(f"{y}is divisible by 9") 
    else:
        print(f"{y} is not divisible by 5,6,7 or 9")
