import player_class


def pend_player_action(player):
    ans = input(f"\n{player.name} turn, current score: {player.score}, roll? [y/n] -> ")

    if ans == "y":
        print("rolling dice...\ndice shows [", player.roll_dice(), "]!")

        if player.score > 21:
            print("bust! you loose the round")
            player.score = 0
            player.is_done = True
        else:
            pend_player_action(player)
    elif ans == "n":
        player.is_done = True
    else:
        print("/invalid token/")
        pend_player_action(player)




players = []
is_everyone_done = False
txt = ""

print("=-=-= dice blackjack =-=-=\n")
print("write player names, if done, enter '-':")

while True:
    while txt != "-":
        txt = input("-> ")
        if txt != "-":
            players.append(player_class.Mplayer(txt))

    for player in players:
        if player.is_done == False:
            pend_player_action(player)   

    highest_score = 0
    winners = []
    for player in players:
        print(player.name, " scored: ", player.score)

        if player.score > highest_score:
            winners = player
            highest_score = player.score
        elif player.score == highest_score:
            winners.append(player)

        player.score = 0
        player.is_done = False
    
        
    print("\nthis round was won by: ", winners.name, "\n=-=-=-=-=-=-=-=-=-=-=-=-\n")