import csv
import requests

url = "https://free-nba.p.rapidapi.com/players"

headers = {
	"X-RapidAPI-Key": "d4c2df8ae2msh3190d5e7ffb1d20p137876jsn03021e078112",
	"X-RapidAPI-Host": "free-nba.p.rapidapi.com"
}
querystring = {"page":"1","per_page":"100"}

players = []
next_page = True

while next_page is not None:
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    players_batch = data["data"]

    for player in players_batch:
        player["full_name"] = f"{player['first_name']} {player['last_name']}"
        player["team"] = player["team"]["full_name"]
        del player["height_inches"]
        del player["height_feet"]
        del player["weight_pounds"]
        del player["first_name"]
        del player["last_name"]
        players.append(player)
    next_page = data["meta"]["next_page"]
    querystring["page"] =  f"{next_page}"


with open("nba_players_report.csv", mode='w', newline='') as file:
    writer = csv.DictWriter(file, ["id", "full_name", "position", "team"])
    writer.writeheader()
    writer.writerows(players)
