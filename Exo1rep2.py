#We want to write a programe that can count uppercase and lowercase letters.

#define a function and call it user_string
def cap (user_string):
    countUpper = 0   #Start the countdown from zero
    countlower = 0    
    for e in user_string:  #for elements in my string
        if e.isupper():    # if element is uppercase
            countUpper += 1   # add 1
        elif e.islower():      # else if it is lowercase
            countlower +=1      #add 1
    return countUpper,countlower     #after return in the order number of upper and lower 



User_string = input("write your string here")
countUpper, countlower = cap(User_string)

print("Number of uppercase :", countUpper)
print("Number of lowercase :", countlower)
