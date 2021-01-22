from math import sqrt
import pickle


def SoZ_P5(N):
    """
    Takes a maximum limit and returns a 1 d boolean array that 
    corresponds to the prime numbers generated with
     prime = 30 * k + remainder
    where its state is stored in the bool array at 8*k + pos[remainder]
    """
    mod = 30
    rescnt = 8
    residues = [1, 7, 11, 13, 17, 19, 23, 29, 31]
    num = N - 1 | 1
    k = num // mod
    modk = mod * k
    r = 1
    while num >= modk + residues[r]:
        r += 1
    maxprms = k*rescnt + r - 1
    prms = [True] * maxprms

    pos = {}
    for i in range(rescnt):
        pos[residues[i]] = i - 1

    sqrtN = sqrt(num)
    modk, r, k = 0, 0, 0

    for i in range(maxprms):
        r += 1

        if r > rescnt:
            r = 1
            modk += mod
            k += 1

        if not prms[i]:
            continue

        res_r = residues[r]
        prime = modk + res_r

        if prime > sqrtN:
            break
        
        print(f"Generating Prime Map: {prime / sqrtN * 100}%")

        prmstep = prime * rescnt

        for ri in range(1, rescnt + 1):
            prod = res_r * residues[ri]
            ki = k * (prime + residues[ri]) + prod // mod
            np = ki * rescnt + pos[prod % mod]

            while np < maxprms:
                prms[np] = False
                np += prmstep
    return prms


def P5_PrimeConvert(prms):
    maxprms = len(prms)
    modk, r = 0, 0
    rescnt = 8
    mod = 30
    residues = [1, 7, 11, 13, 17, 19, 23, 29, 31]
    primes = [2, 3, 5]
    for i in range(maxprms):
        r += 1
        if r > rescnt:
            r = 1
            modk += mod
        if prms[i]:
            primes.append(modk + residues[r])
    return primes


def storePrimes(N, fName="pickledPrimes.pickle"):
    primeArray = SoZ_P5(N)
    with open(fName, "wb") as pf:
        pickle.dump(primeArray, pf)


def loadStoredPrimes(fName="pickledPrimes.pickle"):
    with open(fName, "rb") as pf:
        primeArray = pickle.load(pf)
    return primeArray
