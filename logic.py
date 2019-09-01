import json 

data=json.load(open("data.json"))
teams = data["teams"]
opponents = data["opponents"]
print(list(filter(lambda team: team not in opponents, teams)))