from constants import TEAMS
from constants import PLAYERS

def team_names(TEAMS):
    team_one = TEAMS[0]
    team_two = TEAMS[1]
    team_three = TEAMS[2]

def clean_data(PLAYERS):
    cleaned = []
    for player in PLAYERS:
        fixed = {}
        fixed["height"] = int(player["height"].split(" ")[0])
        if player["experience"] == "YES":
            fixed["experience"] = True
        else:
            fixed["experience"] = False
        fixed["name"] = str(player["name"])
        fixed["guardians"] = player["guardians"].split(" and ")
        cleaned.append(fixed)
    return cleaned

def main():
    players_new = clean_data(PLAYERS)
    experienced = []
    inexperienced = []
    for player in players_new:
        if player["experience"] == True:
            experienced.append(player)
        else:
            inexperienced.append(player)

    team_one = []
    team_two = []
    team_three = []

    def balance_teams(team):
        team.extend(experienced[0:3])
        experienced.pop(0)
        experienced.pop(0)
        experienced.pop(0)
        team.extend(inexperienced[0:3])
        inexperienced.pop(0)
        inexperienced.pop(0)
        inexperienced.pop(0)

    balance_teams(team_one)
    balance_teams(team_two)
    balance_teams(team_three)

    def experienced_count(team):
        experienced_players = 0
        inexperienced_players = 0
        for player in team:
            if player["experience"] == True:
                experienced_players += 1
            elif player["experience"] == False:
                inexperienced_players += 1
        print("Total experienced: {}".format(experienced_players))
        print("Total inexperienced: {}".format(inexperienced_players))

    def players_on_team(team):
        all_names = []
        print("\nPlayers on Team:")
        for player in team:
            all_names.append(player["name"])
        print(", ".join(all_names))

    def guardians_on_team(team):
        print("\nGuardians:")
        all_guardians = []
        for player in team:
            all_guardians.extend(player["guardians"])
        print(", ".join(all_guardians))

    def height_calculation(team):
        all_heights = []
        num_of_players = int(len(team))
        for player in team:
            all_heights.append(player["height"])
        avg_height = round(sum(all_heights) / num_of_players)
        print("Average height (inches): {}".format(avg_height))


    print("BASKETBALL TEAM STATS TOOL\n\n")
    print("--- Menu ---\n\n")
    print("Here are your choices:\nA) Display Team Stats\nB) Quit")

    while True:
        answer = input("\nEnter an option:  ")
        if answer.lower() == "a":
            break
        elif answer.lower() == "b":
            print("Thank you! Come back again!")
            exit()
        else:
            print("That's not a valid choice, please select A or B!")

    while True:
        print("\nA) Panthers\nB) Bandits\nC) Warriors")
        answer = input("\nSelect your team:  ")
        if answer.lower() == "a":
            number_of_players = int(len(team_one))
            print("\nTeam: Panthers Stats\n-------------\nTotal players: {}".format(number_of_players))
            experienced_count(team_one)
            height_calculation(team_one)
            players_on_team(team_one)
            guardians_on_team(team_one)
            while True:
                answer = input("\nPress Enter to continue:  ")
                if answer == "":
                    break
                else:
                    print("Invalid input, try again!")
        elif answer.lower() == "b":
            number_of_players = int(len(team_two))
            print("\nTeam: Bandits Stats\n-------------\nTotal players: {}".format(number_of_players))
            experienced_count(team_two)
            height_calculation(team_two)
            players_on_team(team_two)
            guardians_on_team(team_two)
            while True:
                answer = input("\nPress Enter to continue:  ")
                if answer == "":
                    break
                else:
                    print("Invalid input, try again!")
        elif answer.lower() == "c":
            number_of_players = int(len(team_three))
            print("\nTeam: Warriors Stats\n-------------\nTotal players: {}".format(number_of_players))
            experienced_count(team_three)
            height_calculation(team_three)
            players_on_team(team_three)
            guardians_on_team(team_three)
            while True:
                answer = input("\nPress Enter to continue:  ")
                if answer == "":
                    break
                else:
                    print("Invalid input, try again!")
        else:
            print("Oops! Not a valid option. Please select A, B, or C to see your team's stats!")

if __name__ == "__main__":
    main()
