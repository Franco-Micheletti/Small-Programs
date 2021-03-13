"""Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb"."""


def test():
                                             # TEST FOR DEBUGGING
    print("POSIBLE: ","[",posible,"]")
    print("LONGEST: ","[",longest,"]")
    print("LETTER: ",x)
    print("UNIQUE CHARS :",unique_chars)
    print("STRING :",string,"\n")

def longsub(s,k):
                                                    # DEFINING VARIABLES
    import time                                     
    global posible,longest,unique_chars,x,string    
    string = s                                      
    solved = False                                  
    unique_chars = 0                                
    chars_number = -1                               
    longest =""                                                
    posible =""                                     
    while solved == False:                          # CONTINUE SOLVING UNTIL THE PROGRAM RETURNS A VALUE
        for x in string:                            # PICKS EVERY LETTER IN THE STRING ONE BY ONE
            chars_number+=1                         # ADD 1 TO THE COUNT OF CHARACTERS
            time.sleep(1)                           # FOR PROGRESSIVE UPDATE WHILE RESOLVING 
            test()                                  # FOR TESTING
            if x in posible:                        # IF THE LETTER IS IN THE POSIBLE SUBSTRING
                if chars_number == len(string):     # IF THE TOTAL COUNT OF CHARACTER IS EQUAL TO THE LENGTH OF THE STRING
                    if len(posible) > len(longest): 
                        return posible              # IF THE POSIBLE SUBSTRING IS LONGER THAN THE ACTUAL LONGEST SUBSTRING RETURN THE POSIBLE SUBSTRING
                    else:                           # RETURN THE LONGEST SUBSTRING OTHERWISE
                        return longest              
                else:                               # IF THERE IS MORE NON UNIQUE CHARACTER THE PROGRAM ADD IT TO THE POSIBLE SUBSTRING
                    posible+=x                      
            elif unique_chars < k:                  # IF THE LETTER IS NOT IN THE POSIBLE SUBSTRING , THAT MEANS IT IS A UNIQUE CHARACTER
                unique_chars+=1                     # SO IT CHECKS IF THE UNIQUE CHARACTERS ARE LOWER THAN " K "
                posible+=x                          # IF SO , IT ADD ONE TO UNIQUE_CHARS AND ADD THE LETTER TO THE POSIBLE SUBSTRING
            else:
                if posible in s:                    # IF THE POSIBLE SUBSTRING IS IN THE ORIGINAL STRING
                    if len(posible) > len(longest) or len(posible) == len(longest): #IF THE POSIBLE IS LONGER THAN THE LONGEST SUBSTRING OR EQUAL
                        longest = posible           # POSIBLE SUBSTRING BECAME THE LONGEST
                        posible = ""                # CLEAR THE POSIBLE SUBSTRING SO IT CAN BE GENERATED AGAIN
                        string = string[1:]         # STARTING AGAIN BUT WITHOUT THE FIRST LETTER OF THE STRING
                        unique_chars = 0            # RESET UNIQUE CHARACTERS
                        chars_number = -1           # RESET COUNTING OF CHARACTERS
                        break                       # THIS PREVENTS THE FOR LOOP TO KEEP RUNNING
                    else:
                        return longest              # IF THE POSIBLE SUBSTRING IS NOT LONGER THEN,RETURNS LONGEST

print("THE LONGEST SUBSTRING WITH 2 DISTINCT CHARACTERS IS :",longsub("abcba",2))

