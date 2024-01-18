import math

def osszegzesTetel():
    n = int(input("N = "))
    while n < 0:
        n = int(input("N = "))
    ossz = 1
    for i in range(1, n + 1):
        ossz *= i
    print(f"Az első {n} db természetes szám összege: {ossz}")

def eldontesTelel():
    n = int(input("szám: "))
    prim = False
    if n < 2:
        prim = False
    else:
        i = 2
        while i <= n ** 0.5 and n % i != 0:
            i += 1
        prim = i > n ** 0.5
    print("Prím" if prim else "Nem prim")
