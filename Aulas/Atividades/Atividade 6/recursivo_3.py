def Potencia(X,K):
    if K == 1:
        return X
    if K == 0:
        return 1
    return X * Potencia(X, K-1)

if __name__ == "__main__":
    X = int(input("Valor de X: "))
    K = int(input("Valor de K: "))
    
    print(Potencia(X,K))