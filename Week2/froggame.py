

#Initial positions of the frog 
#Rules the left side frogs can move to right only and right side frogs can move only to left 

positions=['G','G','G','_','B','B','B']

print("Positions of the frog")
print("[1 2 3 4 5 6 7]")
print(positions)

#Winning positions
final_positions=['B','B','B','_','G','G','G']
# The data type of pos is String 
pos = input("Press q to quit else \nEnter position of piece to move:")

#invalid count 
invalid_count=0
#If the person presses q they quit since they could not finish the game so printing "You Loose"
while(True):
    #The no move possible option is set with invalid _ count if the Move not possible attempt exceeds 3 then automatically you loose
    if(pos=='q' or invalid_count>=3):
      print("You Lose")
      break
    elif(pos.isdigit() and int(pos)>0 and int(pos)<=7):
      pos=int(pos)-1
      if(pos>=0 and pos<=6):
        if(positions[pos]=='_'):
          print("No frog present in the position mentioned")
        else:
            if(positions[pos]=='G'):
                #Player has chosen a green frog, he/she jumps to the next lime
                if(positions[pos+1]=='_' and (pos+1)<7):
                    positions[pos]= '_'
                    positions[pos+1]='G'
                elif(positions[pos+2]=='_' and (pos+2)<7):
                    positions[pos]= '_'
                    positions[pos+2]='G'
                else: 
                   print("Move not possible")
                   invalid_count+=1
            elif(positions[pos]=='B'):
                #Player has chosen a blue frog, he/she jumps to the previous lime
                if((pos-1)>=0 and positions[pos-1]=='_'):
                    positions[pos]= '_'
                    positions[pos-1]='B'
                elif((pos-2)>=0 and positions[pos-2]=='_'):
                    positions[pos]='_'
                    positions[pos-2]='B'
                else: 
                   print("Move not possible")
                   invalid_count+=1
    else:
       print("Invalid input or Invalid position entered! Please enter a different move")
    #    if(pos>0 and pos<7):
    #       invalid_count+=1
    if(positions==final_positions):
        print(positions)
        print("You Win!")
        break
    print()
    print("Positions of the frog")
    print("[1 2 3 4 5 6 7]")
    print(positions)
    pos = input("Press q to quit else \nEnter position of piece to move:")


print("Game Over!! Thanks for playing.")