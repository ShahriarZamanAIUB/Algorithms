import math
import random

def print_in_red(s):
    return('\x1b[0;31;40m' + s + '\x1b[0m')

def print_in_green(s):
    return('\x1b[0;32;40m' + s + '\x1b[0m')

def print_in_yellow(s):
    return('\x1b[0;33;40m' + s + '\x1b[0m')

def print_in_blue(s):
    return('\x1b[0;34;40m' + s + '\x1b[0m')

def get_optimal_diagonal(n):
    optimal_diagonal=[]
    for i in range(1,n*n+1,1):
     if(i%(n+1)==0):optimal_diagonal.append(i)

    return(optimal_diagonal)

def get_optimal_anti_diagonal(n):
    optimal_anti_diagonal=[]
    for i in range(1,n*n+1,1):
     if(i%(n-1)==0):optimal_anti_diagonal.append(i)
     
    return(optimal_anti_diagonal)       


def get_next_safe_boxes(n, row, queens): 
    # Function to get safe boxes in next row from the last queen added
    safe_boxes=[]
    for i in range(n*(row-1)+1,n*row+1,1):
            for j in range(0,len(queens),1):
                if(i%n==queens[j]%n): 
                  #  print(f"Excluding {i} due to Vertical Match with      {queens[j]}") # Vertical Match
                    safe_boxes = [k for k in safe_boxes if k!= i] # Removing a box if it is unsafe due to queens[j]
                    break # Stopping comparison with other values of queens[] since it might add them in safe_boxes again

                elif(math.floor((i-1)/n)+1==math.floor((queens[j]-1)/n)+1): 
                 #   print(f"Excluding {i} due to Horizontal Match with    {queens[j]}") # Horizontal Match
                    safe_boxes = [k for k in safe_boxes if k!= i] # Removing a box if it is unsafe due to queens[j]
                    break # Stopping comparison with other values of queens[] since it might add them in safe_boxes again

                elif(((i-1)//n - (i-1)%n)==((queens[j]-1)//n - (queens[j]-1)%n)):
                  #  print(f"Excluding {i} due to Diagonal Match   with    {queens[j]}") #  Diagonal Match (L->R)
                    safe_boxes = [k for k in safe_boxes if k!= i] # Removing a box if it is unsafe due to queens[j]
                    break # Stopping comparison with other values of queens[] since it might add them in safe_boxes again

                elif(((i-1)//n + (i-1)%n)==((queens[j]-1)//n + (queens[j]-1)%n)):
                  #  print(f"Excluding {i} due to Anti-Diagonal Match with {queens[j]}") # Anti-Diagonal Match (R->L)
                    safe_boxes = [k for k in safe_boxes if k!= i] # Removing a box if it is unsafe due to queens[j]
                    break # Stopping comparison with other values of queens[] since it might add them in safe_boxes again

                else: safe_boxes.append(i) # Append safe boxes to alist

            if(len(queens)==0): safe_boxes.append(i) # All boxes in a row are valid when no Queen has ben placed  

    return(sorted(list(set(safe_boxes))))  # Take only unique values and sort them before returning      

def forward_track(n,selected_queens,problem_queens):
    #print("\nForward Tracking...")
    safe_box=[]
    if(len(selected_queens)==n):
        print_chess_board(n, selected_queens)
        print(f"All {len(selected_queens)} queens placed successfully in the order {selected_queens}")
        return n, selected_queens, problem_queens, 2
    else:
        #print(f"Selected Queens: {selected_queens}")
        #print(f"Problem Queens: {problem_queens}")
        
        #print()
        if(len(get_next_safe_boxes(n, len(selected_queens)+1, selected_queens))==0): 
            #print(f"No new Queen can be placed after selecting {selected_queens}")
            #print_chess_board(n, selected_queens)
            #back_track(n,selected_queens,problem_queens)
            return n, selected_queens, problem_queens, -1
        
       #print(f"Available Safe Boxes: {get_next_safe_boxes(n, len(selected_queens)+1,selected_queens)}")
        updated_safe_boxes = [box for box in get_next_safe_boxes(n, len(selected_queens)+1,selected_queens) if box not in problem_queens] # Eliminating box in next row which stops convergence
        
        if(not updated_safe_boxes):
            #print("\nNo safe options left...") 
            #back_track(n,selected_queens,problem_queens)
            return n, selected_queens, problem_queens, -1
        else:
            #safe_box=random.choice(updated_safe_boxes) # Selecting first/random box in next row
            #safe_box=random.choice(updated_safe_boxes)
            #safe_box=updated_safe_boxes[0]

            selected_queens.append(random.choice(updated_safe_boxes))
            #selected_queens.append(updated_safe_boxes[0])

            #print(f"After selecting {selected_queens} :")
            #print_chess_board(n, selected_queens)
            #forward_track(n,selected_queens,problem_queens)
            return n, selected_queens, problem_queens, 1

def back_track(n,selected_queens,problem_queens):
    if(not selected_queens):
        #print(f"No solution exists for n={n}")
        return
     
    #print(f"\nBacktracking through {selected_queens}...")

    if(len(selected_queens)==1):
        problem_queens=[queen for queen in problem_queens if queen<=n]
        problem_queens.append(selected_queens.pop())
    else:
        problem_queens=[queen for queen in problem_queens if queen<=len(selected_queens)*n]
        problem_queens.append(selected_queens.pop())

       #problem_queens=sorted(list(set(problem_queens)))
    problem_queens=sorted(list(set(problem_queens)))


    forward_track(n,selected_queens,problem_queens)
    

def print_chess_board(n, values_at):
    print("Chess Board: ")
    for i in range(0,n*n,1):
        
        print("|", end='') # Print wall for visualization
        if((i+1) in values_at): print(print_in_green('1'), end='') # Print 1 where queens exist
        else:                   print(print_in_red('0'), end='') # Print 0 otherwise
        print("|", end='') # Print wall for visualization

        if((i+1)%n==0): # Print new row of Chessboard
            print()


def n_queens_solver(n):
    problem_queens=selected_queens=[]

    while(1):
        n, selected_queens, problem_queens ,status = forward_track(n,selected_queens,problem_queens)
        if(status==-1):
            if(not selected_queens):
                print(f"No solution exists for n={n}")
                break
        
        
            #print(f"\nBacktracking through {selected_queens}...")

            if(len(selected_queens)==1):
                problem_queens=[queen for queen in problem_queens if queen<=n]
                problem_queens.append(selected_queens.pop())

            else:
                problem_queens=[queen for queen in problem_queens if queen<=len(selected_queens)*n]
                problem_queens.append(selected_queens.pop())

            #problem_queens=sorted(list(set(problem_queens)))
            problem_queens=sorted(list(set(problem_queens)))
        

        elif(status==2):
            break

while(1):
    try:
        n=int(input("Enter n :"))
        n_queens_solver(n)
    except ValueError:
        print("Give proper input!")



 



