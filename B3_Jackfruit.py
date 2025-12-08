def header():
    print("        ===========================================")
    print("                   THE PYTHON GAME BOX")
    print("        ===========================================\n")

    print("                   Welcome to our Game\n" )
header()

import random as r
import time as t
import os

name = str(input("Enter your name:")).upper()
print("Hello",name +"!\n")

RPS = "RPS"
OXO ="OXO"
MEM = "MEM"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print("1) Rock Paper Scissor (RPS)")
    print("2) Tic Tac Toe (OXO)")
    print("3) Memory Challenge (MEM)\n")
    
    game = str(input("Choose Your Game (RPS,OXO,MEM): ")).upper()
    print()

    if game == RPS:

        def print_header():
            print("╔══════════════════════════════╗")
            print("║      WELCOME TO THE GAME     ║")
            print("╚══════════════════════════════╝")
        print_header()    
    
        round=1
        playing= True
        invalid_round,score_p1,score_p2=0,0,0
            
        def player_count():
            playing=True
            while playing:
                players=input('Enter number of players (max player-2): ')
                if players.isdigit():
                    players=int(players)
                if players in (1,2):
                    playing=False 
                else:
                    print('Invalid choice! Restart')
                    t.sleep(2)
                    clear()
                    print_header()
            return players

        count=player_count()
        choices = {1:'rock',2:'scissor',3:'paper'}

        if count==1:
            Player1 = str(input('Enter player name: ')).title()
            Player2="Computer"
            print(f'ඞ {Player1} ⚔︎  {Player2} 모')
            print()
        else:
            Player1= str(input('Enter player1 name: ')).title()
            Player2= str(input('Enter player2 name: ')).title()
            print(f'ඞ {Player1} ⚔︎  {Player2} ඞ')
            print()
            
        def get_choice(name):
            print('Choices 🡺 rock(1) , scissor(2)  , paper(3)')
            value= input(f'{name}, enter your choice(1/2/3):')
            clear()
            print(f'--Round{round}--')
            print()
            if value.isdigit():
                return int(value)
            else:
                return None

        def game():
            global score_p1,score_p2,invalid_round
            invalid_round = 0
            
            p1=get_choice(Player1)
            if count==1:
                p2= r.choice([1,2,3])
            else:
                p2=get_choice(Player2)
                
            if (p1 not in [1,2,3]) or (p2 not in [1,2,3]):
                print("✘ Invalid choice! Round restarting...")
                invalid_round=1
                t.sleep(2)
                return 
            else:
                if (choices[p1]==choices[1] and choices[p2]==choices[2]) or (choices[p1]==choices[2] and choices[p2]==choices[3]) or (choices[p1]==choices[3] and choices[p2]==choices[1]):
                    winner= Player1
                    score_p1+=1
                elif choices[p1]==choices[p2]:
                    winner="tie"
                else:
                    winner=Player2
                    score_p2+=1
                print("╔═════════RESULT═════════╗") 
                t.sleep(2)
                if winner=="tie":
                    print("║        ⚑ Draw ⚑        ║")
                else:
                    print(f'      {winner} Wins 🏅    ')
                print("╚════════════════════════╝")    
                print('✄┈┈┈┈┈┈┈THE CHOICES WERE:')
                t.sleep(1)
                print(f'➤ {Player1}: {choices[p1]}')
                t.sleep(1)
                print(f'➤ {Player2}: {choices[p2]}')
            
                
        while playing:
                print(f'--Round{round}--')
                print()
                game()
                if invalid_round==0:
                    round+=1
                else:
                    round+=0
                condition= str(input("Play Again? (Y/N): "))
                clear()
                if condition.upper()== "Y":
                    playing=True
                else:
                    playing=False
                    print("╔══════════════════════════════╗")
                    print("║         SCORE BOARD          ║")
                    print("╚══════════════════════════════╝")
                    print()
                    print(f"Rounds Played: {round-1}")
                    print(f'➤ {Player1} total score: {score_p1}')
                    print(f'➤ {Player2} total score: {score_p2}')
                    print()
                    print("╔═════════OVERALL WINNER═════════╗")
                    if score_p1>score_p2:
                        print(f'         {Player1}  🏆        ')
                    elif score_p1==score_p2:
                        print("║            ⚑  TIE  ⚑           ║")
                    else:
                        print(f'        {Player2} 🏆           ')
                        
                    print("╚════════════════════════════════╝")
                    t.sleep(5)    
                
    elif game == OXO:
        import tkinter 

        def set_tile(row, column):
            global curr_player

            if (game_over):
                return

            if board[row][column]["text"] != "":
                return
            
            board[row][column]["text"] = curr_player 

            if curr_player == Player1: 
                curr_player = Player2
            else:
                curr_player = Player1
            
            label["text"] = curr_player+"'s turn"
           
            check_winner()

        def check_winner():
            global turns, game_over
            turns += 1

            for row in range(3):
                if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
                    and board[row][0]["text"] != ""):
                    label.config(text=board[row][0]["text"]+" is the winner!", foreground=color_yellow)
                    for column in range(3):
                        board[row][column].config(foreground=color_yellow, background=color_light_gray)
                    game_over = True
                    return
            
            for column in range(3):
                if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
                    and board[0][column]["text"] != ""):
                    label.config(text=board[0][column]["text"]+" is the winner!", foreground=color_yellow)
                    for row in range(3):
                        board[row][column].config(foreground=color_yellow, background=color_light_gray)
                    game_over = True
                    return
            
            if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
                and board[0][0]["text"] != ""):
                label.config(text=board[0][0]["text"]+" is the winner!", foreground=color_yellow)
                for i in range(3):
                    board[i][i].config(foreground=color_yellow, background=color_light_gray)
                game_over = True
                return

            if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
                and board[0][2]["text"] != ""):
                label.config(text=board[0][2]["text"]+" is the winner!", foreground=color_yellow)
                board[0][2].config(foreground=color_yellow, background=color_light_gray)
                board[1][1].config(foreground=color_yellow, background=color_light_gray)
                board[2][0].config(foreground=color_yellow, background=color_light_gray)
                game_over = True
                return
            
            if (turns == 9):
                game_over = True
                label.config(text="Tie!", foreground=color_yellow)


        def new_game():
            global turns, game_over

            turns = 0
            game_over = False

            label.config(text=curr_player+"'s turn", foreground="white")

            for row in range(3):
                for column in range(3):
                    board[row][column].config(text="", foreground=color_blue, background=color_gray)


        Player1 = "X"
        Player2 = "O"
        curr_player = Player1
        board = [[0, 0, 0], 
                [0, 0, 0], 
                [0, 0, 0]]

        color_blue = "#4584b6"
        color_yellow = "#ffde57"
        color_gray = "#343434"
        color_light_gray = "#646464"

        turns = 0
        game_over = False

        window = tkinter.Tk()
        window.title("Tic Tac Toe")
        window.resizable(False, False)

        frame = tkinter.Frame(window)
        label = tkinter.Label(frame, text=curr_player+"'s turn", font=("Consolas", 20), background=color_gray,
                            foreground="white")
        label.grid(row=0, column=0, columnspan=3, sticky="we")

        for row in range(3):
            for column in range(3):
                board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"),
                                                    background=color_gray, foreground=color_blue, width=4, height=1,
                                                    command=lambda row=row, column=column: set_tile(row, column))
                board[row][column].grid(row=row+1, column=column)

        button = tkinter.Button(frame, text="restart", font=("Consolas", 20), background=color_gray,
                                foreground="white", command=new_game)
        button.grid(row=4, column=0, columnspan=3, sticky="we")

        frame.pack()


        window.update()
        window_width = window.winfo_width()
        window_height = window.winfo_height()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        window_x = int((screen_width/2) - (window_width/2))
        window_y = int((screen_height/2) - (window_height/2))

        #format "(w)x(h)+(x)+(y)"
        window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

        window.mainloop()
                        
    elif game == MEM:

        sym = ['A', 'B', 'C', 'D', 'E', 'F']

        board = sym* 2  

        r.shuffle(board)

        hidden_board= ['*'] * len(board)


        def display_board():
            print("Memory Game Board :")
            for i in range(len(hidden_board)):
                print(f"{i+1}:{hidden_board[i]}", end="  ")
                if (i + 1) % 4 == 0:
                    print()
            print()


        def play_game():
            turns = 0
            matches = 0
            while matches< len(board) // 2:
                clear()
                display_board()
                print(f"Turns taken: {turns}")
                try:
                    c1 = int(input("Choose the first card (1–12): ")) - 1
                    c2 = int(input("Choose the second card (1–12): ")) - 1
                except ValueError:
                    print("Please enter valid numbers(1-12)")
                    t.sleep(1)
                    continue

                if c1 == c2 or c1 not in range(12) or c2 not in range(12):
                    print("Number out of range.Please enter valid numbers(1-12)")
                    t.sleep(1)
                    continue

                hidden_board[c1] = board[c1]
                hidden_board[c2] = board[c2]
                clear()
                display_board()

                if board[c1] == board[c2]:
                    print("A Match has been found!")
                    matches += 1
                else:
                    print("Not a match.Try Again")
                    t.sleep(1)
                    hidden_board[c1] = '*'
                    hidden_board[c2] = '*'

                turns += 1
                t.sleep(1)

            print(f" You won in {turns} turns!")


        play_game()

    else:
        print("Game does not exist")
        print('Restarting...')
        t.sleep(2)
        clear()
        header()
        print("Hello",name +"!\n")
        continue
    
    again=input("Do you want to play again? (Y/N): ").upper()

    if again == "Y":
        print("\nRestarting...\n")
        continue

    elif again == "N":
        print("\nThank You for playing!")
        break

    else:
        print("\nInvalid input.")
        break
