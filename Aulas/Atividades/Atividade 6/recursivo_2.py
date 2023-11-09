def soma_ate_N(N):
    if N == 0:
        return N
    return 1/N + (soma_ate_N(N-1))

if __name__ == "__main__":
    N = int(input("Valor: "))
    print(soma_ate_N(N))