name = input("What is your name?")

#remove whitespace from the string 
name = name.strip()
#we can also do it like this also name = input("What is your name?").strip().tiltle for shorter code
#capatlize user name means captial letter me
name =name.capitalize()

#split user name into first and last name 
first, last = name.split(" ")
#say hello to user
print(f"hello, {first}")
