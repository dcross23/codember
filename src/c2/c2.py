
file1 = open('input.txt', 'r')
lines = file1.readline().strip().split(' ')

fullMsg = ""
for line in lines:
    asciiLetter = ""
    message = ""
    for letter in line:
        asciiLetter += str(letter)
        if int(asciiLetter) >= 97 and int(asciiLetter) <= 122:
            newChar = chr(int(asciiLetter))
            message += newChar
            asciiLetter = ""

    fullMsg += (message + " ")

print(fullMsg)
    

