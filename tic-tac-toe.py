#Program: Tic-Tac-Toe with numbers.
#Author: Youssef mohamed mohamed 20230511
#version: V1.0
#Date: 3/1/2024



while True:
    while True:#this loop to make validation to the main menu
        print("A)start new game")
        print("B)exit game")
        choose1=input("please choose option: ")
        if choose1 not in ["A","a","B","b"]:
            print("Please enter a valid choise")
            continue
        else:break
    if choose1=="B"or choose1=="b":
        print("exiting the programe")
        break
    else:
        board=['111',"112","113","221","222","223","331","332","333"]#this is the postion numbers that will replace with the player number
        list1=["1","3","5","7","9"]#this list is the valid number for each player
        list2=["0","2","4","6","8"]
        def printboard(board):
            print(board[0]+"|"+board[1]+"|"+board[2])
            print("-----------")
            print(board[3]+"|"+board[4]+"|"+board[5])
            print("-----------")
            print(board[6]+"|"+board[7]+"|"+board[8])
        for i in range (0,5):#this loop to make 5 round each round player 1 and 2 player except last round player 2 dosent pplay
            print("**************Player 1 turn***************")
            while True:
                llist1=" ".join(list1)    
                print("Remaining number is " +llist1)
                Player_1=input(" Player 1 Please enter an odd number from the remaining number: ")
                if Player_1 not in list1:
                    print("the number is not exist")
                    continue
                else:break
            while True:#this loop to the user that cant take wrong position
                printboard(board)
                Player_1_p=input("Please enter your position as 221,222,......etc: ")
                if Player_1_p not in board:
                    print("you cant take this position")
                    continue
                if len(Player_1_p)!=3:
                    print("you cant take this position")
                    continue
                else: break
            x=int(board.index(Player_1_p))#this is a way to replace the position to the number that choosed by first player
            board[x]=Player_1
            printboard(board)
            #this is the all possible values to check the lines
            check1=int(board[0])+int(board[1])+int(board[2])
            check2=int(board[3])+int(board[4])+int(board[5])
            check3=int(board[6])+int(board[7])+int(board[8])
            check4=int(board[0])+int(board[3])+int(board[6])
            check5=int(board[1])+int(board[4])+int(board[7])
            check6=int(board[2])+int(board[8])+int(board[5])
            check7=int(board[0])+int(board[4])+int(board[8])
            check8=int(board[2])+int(board[4])+int(board[6])
            if check1==15 or check2==15 or check3==15 or check4==15 or check5==15 or check6==15 or check7==15 or check8==15:
                print("player 1 is the winner")
                break
            list1.remove(Player_1)
            #this if beacuse the last loop player 2 won't play his turn
            if i!=4:
                while True:#the same algorithms for player 2
                    print("**************Player 2 turn***************")
                    llist2=" ".join(list2)    
                    print("Remaining number is " +llist2)
                    Player_2=input(" Player 2 Please enter an even number from the remaining number: ")
                    if Player_2 not in list2:
                        print("the number is not exist")
                        continue
                    else:break
                while True:
                    printboard(board)
                    Player_2_p=input("Please enter your position as 221,222,......etc: ")
                    if Player_2_p not in board:
                            print("you cant take this position")
                            continue
                    if len(Player_2_p)!=3:
                        print("you cant take this position")
                        continue
                    else: break
                x=int(board.index(Player_2_p))
                board[x]=Player_2
                printboard(board)
                check1=int(board[0])+int(board[1])+int(board[2])
                check2=int(board[3])+int(board[4])+int(board[5])
                check3=int(board[6])+int(board[7])+int(board[8])
                check4=int(board[0])+int(board[3])+int(board[6])
                check5=int(board[1])+int(board[4])+int(board[7])
                check6=int(board[2])+int(board[8])+int(board[5])
                check7=int(board[0])+int(board[4])+int(board[8])
                check8=int(board[2])+int(board[4])+int(board[6])
                if check1==15 or check2==15 or check3==15 or check4==15 or check5==15 or check6==15 or check7==15 or check8==15:
                    print("player 2 is the winner")
                    break
                list2.remove(Player_2)
            if i==4:
                print("the game is draw")
            