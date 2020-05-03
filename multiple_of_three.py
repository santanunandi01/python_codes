#Given a string, return a string where for every character in the original there are three characte
str = "Santanu"
for i in  range (len(str)):
    letters = str[i]
    print(3*letters,end="")