height= int(input("Enter the number for height:"))
width= int(input("Enter the number for width:"))
if height > 0  and width >0 :
     for i in range(height):
         for j in range(width):
             if(i == 0 or i== height- 1 or j==0 or j == width- 1):
                 print("*", end= " ")
             else:
                 print(" ", end=" ")
         print()  #for a newline when the row was done

else:
 print("Enter positive number")


