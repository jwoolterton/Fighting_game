from random import randint


def main():
    # Variables and what is your name

    players = []
    player_stats = {}
    player_scores = {}
    max_player_stats = 10

    # get the name of the 2 players store them into a list and set their scores to 0
    print("What is your name?")
    for n in range(0, 2):
        player_name = input("Player " + str(n + 1) + "? ")
        print("player {0} is {1}".format(n + 1, player_name))
        players.append(player_name)
        player_scores[player_name] = 0

    # print(str(players))

    # for each player input their attack stat, calculate their defense stat and store them in a map
    for name in players:
        print(name)
        attack = int(input("{0} input your attack stat".format(name)))
        defense = max_player_stats - attack
        player_stats[name] = [attack, defense]
    print(player_stats)

    # organizing rounds
    for round in range(0, 3):
        print("starting round {0}".format(round + 1))
        attacker, defender = players

        # Battle scene
        for player in players:

            # get the attacker stats from the player stats map, callulate the total attack by rolling a dice and adding
            # it to the attackers attack stat
            print("{0} attacks {1}".format(attacker, defender))
            attack, defense = player_stats[attacker]
            total_attack = randint(1, 6) + attack

            # get the defender stats from the player stats map, callulate the total defense by rolling a dice and
            # adding it to the defenders defense stat
            attack, defense = player_stats[defender]
            total_defense = randint(1, 6) + defense
            print(
                "{0}'s attack is {1} and {2}'s defense is {3}".format(attacker, total_attack, defender, total_defense))

            # calculate the scores
            if total_attack > total_defense:
                player_scores[attacker] += 1

            # rotate who the attacker and defender are
            defender, attacker = attacker, defender

            input()

    print(str(player_scores))

    # find out who is the winner
    if player_scores[players[0]] > player_scores[players[1]]:
        print("{0} is the winner!!!".format(players[0]))

    elif player_scores[players[1]] > player_scores[players[0]]:
        print("{0} is the winner!!!".format(players[1]))

    else:
        print("It's a draw")
