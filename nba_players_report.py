import csv
import requests

# base url and endpoint for players information
url = "https://free-nba.p.rapidapi.com/players"

# providing credentials
headers = {
	"X-RapidAPI-Key": "",
	"X-RapidAPI-Host": "free-nba.p.rapidapi.com"
}

# Setting the page to begin with and the amount of results in a response
querystring = {"page":"0","per_page":"100"}

# initializing a list to store list of dictionaries with player info
players = []

# setting next page to true so the while loop can begin
next_page = True

while next_page is not None:
    response = requests.get(url, headers=headers, params=querystring)
	# grabbing our response
    data = response.json()

	# assigning list of player dictionaries that we will append to our players list
    players_batch = data["data"]

	# iterating through the players list in the response to create dictionary with the information required.
    for player in players_batch:
        player["full_name"] = f"{player['first_name']} {player['last_name']}"
        player["team"] = player["team"]["full_name"]
	    # removing columns we don't need
        del player["height_inches"]
        del player["height_feet"]
        del player["weight_pounds"]
        del player["first_name"]
        del player["last_name"]
	    # adding list of players to response to our parent list of players
        players.append(player)
	    
	# assigning next_page so that we can check if we need to iterate again
    next_page = data["meta"]["next_page"]
	# assigning the next_page number so that we call the next page on our next request
    querystring["page"] =  f"{next_page}"


# passing our list of dictionaries to the csv dictionary writer
with open("nba_players_report.csv", mode='w', newline='') as file:
    writer = csv.DictWriter(file, ["id", "first_name", "last_name" ,"full_name", "position", "team"])
    writer.writeheader()
    writer.writerows(players)
