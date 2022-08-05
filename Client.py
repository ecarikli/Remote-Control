while True:
    abc = input("first: ")
    abc = abc.encode()
    bcd = input("second: ")
    bcd = bcd.encode()
    ansL = []
    for x in range(len(abc)):
        ans = abc[x] ^ bcd[x]
        ansL.append(ans)
    ansL = bytes(ansL).decode()
    print(ansL)