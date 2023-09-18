
N = int( input("input N: "))
K = int( input("input K: "))
if K % 2 ==1:
    print(int(K/2+1))
else:
    print(int(N/2 + N%2 + K/2))