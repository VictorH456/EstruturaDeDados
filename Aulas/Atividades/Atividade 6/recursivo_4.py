def Tribonacci(N):
    if N <= 1:
        return 0
    if N == 2:
        return 1
    return Tribonacci(N-1) + Tribonacci(N-2) + Tribonacci(N-3)
if __name__ == "__main__":
    N = int(input("Valor de N: "))
    
    print(Tribonacci(N))