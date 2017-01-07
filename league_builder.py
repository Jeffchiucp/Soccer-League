import csv
import datetime
import random


def get_players(csv_file_name):
    """ Reads a csv file and returns a list of player dictionaries"""
    with open(csv_file_name, newline = '') as csvfile:
        player_list = csv.DictReader(csvfile)
        return list(player_list)


def build_teams(player_roster, team_names):
    """
    sorts a list of player dictionaries 'player_roster' into the teams listed
    in 'team_names' players are updated with 'Team Name' key from the team_names
    list.

    teams are sorted to have ballanced height and experience

    The function returns a tuple with lists of players for each team
    """

    # sort lists into experienced or not with decending height
    player_roster = sorted(player_roster,
                           key = lambda height: height['Height (inches)'],
                           reverse = True)

    player_roster = sorted(player_roster,
                           key = lambda exp: exp['Soccer Experience'],
                           reverse = True)

    league = [] # league = a list of teams. teams = list of player dictionaries
    for count in team_names: # initialise list with correct number of teams
        league.append([])

    # assign an index for league to team name
    team_names = enumerate(team_names, start = 0)
    team_names = list(team_names)
    # reverse the team name order players can be sorted forward then backwards
    rev_team_names = team_names[::-1]

    while player_roster:

        # add a player to each team from sorted list
        for count, team in team_names:
            try:
                player = player_roster.pop()
            except IndexError:
                break
            else:
                player.update({'Team Name': team})  # add team to player properties
                league[count].append(player)  # add to team list in league

        # add a player to each team from sorted list but in reverse for ballance
        for count, team in rev_team_names:
            try:
                player = player_roster.pop()
            except IndexError:
                break
            else:
                player.update({'Team Name': team})  # add team to player properties
                league[count].append(player)  # add to team list in league

    # write a new csv file with the players assigned to teams for future reference
    with open('team_roster.csv', 'w', newline="\n") as csvfile:
        fieldnames = league[0][0].keys() #get the fieldnames from first player
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()

        for league_team in league:
            for player in league_team:
                writer.writerow(player)

    return tuple(league)

def soccer_mum_fight():
    """
    This function returns a location and three possible weapons.
    The rest is left to your Imagination.
    """
    # we wont have a repeat of last years incident
    # with the {fruit}, {mobility} and {misc} {location}

    #improvised weapons
    fruit = ['water melon', 'orange wedges', 'pineapple', 'grapes', 'banana']
    mobility = ['wheel chair', 'skate board', 'Segway', 'bicycle', 'push scooter']
    misc = ['doggy doo', 'unsolicited advice', 'harsh words', 'wrestling', 'bike lock', 'stolen car keys']

    location = ['in the car park', 'on the side line', 'in the toilet block', 'in the changing rooms', 'now all over facebook']

    return random.choice(fruit), random.choice(mobility), random.choice(misc), random.choice(location)


def personal_letter(player_list):
    """
    creates a personalised introductory letter for each player in the teams
    'Dragons', 'Sharks' and 'Raptors' function requires a list of player dicts
    with the keys: Name, Guardian Name(s), Soccer Experience, Team Name.
    """
    project_requirements = True # set to false for better file names
    the_incident = soccer_mum_fight()
    dragons = {'Name': 'Dragons','Team Noise': 'WOOSH', 'First Practice': 'March 17th @ 1pm'}
    sharks = {'Name': 'Sharks','Team Noise': 'CHOMP', 'First Practice': 'March 17th @ 3pm'}
    raptors = {'Name': 'Raptors','Team Noise': 'ROAR', 'First Practice': 'March 18th @ 1pm'}
    date = str(datetime.date.today())
    #datestr = str(date)

    while player_list: # continue while there are still players in the list
        player = player_list.pop() # remove a player from the list

        if project_requirements:
            # file name lower case underscore separated
            letter_name = player['Name'].replace(' ', '_') +'.txt'
            letter_name = letter_name.lower()

        else:
            # create a date specific file name YYYY-MM-DD-Team-Player
            letter_name =(date + '-' + player['Team Name'] + '-' +
                          player['Name'].replace(' ', '-') +'.txt')

        if player['Team Name'] == 'Dragons':
            team = dragons
        elif player['Team Name'] == 'Sharks':
            team = sharks
        elif player['Team Name'] == 'Raptors':
            team = raptors
        else:
            pass

        with open(letter_name, "w") as file:
            file.write("".format()+"\n")
            file.write("Dear {}".format(player['Guardian Name(s)'])+"\n")
            file.write("""
This season {} has been selected to play for the {}. {} go {}!
                        """.format(player['Name'], team['Name'], team['Team Noise'], team['Name'])+"\n")
            # if the player has played before tell them why the teams have changed
            if player['Soccer Experience'] == 'YES':
                file.write("You may be wondering why you are not in the same team as last year." + "\n")
                file.write("Unfortunately we have decide that disbanding the previous teams and creating new more balanced teams" +"\n")
                file.write("was in the best interests of the League. We understand that football is a competitive sport however,"+"\n")
                file.write("in children's games fun and good sportsmanship should be the priority." + "\n")
                file.write("This also applies to parents! I feel I shouldn't have to say this but given" + "\n")
                file.write("the incident last season with the {}, {} and {} {}".format(*the_incident) + "\n")
                file.write("I feel I must remind you such behaviour is unacceptable.")
            else: # else welcome new players
                file.write("Welcome to the Children's football League. We encourage fun and good sportsmanship" +"\n")
                file.write("from both players and guardians. Please come along and encourage your children in this great sport" + "\n")

            file.write("\nYour fist practice session is on {} at Saxton Field, field 2.\n\n".format(team['First Practice']))
            file.write("Kind Regards\nJoshua Wilson\n(Teams Coordinator)")


if __name__ == "__main__":
    # part1: csv to list of dicts
    player_list = get_players('soccer_players.csv')
    team_names = ["Dragons", "Sharks", "Raptors"] #not limited to three teams

    # part2: sort teams by experience and height
    # (also creates a csv file with sorted teams team_roster.csv)
    dragons, sharks, raptors = build_teams(player_list, team_names)

    # part3: write letters for each team (limited to predefined teams)
    personal_letter(dragons)
    personal_letter(sharks)
    personal_letter(raptors)









    #dragons, sharks, raptors
