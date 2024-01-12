while True:
    try:
        a, b = map(int, input().split())
        arr = []
        for i in range(a):
            tmp = list(map(int, input().split()))
            arr.append(tmp)
        for j in range(b):
            for i in range(a):
                print(f"{arr[i][j]} ", end='')
            print("")
    except EOFError: break