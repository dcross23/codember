

file1 = open('input.txt', 'r')
lines = file1.readlines()
  
users = []
newUser = {}
for line in lines:
    if line == '\n' or line == '  ': 
        users.append(newUser)
        newUser = {}
        continue  

    info = line.strip()
    for data in info.split(' '):
        key, value = data.split(':')
        newUser[key] = value


lastCorrectUser = {}
numCorrect = 0
for user in users:
    if "usr" not in user or "eme" not in user or "psw" not in user or "age" not in user or "loc" not in user or "fll" not in user:
        continue
    else:
        lastCorrectUser = user
        numCorrect += 1

print(numCorrect, lastCorrectUser["usr"])
