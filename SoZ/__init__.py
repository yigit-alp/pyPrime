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

        print(f"Generating Prime Map: {prime / sqrtN * 100:0.2f}%")

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


class isPrimeHandler:
    def __init__(self, map=loadStoredPrimes()):
        self.__map = map
        self.__maplen = len(map)
        self.__residues = [1, 7, 11, 13, 17, 19, 23, 29, 31]
        if self.__maplen == 0:
            self.__max = 0
        else:
            self.__max = (self.__maplen // 8) * 30 + \
                self.__residues[self.__maplen % 8]

    def posGen(self, N):
        # MAKE SURE THAT N IS IN MAP BEFORE USING
        pos = {}
        for i in range(len(self.__residues)):
            pos[self.__residues[i]] = i - 1
        return (N // 30) * 8 + pos[N % 30]

    def isInMap(self, N):
        if N <= self.__max:
            return N % 30 in self.__residues
        else:
            raise Exception("Number greater than map scope. Consider generating a bigger map.")


    def isPrime(self, N):
        if N < 7:
            return N in [2, 3, 5]
        if self.isInMap(N):
            return self.__map[self.posGen(N)]
        else:
            return False


#jnddsfl