import random
Board = ['1','2','3','4','5','6','7','8','9']
def playeraction():
    players_input = input("Type your coordinates\n")
    try:
        match (players_input):
            case '1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9':
                i = Board.index(players_input)
                Board[i]='O'
                Game_board()                
    except ValueError:
        print("not a valid coordinate.")

def Game_board():        
    print(Board[0:3:1])
    print(Board[3:6:1])
    print(Board[6:9:1])
    
def checking_win(symbol):
    win_conditions=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    return any(all(Board[i] == symbol for i in condition) for condition in win_conditions)

def Ai_action():
    available_moves = [pos for pos in Board if pos not in ['O', 'X']]
    randomizor = random.SystemRandom()
    ai_input= randomizor.choice(available_moves)
    match (ai_input):
        case '1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9':
            i = Board.index(ai_input)
            Board[i]='X'
            Game_board()                

def Check_Tie():
    return all(space in ['O', 'X'] for space in Board)

print("Starting a game of tik tac toe! type a coordinate to place O.")
print("1|2|3")
print("4|5|6")
print("7|8|9")
GameWin = False
while not GameWin:
    playeraction()
    if checking_win('O'):
        print("player wins")
        break
    if Check_Tie():
        print("Tie")
        break
    print('\n')
    Ai_action()
    if checking_win('X'):
        print("Ai wins")
        break
    if Check_Tie():
        print("Tie")
        break
print("game over!")