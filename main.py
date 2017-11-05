from random import randint
def main():

    # dddd
    print("What is your name?")
    players = []
    player_stats={}
    player_scores={}
    max_player_stats = 10

    # dddd
    for n in range(0,2):
        player_name=input("player " + str(n+1))
        print("player {0} is {1}".format(n+1, player_name) )
        players.append(player_name)
        player_scores[player_name]=0
    print(str(players))

    # dddd
    for name in players:
        print(name)
        attack=int(input("{0} input your attack stat".format(name)))
        defense=max_player_stats-attack
        player_stats[name]= [attack,defense]
    print(player_stats)

    # dddd
    for round in range(0,3):
        print("starting round {0}".format(round+1))
        attacker, defender = players

        # dddd
        for player in players:
            print ("{0} attacks {1}".format(attacker,defender))
            attack,defense=player_stats[attacker]

            total_attack= randint(1,6)+attack
            attack, defense = player_stats[defender]
            total_defense= randint(1,6)+defense
            print("{0}'s attack is {1} and {2}'s defense is {3}".format(attacker,total_attack, defender, total_defense))

            # dddd
            if total_attack>total_defense:
                player_scores[attacker]+=1
            defender,attacker=attacker,defender
            input()

    print(str(player_scores))

    # ddddd
    if player_scores[players[0]]>player_scores[players[1]]:
        print("{0} is the winner!!!".format(players[0]))

    elif player_scores[players[1]] > player_scores[players[0]]:
        print("{0} is the winner!!!".format(players[1]))

    else:
        print("It's a draw")