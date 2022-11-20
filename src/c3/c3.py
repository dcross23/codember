import json

file = open('input.txt', 'r')
colors = json.load(file)

chainLength = 0
longestChainLength = 0
lastColorLongestChain = ''
lastColor = ''
nextColor = colors[2]

for color in colors:
    if color != nextColor or lastColor == color:
        chainLength = 1

    chainLength += 1
    nextColor = lastColor
    lastColor = color

    if chainLength > longestChainLength:
        longestChainLength = chainLength
        lastColorLongestChain = lastColor

print(str(longestChainLength) + "@" + lastColorLongestChain)
            



    



