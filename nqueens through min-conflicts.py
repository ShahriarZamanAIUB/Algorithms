import math, random

def print_in_red(s):
    return('\x1b[0;31;40m' + s + '\x1b[0m')

def print_in_green(s):
    return('\x1b[0;32;40m' + s + '\x1b[0m')

def print_in_yellow(s):
    return('\x1b[0;33;40m' + s + '\x1b[0m')

def print_in_blue(s):
    return('\x1b[0;34;40m' + s + '\x1b[0m')

def conflict_exists(n, x, y):

    if(x%n==y%n): 
        # Vertical Match
        return 1  

    elif(math.floor((x-1)/n)+1==math.floor((y-1)/n)+1): 
        # Horizontal Match
        return 1   

    elif(((x-1)//n - (x-1)%n)==((y-1)//n - (y-1)%n)):
        # Diagonal Match (L->R)
        return 1 

    elif(((x-1)//n + (x-1)%n)==((y-1)//n + (y-1)%n)):
        # Anti-Diagonal Match (R->L)
        return 1
    
    else:
        # No Match
        return 0  


def check_overall_conflict(list):
    
    n=len(list)
        
    conflict_found=0
    for i in range(0, len(list), 1):
        
        for j in range(i+1, len(list), 1):
            if(list[i]%n==list[j]%n): 
                # Vertical Match
                conflict_found=1 
                break  

            elif(math.floor((list[i]-1)/n)+1==math.floor((list[j]-1)/n)+1): 
                # Horizontal Match
                conflict_found=1  
                break  

            elif(((list[i]-1)//n - (list[i]-1)%n)==((list[j]-1)//n - (list[j]-1)%n)):
                # Diagonal Match (L->R)
                conflict_found=1 
                break  

            elif(((list[i]-1)//n + (list[i]-1)%n)==((list[j]-1)//n + (list[j]-1)%n)):
                # Anti-Diagonal Match (R->L)
                conflict_found=1 
                break  

        if(conflict_found==1):
            
            break   

    if(conflict_found==0):
        #print(" No conflicts found")
        return 1
    else:
        #print(" Conflicts exist") 
        return 0     

 
        

def print_chess_board(n, values_at):
    queen_count=0
    print("Chess Board: ")
    for i in range(0,n*n,1):
        
        print("|", end='') # Print wall for visualization
        if((i+1) in values_at): 
            queen_count=queen_count+1
            print(print_in_green('1'), end='') # Print 1 where queens exist
        else:                   
            print(print_in_red('0'), end='') # Print 0 otherwise
        print("|", end='') # Print wall for visualization

        if((i+1)%n==0): # Print new row of Chessboard
            print()

def n_queens_random_queen_placer(n):
    
    placed_queens=[]
    for i in range(1, n*n-n+2, n):
        selected_position=random.randint(i,n*math.ceil(i/n))
        placed_queens.append(selected_position)
    
    if(n==len(placed_queens)):
        print_chess_board(n,placed_queens)
        return placed_queens
    else:
        print("n doesn't match with no. of queens")    

n_queens_random_queen_placer(8)
           
 

        