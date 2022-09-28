a = int(input()) #1-ші бүтін санды енгізу 20
b = int(input()) #2-ші бүтін санды енгізу  8
for i in range(a - (a + 1) % 2, b - b % 2, -2): #start - 20 - 21 % 2 (19) , stop - 8 - 8 % 2 (8), step - 2
    print(i) #19 17 15 13 11  9