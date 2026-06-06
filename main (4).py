L=int(input("Enter the number of legs:"))
H=int(input("Enter the number of heads:"))
toss=False

for cows in range(H+1):
    hens=H-cows
    if(cows*4 + H*2==L):
        print(cows)
        print(hens)
        toss=True
    if(toss==False):
        print("No solution")