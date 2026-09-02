from random import choice
class RockPaperScissorsGame:
    OPTIONS=["rock","paper","scissors"]
    def check(self,user_input, computer_input):
        if(user_input==computer_input):
            print("Stalemate, Please play again!")
        elif(user_input =="rock" and computer_input=="scissors") or (user_input =="scissors" and computer_input=="paper"):
            print("Congratulations you win!")
        else:
            print("Computer wins!")

        if not self.play_again():
            print("Thanks for playing!")
            return


    def game_menu(self):
        while True:
            print("lets play Rock, Paper & scissors Game")
            user_input=input("Choose any one of them (Rock, Paper, Scissors, or 'quit' to exit):").strip()
            if user_input.lower() == 'quit':
                print("Thanks for playing!")
                break
            elif user_input.lower() in RockPaperScissorsGame.OPTIONS:
                computer_input= choice(RockPaperScissorsGame.OPTIONS)
                print("Computer picks : ",computer_input)
                self.check(user_input.lower(),computer_input.lower())
            else:
                print("Invalid input. Please enter Scissors, paper or Rock or 'quit'.")
                

    def play_again(self):
        answer=input("Do you want to play again? (yes/no)")
        return answer.lower() == "yes"



rock_scissor_paper=RockPaperScissorsGame()
rock_scissor_paper.game_menu()
