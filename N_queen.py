
def print_solution(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j],end = " ")
        print()

def is_safe(board,row,col):
    #check the column above
    for i in range(row):
        if board[i][col] == 1:
            return False
        
    #check upper left diagonal    
    i, j = row-1,col -1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    #check upper right diagonal
    i, j = row-1, col +1
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_nqueens(board,row):
    if row == len(board):
        print_solution(board)
        print()
        return
    
    for col in range(len(board)):
        if is_safe(board,row,col):
            board[row][col] = 1
            solve_nqueens(board,row+1)
            board[row][col] = 0

def main():
    n = 4
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_nqueens(board,0)

if __name__ == "__main__":
    main()