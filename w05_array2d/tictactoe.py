"""
0. Worked with Nia Lam and Sarah Wu + Ducky: Mario 
1. Do you want to play tic tac toe
2. Player O: Select your spot. First give us the row (1, 2, 3)
3. Player O: Then give us the column (1, 2, 3). 
4. Display the game. 
5. Then it asks for player x 
6. this continues until all the spots filled out without a winner or there is a winner where a set of threes appear 
"""
arr = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
def make_board(): 
    for row in arr:
        print(row)
def place(row, col, num): #place an X or O if it can be placed (so if there is " ")
    if  arr[row-1][col-1] == " ":
        if num == 0:
            arr[row-1][col-1] = "O"
            print(arr[row-1][col-1])
        else:
            arr[row-1][col-1] = "X"
def start_game():
     play = input("Do you want to play tic tac toe: ")
     if play == "yes":
         make_board()
         for i in range(9):# a range of 9 is the total number of times you can input X or O before the grid is full
            #Player O time 
            row = int (input("Player O: Select your spot. First give us the row (1, 2, 3)"))
            col = int (input("Player O: Then give us the column (1, 2, 3)"))
            place(row,col, 0)
            make_board()
            if(win()):
                print("The winner is player O")
                break
            if(is_full()):
                print("It is a tie. Do better")
                break
            #Player X time 
            row = int (input("Player X: Select your spot. First give us the row (1, 2, 3)"))
            col = int (input("Player X: Then give us the column (1, 2, 3)"))
            place(row,col,1)
            make_board()
            if(win()):
                print("The winner is player O")
                break
            if(is_full()):
                print("It is a tie. Do better")
                break
def win(): #checks for a win 
    row1 = (arr[0][0] == arr[0][2] and arr[0][0] == arr[0][1] and arr[0][0] != " " )
    row2 = (arr[1][0] == arr[1][2] and arr[1][0] == arr[1][1] and arr[1][0] != " " )
    row3 = (arr[2][0] == arr[2][2] and arr[2][0] == arr[2][1] and arr[2][0] != " " )
    col1 = (arr[0][0] == arr[2][0] and arr[0][0] == arr[1][0] and arr[0][0] != " " )
    col2 = (arr[0][1] == arr[2][1] and arr[0][1] == arr[1][1] and arr[0][1] != " " )
    col3 = (arr[0][2] == arr[2][2] and arr[0][2] == arr[1][2] and arr[0][2] != " " )
    diagonal1 = (arr[0][0] == arr[2][2] and arr[0][0] == arr[1][1] and arr[0][0] != " " )
    diagonal2 = (arr[0][2] == arr[2][0] and arr[0][2] == arr[2][2] and arr[0][2] != " " )
    if (row1 or row1 or row3 or col1 or col2 or col3 or diagonal1 or diagonal2):
        return True
        
def is_full(): #check if the grid is full 
    for row in arr:
        for col in row: 
            if col == " ":
                return False 
    return True 
start_game()
