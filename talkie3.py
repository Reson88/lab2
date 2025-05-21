#input lab 2 thing
#ask user for their mame
#then say hi, name
#back where name is the users name


#lab2: ask user for string info & say something back with that info
#ask user for numerical info
#say something back
#optional: describe whats happening



user_name = input("What is your name? ") #ask1
num_programs = input("How many programs have you contributed to this year? ") #ask2

prgm_amt = int(num_programs)

try:
    num_programs = int(num_programs) #convert to integer for math & things
    if num_programs < 10:
        print(f"Wow {user_name}, you need to get those numbers up!") #be condescending
    if num_programs > 10:
        print("Good stuff, keep it up!")
        print("wow that's approx " + str(prgm_amt / 12) + " per month!")

except ValueError:
    print("not a number :(")


#was going to add a timeout delay of 15 seconds. Couldnt get the time command to fit in time (no pun intended)

