def Pell(N):
    if N <= 1 :
        return N
    return (2 * Pell(N - 1)) + Pell(N - 2)

if __name__ == "__main__":
    N = int(input("Valor de N: "))
    
    print(Pell(N))