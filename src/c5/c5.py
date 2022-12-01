import json

file = open('input.json', 'r')
initialPlayers = json.load(file)

players = []
for idx, player in enumerate(initialPlayers):
    players.append({'name': player, 'alive': True, 'idx': idx})


while len(players) > 1:
    for i in range(len(players)):
        if i % 2 != 0:
            players[i]['alive'] = False

    if players[len(players)-1]['alive'] and players[0]['alive']:
        players[0]['alive'] = False

    players = [player for player in players if player['alive']]


print(players[0]['name'] + "-" + str(players[0]['idx']))


            



    



