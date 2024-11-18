Grid={'7': ' ', '8': ' ', '9':' ',
      '4': ' ', '5': ' ' , '6':' ',
      '1': ' ', '2': ' ' , '3':' '}
Keys=[]
for Key in Grid:
    Keys.append(Key)
def Print (grid):
    print(grid['7']+ '|'+grid['8']+'|' +grid['9']+'|')
    print(grid['4']+ '|'+grid['5']+'|' +grid['6']+'|')
    print(grid['1']+ '|'+grid['2']+'|' +grid['3']+'|')
def Game():
    Turn='X'
    Count=0
    for i in range (10):
        Print(Grid)
        print("Its your turn, " + Turn+". Now move to which place?")
        Move=input()
        if Grid[Move]==' ': 
           Grid[Move]=Turn
           Count+=1
        else:
            print("That place is already filled \n Move to which place?")
            continue
        if Count>=5:
            if Grid ['7']==Grid['8']==Grid['9']!=' ':
                Print(Grid)
                print("\n GAME OVER \n")
                print("****"+Turn+"Won*****")
                break
            elif Grid['1']==Grid['4']==Grid['7']!=' ':
                Print(Grid)
                print("\n GAME OVER \n")
                print("****"+Turn+"Won*****")
                break
            elif Grid['2']==Grid['5']==Grid['8']!=' ':
                 Print(Grid)
                 print("\n GAME OVER \n")
                 print("****"+Turn+"Won*****")
                 break
            elif Grid['3']==Grid['6']==Grid['9']!=' ':
                 Print(Grid)
                 print("\n GAME OVER \n")
                 print("****"+Turn+"Won*****")
                 break
            elif Grid['7']==Grid['5']==Grid['3']!=' ':
                 Print(Grid)
                 print("\n GAME OVER \n")
                 print("****"+Turn+"Won*****")
                 break
            elif Grid['1']==Grid['5']==Grid['9']!=' ':
                 Print(Grid)
                 print("\n GAME OVER \n")
                 print("****"+Turn+"Won*****")
                 break
        if Count==9:
            print("GAME OVER")
            print("ITS A TIEE")
        if  Turn=='X':
            Turn='O'
        else:
            Turn='X'
    Restart=input("Do you want to play agian?(Y/N)")
    if Restart=='Y'or Restart=='y':
       for key in Keys:
           Grid[key]=" "
       Game()
if __name__=="__Main__":
    Game()