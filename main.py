#!/usr/bin/env python
"""
Let's play rock paper and scissors in python

"""
__author__ = "Noe Vazquez"
__email__ = "jonovagu@gmail.com"


from random import choice

class Game():
    __options = {"rock":1, "paper":2, "scissors":4}
    
    def __evaluate_winner(self, player_1, pc):
        result = Game.__options[player_1] + Game.__options[pc]
        winner = "IT'S A MATCH!!!"
        if result == 3: # rock + paper
            winner = "You WON" if player_1 == "paper" else "pc"
        elif result == 6: # paper + sscissors
            winner = "You WON" if player_1 == "scissors" else "pc"
        elif result == 5: # rock + scissors
            winner = "You WON" if player_1 == "rock" else "pc"

        return winner
            
    def __get_pc_answer(self):
        return choice(  list( Game.__options.keys() )  )

    def __check_option(self, option):
        return option in list(Game.__options.keys())

    def play(self):
        player1 = None
        while self.__check_option(player1) == False:
            player1 = input("   -> Your option [{}, {}. {}]: ".format(
                                                                *list( Game.__options.keys() )
                                                            )
                        )
            pc = self.__get_pc_answer()

        print(f"   -> {player1} vs {pc}(pc)")
        winner = self.__evaluate_winner(player1, pc)
        print(f"    Winner: {winner}")


if __name__ == "__main__":
    g = Game()
    repeat_game = True
    while repeat_game:
        g.play()
        ask_user = input("\n\nPlay again? [Y/n]")
        if ask_user.lower() == "n":
            repeat_game = False
    print("Bye Bye :D")