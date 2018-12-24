import json

di = {'The big bang theory': [2, 10, 'thumbnails/bigbang.gif'], 'Two broke girls': [4, 20, 'thumbnails/2-broke-girls-539.gif'], 'Game of thrones': [7, 6, 'thumbnails/game-of-thrones-481.gif '], 'Breaking Bad': [5, 1, 'thumbnails/breaking-bad-2583.gif '], 'Scorpion': [3, 2, 'thumbnails/scorpion-1111.gif ']}

with open('series_table.json', 'w+') as f:

    json.dump(di, f, indent=2)


