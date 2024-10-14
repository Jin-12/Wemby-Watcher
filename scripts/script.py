import requests 
from config.config import API_KEY

PLAYER_NAME = "Wembanyama"
spurs_id = 27
headers= {
    "Authorization": API_KEY
}

def get_wemby():
    response = requests.get("https://api.balldontlie.io/v1/players", headers=headers, params={"search":PLAYER_NAME})
    if response.status_code == 200:
        data = response.json()
        return data['data'][0]
    else: 
        print(f"Error: {response.status_code}, Response: {response.text}")
def extract_player_info(player):
    #Extract and return relevant player information as a dictionary
    player_info = {
        "id": player.get("id"),
        "first_name": player.get("first_name"),
        "last_name": player.get("last_name"),
        "position": player.get("position"),
        "height": player.get("height"),
        "weight": player.get("weight"),
        "jersey_number": player.get("jersey_number"),
        "college": player.get("college"),
        "country": player.get("country"),
        "draft_year": player.get("draft_year"),
        "draft_round": player.get("draft_round"),
        "draft_number": player.get("draft_number"),
        "team": player.get("team", {})
    }
    return player_info

def print_player_info(player_info):
    #Print player information in a clean format
    team = player_info["team"]
    print(f"Player ID: {player_info['id']}")
    print(f"Name: {player_info['first_name']} {player_info['last_name']}")
    print(f"Position: {player_info['position']}")
    print(f"Height: {player_info['height']}, Weight: {player_info['weight']} lbs")
    print(f"Jersey Number: {player_info['jersey_number']}")
    print(f"College: {player_info['college']}")
    print(f"Country: {player_info['country']}")
    print(f"Draft Year: {player_info['draft_year']}, Round: {player_info['draft_round']}, Pick: {player_info['draft_number']}")
    print(f"Team: {team.get('full_name', 'N/A')} ({team.get('abbreviation', 'N/A')})")
    print(f"Conference: {team.get('conference', 'N/A')}, Division: {team.get('division', 'N/A')}")
    print(f"City: {team.get('city', 'N/A')}")

def main():
    try:
        wemby = get_wemby()
        if wemby:
            player_info = extract_player_info(wemby)
            print_player_info(player_info)
    except Exception as e:
        print(f"Error:{e}")

if __name__ == "__main__":
    main()