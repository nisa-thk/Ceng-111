n = int(input("Enter the number of rows:"))
if(n >0):
    for i in range(1, n+1):
        num_of_space= n-i
        num_of_star = 2*i -1
        print((" " * num_of_space) + ("*" * num_of_star))
    else:
        print("Enter a positive number")




