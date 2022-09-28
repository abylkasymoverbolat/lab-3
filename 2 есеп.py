A = int(input())
B = int(input())
if(A<B):
    for i in range(A, B):
        print(i)
elif A>B:
    for i in range (B,A):
        print(A-i)
else:
    print("A==B")